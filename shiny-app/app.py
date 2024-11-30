# Import required packages
import pandas as pd
import altair as alt
import json
from pathlib import Path
from shiny import App, reactive, render, ui, Inputs
from shinywidgets import render_altair, output_widget
import geopandas as gpd

# Paths for data
carjacking_file = "data/processed_carjackings.csv"
neighborhood_file = "data/chicago_neighborhoods.geojson"

# Load carjacking and neighborhood data
df = pd.read_csv(carjacking_file)
neighborhoods = gpd.read_file(neighborhood_file)

# Convert 'date' column to datetime and extract date range
df["date"] = pd.to_datetime(df["date"], errors="coerce")
start_date = df["date"].dt.date.min()
end_date = df["date"].dt.date.max()

# Load GeoJSON for neighborhood boundaries
with open(neighborhood_file) as f:
    chicago_geojson = json.load(f)

# Prepare Altair GeoJSON data
geo_data = alt.Data(values=chicago_geojson["features"])

# Extract unique neighborhoods for filtering
unique_neighborhoods = sorted(df["pri_neigh"].dropna().unique())

# App UI
app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_select(
            id="neighborhood",
            label="Select Neighborhood",
            choices=["All"] + unique_neighborhoods,
            selected="All",
        ),
        ui.input_date_range(
            id="date_range",
            label="Select Date Range",
            start=str(start_date),  # Dataset's minimum date
            end=str(end_date),      # Dataset's maximum date
            min=str(start_date),    # Limit the earliest selectable date
            max=str(end_date),      # Limit the latest selectable date
        ),
        title="Carjacking Filters",
    ),
    ui.layout_columns(
        ui.card(
            ui.card_header("Carjacking Incidents Map"),
            output_widget("carjacking_map"),
            full_screen=True,
        ),
        ui.card(
            ui.card_header("Carjacking Trends Over Time"),
            output_widget("carjacking_trend"),
            full_screen=True,
        ),
    ),
    title="Interactive Carjacking Dashboard",
    fillable=True,
)

# Server logic
def server(input, output, session):
    @reactive.calc
    def filtered_df():
        # Filter by neighborhood and date range
        filtered = df.copy()
        if input.neighborhood() != "All":
            filtered = filtered[filtered["pri_neigh"] == input.neighborhood()]
        start_date, end_date = input.date_range()
        filtered["date"] = pd.to_datetime(filtered["date"], errors="coerce")
        filtered = filtered[
            (filtered["date"] >= pd.to_datetime(start_date))
            & (filtered["date"] <= pd.to_datetime(end_date))
        ]
        return filtered

    @render_altair
    def carjacking_map():
        # Prepare filtered data
        filtered_data = filtered_df()
        filtered_counts = filtered_data.groupby("pri_neigh").size().reset_index(name="count")

        # Map counts to the GeoJSON features
        for feature in chicago_geojson["features"]:
            pri_neigh = feature["properties"]["pri_neigh"]
            feature["properties"]["count"] = filtered_counts.set_index("pri_neigh")["count"].get(pri_neigh, 0)

        # Choropleth map
        map_chart = alt.Chart(alt.Data(values=chicago_geojson["features"])).mark_geoshape().encode(
            color=alt.Color("properties.count:Q", title="Carjackings"),
            tooltip=["properties.pri_neigh:N", "properties.count:Q"],
        ).project(
            type="equirectangular"
        ).properties(
            title="Carjacking Incidents by Neighborhood",
            width=600,
            height=400,
        )

        return map_chart


    @render_altair
    def carjacking_trend():
        # Aggregate data by month/year
        filtered_data = filtered_df()
        filtered_data["year_month"] = filtered_data["date"].dt.to_period("M")
        trend_data = filtered_data.groupby("year_month").size().reset_index(name="count")
        trend_data["year_month"] = trend_data["year_month"].astype(str)

        # Line chart
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