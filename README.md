# ppha30538-final-project

## Project Proposal Group 28
### Group Members
- Astari Raihanah (cNetID: astari)
- Surya Hardiansyah (cNetID: sur)

# Final Project: Carjacking Analysis in Chicago: Visualizing Trends for Policy Implications

## Project Overview
This project aims to analyze carjacking trends across Chicago neighborhoods to provide insights for fair insurance policy-making. 
Using public datasets from the Chicago Data Portal, we visualize carjacking hotspots, temporal trends, and allow dynamic exploration through an interactive Shiny dashboard.
The repository contains all the necessary code, data, and documentation for reproducing our analysis and findings.

## Data Source
Using datasets from the Chicago Data Portal, we examine spatial and temporal distributions of incidents.

## Datasets used
- Carjacking data from Chicago Data Portal. Contains detailed information on carjacking incidents, including location, date, and time.
- Neighborhood boundaries from Chicago Data Portal. Contains Geospatial data used to map carjacking incidents to specific neighborhood.

## Repository Structure
- `data/`: Contains raw and processed datasets.
- `shiny-app/`: Code for the interactive dashboard.
- `pictures/`: Images used in the writeup.
- `writeup/`: Final report in `.qmd`, `.html`, and `.pdf` formats.
- `requirements.txt`: List of Python dependencies for reproducibility.

## Key Features
1. Data Wrangling:
   - Merged carjacking data with neighborhood boundaries.
   - Created additional columns for time period categorization.
2. Static Visualization:
   - Choropleth map showing carjacking rates by neighborhood.
   - Line chart illustrating trends over time.
2. Shiny dashboard:
   - Interactive map for filtering carjackings by neighborhood, date, and time period.
   - Dynamic tvisualization of temporal trends with adjustable filters. 
   
## How to Run the Project
1. Clone the repository.
2. Install dependencies from `requirements.txt`.
3. Run the Shiny app:
   ```bash
   cd shiny-app
   python app.py

## Reproducibility
- All data processing and analysis steps are documented in the final-project.qmd file. By knitting this file, users can regenerate all results and plots.
- Ensure raw datasets are placed in the data/ folder or downloaded using the links provided in the code comments.

## Deliverables
- Static Plots: pictures/
- Interactive App: shiny-app/
- Writeup: final-project.qmd, available in PDF and HTML formats.

## Acknowledgments
- This project was completed as part of PPHA 30538 Data and Programming for Public Policy II course at the University of Chicago under the guidance of Professor Peter Ganong and Professor Maggie Shi.

## Contact
For any question, please reach out to:
- Surya Hardiansyah: sur@uchicago.edu
- Astari Raihanah: astari@uchicago.edu