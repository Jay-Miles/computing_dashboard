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
import re
from app import app
from app.database.controllers import Database
from pathlib import Path
from selenium import webdriver

class DatabaseTests(unittest.TestCase):
    """Class for testing database functionality and connection."""
    def setUp(self):
        """Run prior to each test."""
        self.db_mod = Database()

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
        
    def test_get_infection_drug_percentage_antibacterial(self):
        """Test that the percentage of antibacterials returns the correct value."""
        self.assertEquals(self.db_mod.get_infection_drug_percentage_antibacterial(), 196186)

    def test_get_infection_drug_percentage_antifungal(self):
        """Test that the percentage of antifungal returns the correct value."""
        self.assertEquals(self.db_mod.get_infection_drug_percentage_antifungal(), 12439)
        
    def test_get_infection_drug_percentage_antiviral(self):
        """Test that the percentage of antiviral returns the correct value."""
        self.assertEquals(self.db_mod.get_infection_drug_percentage_antiviral(),6383)

    def test_get_infection_drug_percentage_antiprotozoal(self):
        """Test that the percentage of antiprotozoal returns the correct value."""
        self.assertEquals(self.db_mod.get_infection_drug_percentage_antiprotozoal(), 22953)

    def test_get_infection_drug_percentage_anthelmintic(self):
        """Test that the percentage of anthelmintic returns the correct value."""
        self.assertEquals(self.db_mod.get_infection_drug_percentage_anthelmintics(), 551)

    def test_total_infection_drugs(self):
        self.assertEquals(self.db_mod.total_infection_drugs(), 238512)

    # def test_creatinine_calculator(self):

        # path = os.path.abspath(os.getcwd())
        # rel_path = 'chromedriver'
        # whole_path = os.path.join(path, rel_path)
        # self.driver = webdriver.Chrome(whole_path)

    #     """Test that the creatinine calculator produces the correct output."""
    #     driver = self.driver
    #     path = os.path.abspath(os.getcwd())
    #     rel_path = 'app/templates/dashboard/index.html'
    #     whole_path = os.path.join(path, rel_path)
    #     driver.get(whole_path)
        
    #     driver.find_element_by_id('pt_Age').send_keys(50)
    #     driver.find_element_by_id('pt_weight').send_keys(50)
    #     driver.find_element_by_id('pt_serum').send_keys(50)
    #     driver.find_element_by_id('male').send_keys()
    #     driver.find_element_by_id('calculate-button').click()

    def test_get_antibiotic_total_in_gp_in_pct(self):
        self.assertEquals(self.db_mod.get_antibiotic_total_in_gp_in_pct('116').first(), ('RECOVERY CENTRE BISHOP AUCKLAND', 1))


if __name__ == "__main__":
    unittest.main()