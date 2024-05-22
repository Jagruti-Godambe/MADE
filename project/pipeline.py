import pandas as pd


def extract_data(data_path_co2, data_path_crop):
    co2_data = pd.read_csv(data_path_co2)
    crop_data = pd.read_csv(data_path_crop)
    co2_data.columns = ['Country_Code', 'Country_Name', 'Year','Co2_Emission']
    crop_data.columns = ['Index', 'Location', 'Indicator','Subject', 'Measure',
                     'Frequency', 'Year', 'Crop_Production_Value','Flag_codes']
    
    #Filter out the data for year 2000 to 2015

    crop_data_us = crop_data[(crop_data['Location'] == 'USA') & (crop_data['Year'].between(1990, 2015))]
    co2_data_us = co2_data[(co2_data['Country_Name'] == 'United States') & (co2_data['Year'].between(1990, 2015))]
    
    #Convert time and year to datetime consistency

    crop_data_us.loc[:, 'Year'] = pd.to_datetime(crop_data_us['Year'], format='%Y')
    co2_data_us.loc[:, 'Year'] = pd.to_datetime(co2_data_us['Year'], format='%Y')
    
    crop_data_us = crop_data_us.assign(Average_Crop_Production=crop_data_us.groupby('Year')['Crop_Production_Value'].transform('mean'))
    co2_data_us = co2_data_us.assign(CO2_Emissions=co2_data_us.groupby('Year')['Co2_Emission'].transform('mean'))
    
    
    merged_data = pd.merge(crop_data_us, co2_data_us, on='Year')
    merged_data = merged_data.drop(['Index', 'Country_Name', 'Flag_codes','Country_Code'], axis=1)
    
    return merged_data




if __name__ == '__main__':
    data_path_co2 = 'data/co2_emissions_kt_by_country.csv'
    data_path_crop  = 'data/crop_production.csv'
    result_dataset = 'data/result.csv'
    result = extract_data(data_path_co2, data_path_crop)
    result.to_csv(result_dataset, index=False)
