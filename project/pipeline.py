import os
import pandas as pd
import sqlite3
from kaggle.api.kaggle_api_extended import KaggleApi

# Initialize Kaggle API
api = KaggleApi()
api.authenticate()

def import_data_from_kaggle_api(dataset_identifier, download_path='/tmp/kaggle_dataset/'):
    # Download the dataset to a temporary directory
    os.makedirs(download_path, exist_ok=True)
    api.dataset_download_files(dataset_identifier, path=download_path, unzip=True)

    # Locate the downloaded file
    for file in os.listdir(download_path):
        if file.endswith('.csv'):
            file_path = os.path.join(download_path, file)
            break

    # Load the dataset into a pandas DataFrame
    df = pd.read_csv(file_path)

    # Clean up the temporary directory
    for file in os.listdir(download_path):
        os.remove(os.path.join(download_path, file))
    os.rmdir(download_path)

    return df

def rename_columns_co2(co2_data):
    co2_data.columns = ['Country_Code', 'Country_Name', 'Year', 'Co2_Emission']
    return co2_data

def rename_columns_crop(crop_data):
    crop_data.columns = ['Index', 'Location', 'Indicator', 'Subject', 'Measure', 'Frequency', 'Year', 'Crop_Production_Value', 'Flag_codes']
    return crop_data

def filter_data(co2_data, crop_data):
    #Filter out the data for year 2000 to 2019
    crop_data_us = crop_data[(crop_data['Location'] == 'USA') & (crop_data['Year'].between(1990, 2015))]
    co2_data_us = co2_data[(co2_data['Country_Name'] == 'United States') & (co2_data['Year'].between(1990, 2015))]
    return crop_data_us, co2_data_us

def convert_year_to_datetime(crop_data_us, co2_data_us):
    #Convert time and year to datetime consistency
    crop_data_us['Year'] = pd.to_datetime(crop_data_us['Year'], format='%Y')
    co2_data_us['Year'] = pd.to_datetime(co2_data_us['Year'], format='%Y')
    return crop_data_us, co2_data_us

def calculate_averages(crop_data_us, co2_data_us):
    #Group by year and calculate average crop production and c02 emission values 
    crop_data_us = crop_data_us.groupby(crop_data_us['Year'].dt.year)['Crop_Production_Value'].mean().reset_index()
    co2_data_us = co2_data_us.groupby(co2_data_us['Year'].dt.year)['Co2_Emission'].mean().reset_index()
    return crop_data_us, co2_data_us

def merge_data(crop_data_us, co2_data_us):
    #Merge the dataset
    merged_data = pd.merge(crop_data_us, co2_data_us, on='Year')
    return merged_data

def save_to_sqlite(df, db_name='project_data.db', table_name='project_data', directory='data/'):
    os.makedirs(directory, exist_ok=True)
    db_path = os.path.join(directory, db_name)
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()
    print(f"Data saved to {db_path} in table {table_name}")

def extract_data(dataset_identifier_co2, dataset_identifier_crop):
    # Import data from Kaggle
    co2_data = import_data_from_kaggle_api(dataset_identifier_co2)
    crop_data = import_data_from_kaggle_api(dataset_identifier_crop)
    
    # Process the data
    co2_data = rename_columns_co2(co2_data)
    crop_data = rename_columns_crop(crop_data)
    
    crop_data_us, co2_data_us = filter_data(co2_data, crop_data)
    crop_data_us, co2_data_us = convert_year_to_datetime(crop_data_us, co2_data_us)
    crop_data_us, co2_data_us = calculate_averages(crop_data_us, co2_data_us)
    
    merged_data = merge_data(crop_data_us, co2_data_us)
    
    # Save to SQLite database in /data directory
    save_to_sqlite(merged_data, directory='data/')
    
    return merged_data

# Dataset identifiers
dataset_identifier_co2 = 'ulrikthygepedersen/co2-emissions-by-country'
dataset_identifier_crop = 'thedevastator/the-relationship-between-crop-production-and-cli'

# Extract and print the merged data
merged_data = extract_data(dataset_identifier_co2, dataset_identifier_crop)

