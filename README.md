# ppha30538-final-project

## Project Proposal Group 28
### Group Members
- Astari Raihanah (cNetID: astari)
- Surya Hardiansyah (cNetID: sur)

# Final Project: Carjacking Analysis in Chicago: Visualizing Trends for Policy Implications

## Project Overview
This project analyzes carjacking incidents across Chicago neighborhoods (2001–2024), identifying spatial and temporal trends to offer actionable insights for policymakers and insurance companies. By combining data visualization, interactive exploration, and sentiment analysis, the project provides a comprehensive understanding of carjacking trends and their implications.
The repository contains all the necessary code, data, and documentation for reproducing our analysis and findings.

## Data Sources
Using datasets from the Chicago Data Portal, we examine spatial and temporal distributions of incidents.

## Datasets used
- Carjacking data from Chicago Data Portal. Contains detailed information on carjacking incidents, including location, date, and time.
- Neighborhood boundaries from Chicago Data Portal. Contains Geospatial data (GeoJSON) used to map carjacking incidents to specific neighborhood.

## Repository Structure
- `data/`: Contains raw and processed datasets.
- `shiny-app/`: Code for the interactive dashboard.
- `pictures/`: Images used in the writeup.
- `requirements.txt`: List of Python dependencies for reproducibility.
- Writeup: Final report in `.qmd`, `.html`, and `.pdf` formats.

## Key Features
1. Data Wrangling:
   - Merged carjacking data with neighborhood boundaries.
   - Created additional columns for time period categorization.
2. Static Visualization:
   - Choropleth map showing carjacking rates by neighborhood.
   - Line chart illustrating trends over time.
3. Interactive Shiny dashboard:
   - Interactive map for filtering carjackings by neighborhood, date, and time period.
   - Dynamic tvisualization of temporal trends with adjustable filters.
4. NLP Sentiment Analysis
   - Collected news articles and blog posts on carjacking and auto insurance in Chicago using SerpAPI.
   - Performed sentiment analysis to identify public attitudes and policy concerns.

   
## How to Run the Project
1. Clone the repository.
2. Install dependencies from `requirements.txt`.
3. Run the Shiny app:
   ```bash
   cd shiny-app/
   python app.py


## Reproducibility
- All data processing and analysis steps are documented in the final-project.qmd file. By knitting this file, users can regenerate all results and plots.
- Ensure raw datasets are placed in the data/ folder or downloaded using the links provided in the code comments.

## Deliverables
- Static Plots: pictures/
- Interactive App: shiny-app/
- Writeup: final-project.qmd, available in PDF and HTML formats.

## Insights and Findings
- Spatial Patterns: Carjacking hotspots identified in neighborhoods like Austin, West Garfield Park, Englewood, and West Englewood. These areas require targeted interventions such as increased patrols and community programs.
- Temporal Trends: A significant rise in carjacking incidents around 2020–2021, potentially due to societal disruptions like the COVID-19 pandemic.
- Sentiment Analysis: Predominantly negative public sentiment towards auto insurance policies tied to carjackings. Insights highlight the need for fair and transparent insurance pricing.

## Policy Implications
- Neighborhood Focus: Prioritize interventions in high-risk areas.
- Temporal Allocation: Align law enforcement resources with high-crime times.
- Insurance Reform: Advocate for data-driven and fair insurance policies.

## Acknowledgments
- This project was completed as part of PPHA 30538 Data and Programming for Public Policy II course at the University of Chicago under the guidance of Professor Peter Ganong and Professor Maggie Shi.

## Contact
For any question, please reach out to:
- Surya Hardiansyah: sur@uchicago.edu
- Astari Raihanah: astari@uchicago.edu