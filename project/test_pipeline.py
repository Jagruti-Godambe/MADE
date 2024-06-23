import os
import unittest
import sqlite3
import pandas as pd
from pipeline import extract_data, save_to_sqlite  

class TestPipeline(unittest.TestCase):

    def setUp(self):
        self.dataset_identifier_co2 = 'ulrikthygepedersen/co2-emissions-by-country'
        self.dataset_identifier_crop = 'thedevastator/the-relationship-between-crop-production-and-cli'
        self.test_db_path = os.path.join('data', 'test_project_data.db')
        self.test_table_name = 'test_project_data'

        # Ensure test output directory is clean
        if os.path.exists('data/'):
            for file in os.listdir('data/'):
                os.remove(os.path.join('data/', file))
        else:
            os.makedirs('data/')
    def test_data_pipeline(self):
        # Run the data pipeline
        merged_data = extract_data(self.dataset_identifier_co2, self.dataset_identifier_crop)

        # Check if the output DataFrame is not empty
        self.assertFalse(merged_data.empty, "Merged data should not be empty")

        # Save the DataFrame to SQLite
        save_to_sqlite(merged_data, db_name='test_project_data.db', table_name=self.test_table_name, directory='data/')

        # Check if the SQLite file is created
        self.assertTrue(os.path.isfile(self.test_db_path), "SQLite database file was not created")

        # Verify the content of the SQLite database
        conn = sqlite3.connect(self.test_db_path)
        query = f"SELECT count(*) FROM {self.test_table_name}"
        result = pd.read_sql_query(query, conn)
        conn.close()
        self.assertGreater(result.iloc[0, 0], 0, "The database table should have at least one row")

    def tearDown(self):
        if os.path.exists(self.test_db_path):
            os.remove(self.test_db_path)
            
if __name__ == '__main__':
    unittest.main()
