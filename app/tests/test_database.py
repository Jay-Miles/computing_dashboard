"""
NAME:          test_database.py
AUTHOR:        Alan Davies (Lecturer Health Data Science)
EMAIL:         alan.davies-2@manchester.ac.uk
DATE:          24/12/2019
INSTITUTION:   University of Manchester (FBMH)
DESCRIPTION:   Suite of tests for testing the dashboards database
               functionality.
"""

import unittest
import os
import inspect

from app import app
from app.database.controllers import Database
from selenium import webdriver

class DatabaseTests(unittest.TestCase):
    """Class for testing database functionality and connection."""
    def setUp(self):
        """Run prior to each test."""
        self.db_mod = Database()
        self.driver = webdriver.Chrome('./chromedriver')

    def tearDown(self):
        """Run post each test."""
        pass

    def test_get_total_number_items(self):
        """Test that the total number of itmems returns the correct value."""
        self.assertEquals(self.db_mod.get_total_number_items(), 8218165)

    def test_get_avg_ACTCOST(self):
        """Test that the average ACT cost is correct."""
        self.assertEquals(self.db_mod.get_avg_ACTCOST(), 76.22)

    def test_get_top_prescribed_item(self):
        """Test that the top prescribed item is identified correctly."""
        self.assertEquals(self.db_mod.get_top_prescribed_item(), (
            226307, 'Omeprazole_Cap E/C 20mg', 2.75))

    def test_get_unique_drugs(self):
        """Test that the total number of unique drugs returns the correct value."""
        self.assertEquals(self.db_mod.get_unique_drugs(), 13922)

    def test_creatinine_calculator(self):
        """Test that the creatinine calculator produces the correct output."""
        actual_path = os.path.dirname(
            os.path.abspath(inspect.stack()[0][1]))
        path_to_html = actual_path + '/app/templates/dashboard/index.html'
        print(path_to_html)
        driver = self.driver()
        driver.get(path_to_html)
        driver.find_element_by_id('pt_Age').send_keys(50)
        driver.find_element_by_id('pt_weight').send_keys(50)
        driver.find_element_by_id('pt_serum').send_keys(50)
        driver.find_element_by_id('male').send_keys()
        driver.find_element_by_id('calculate-button').click()

if __name__ == "__main__":
    unittest.main()