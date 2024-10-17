
# Project Overview

## Analyzing the Impact of Climate Change on Crop Production and CO2 Emissions in the USA (1990-2015)

This Project aims to analyze and find the co relation between Crop production and Co2 emission in USA region from year 1990 to 2015.

## Technologies Used
1. `Data Analysis: Python (Pandas)`
2. `Visualization: Matplotlib`
3. `Version Control: Git, GitHub`

## Datasets

[**Crop Production & Climate Change**](https://www.kaggle.com/datasets/thedevastator/the-relationship-between-crop-production-and-cli):

This dataset provides data on crop yields, harvested areas, and production quantities for wheat, maize, rice, and soybeans. Crop yields are the harvested production per unit of harvested area for crop products. In most cases yield data are not recorded but are obtained by dividing the production data by the data on the area harvested. The actual yield that is captured on a farm depends on several factors such as the crop's genetic potential, the amount of sunlight, water, and nutrients absorbed by the crop, the presence of weeds and pests. This indicator is presented for wheat, maize, rice, and soybean. Crop production is measured in tonnes per hectare.

[**CO2 Emissions**](https://www.kaggle.com/datasets/ulrikthygepedersen/co2-emissions-by-country):

The CO2 emissions dataset provides a comprehensive overview of the amount of CO2 emitted by each country. The dataset includes information on CO2 emissions by country from 1960 to the present day. It covers all countries in the world and is compiled from various sources, including the United Nations Framework Convention on Climate Change (UNFCCC) and the International Energy Agency (IEA).

[**Project Data Report**](project/data-report.pdf): Document detailing data cleaning and pipeline procedures.

[**Project Analysis Report**](project/Analysis-report.pdf): Final report containing data analysis and visualizations.



## Analysis
The analysis focused on examining the trends in crop production and CO2 emissions over the 25-year period. Methods included statistical analysis and visualization to interpret the data patterns.

<img src="data/Screenshot 2024-07-03 at 20.48.09.png" width="700" height="466">

## Installation and Usage

### Setting Up the Environment

1. Clone the repository:
    ```bash
    git clone https://github.com/puni-ram48/MADE-SS2024.git
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Data Pipeline and Testing

### Data Pipeline [View Here](project/pipeline.py)
The project includes an automated data pipeline with the following stages:

- **Data Fetching**: Automatically retrieves datasets from specified sources.
- **Data Transformation & Cleaning**: Applies necessary transformations and cleaning to ensure data accuracy.
- **Data Loading**: Loads transformed data into structured formats ready for analysis.

### Testing the Pipeline [View Test Script](project/test_pipeline.py)
A comprehensive test script validates the entire data pipeline, ensuring:

- Accuracy in data retrieval.
- Proper application of data cleaning and transformation processes.
- Integrity and consistency of the transformed data.

### Continuous Integration (CI) Workflow [View CI Script](.github/workflows/CI_Execute_Test.yml)
An automated CI workflow is set up using GitHub Actions:

- **Continuous Integration (CI)**: Runs the test script on each push to the main branch to ensure pipeline reliability and functionality.

## Running the Data Pipeline and Tests

1. Run the data pipeline:
    ```bash
    python3 automated_datapipeline.py
    ```

2. Execute the test script:
    ```bash
    python3 automated_testing.py
    ```
## Results:
Showed variability over the period, influenced by factors such as industrial activities and changes in energy consumption.CO2 emissions showed a VARIABILITY.
Demonstrated a consistent increase despite variability, driven by advancements in agricultural technology and practices, as well as natural climate variability.

## License
This project is licensed under the CC0-1 Universal License - see the License file for details.

