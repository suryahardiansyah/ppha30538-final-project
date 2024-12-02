from shiny import App, ui, render, reactive
from shinywidgets import render_altair, output_widget
import pandas as pd
import geopandas as gpd
import altair as alt
import json

# Paths for data
carjacking_file = "data/processed_carjackings.csv"
neighborhood_file = "data/chicago_neighborhoods.geojson"

# Load data
df = pd.read_csv(carjacking_file)
neighborhoods = gpd.read_file(neighborhood_file)

# Convert 'date' to datetime and extract date range
df["date"] = pd.to_datetime(df["date"], errors="coerce")
start_date = df["date"].dt.date.min()
end_date = df["date"].dt.date.max()

# Load GeoJSON for neighborhoods
with open(neighborhood_file) as f:
    chicago_geojson = json.load(f)

unique_neighborhoods = sorted(df["pri_neigh"].dropna().unique())

# Sidebar filters
filters = ui.sidebar(
    ui.input_select(
        id="neighborhood",
        label="Select Neighborhood",
        choices=["All"] + unique_neighborhoods,
        selected="All",
    ),
    ui.input_date_range(
        id="date_range",
        label="Select Date Range",
        start=str(start_date),
        end=str(end_date),
        min=str(start_date),
        max=str(end_date),
    ),
    title="Filters",
)

# Create the navigation structure
page1 = ui.nav_panel(
    "Map",
    ui.card(
        ui.card_header("Carjacking Incidents Map"),
        output_widget("carjacking_map"),
    ),
)

page2 = ui.nav_panel(
    "Trends",
    ui.card(
        ui.card_header("Carjacking Trends Over Time"),
        output_widget("carjacking_trend"),
    ),
)

app_ui = ui.page_sidebar(
    filters,
    ui.navset_card_tab(page1, page2),
    title="Interactive Carjacking Dashboard",
)

# Server logic
def server(input, output, session):
    @reactive.Calc
    def filtered_df():
        filtered = df.copy()
        if input.neighborhood() != "All":
            filtered = filtered[filtered["pri_neigh"] == input.neighborhood()]
        start_date, end_date = input.date_range()
        filtered = filtered[
            (filtered["date"] >= pd.to_datetime(start_date))
            & (filtered["date"] <= pd.to_datetime(end_date))
        ]
        return filtered

    @render_altair
    def carjacking_map():
        filtered_data = filtered_df()
        counts = filtered_data.groupby("pri_neigh").size().reset_index(name="count")

        for feature in chicago_geojson["features"]:
            pri_neigh = feature["properties"]["pri_neigh"]
            feature["properties"]["count"] = counts.set_index("pri_neigh")["count"].get(pri_neigh, 0)

        map_chart = alt.Chart(alt.Data(values=chicago_geojson["features"])).mark_geoshape().encode(
            color=alt.Color("properties.count:Q", title="Carjackings"),
            tooltip=["properties.pri_neigh:N", "properties.count:Q"],
        ).project(type="equirectangular").properties(
            title="Carjacking Incidents by Neighborhood",
            width=600,
            height=400,
        )
        return map_chart

    @render_altair
    def carjacking_trend():
        filtered_data = filtered_df()
        filtered_data["year_month"] = filtered_data["date"].dt.to_period("M")
        trend_data = filtered_data.groupby("year_month").size().reset_index(name="count")
        trend_data["year_month"] = trend_data["year_month"].astype(str)

        trend_chart = alt.Chart(trend_data).mark_line(point=True).encode(
            x=alt.X("year_month:T", title="Time (Year-Month)"),
            y=alt.Y("count:Q", title="Number of Incidents"),
            tooltip=["year_month:T", "count:Q"],
        ).properties(
            title="Carjacking Trends Over Time",
            width=800,
            height=400,
        )
        return trend_chart

app = App(app_ui, server)