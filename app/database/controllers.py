"""
NAME:          database\controllers.py
AUTHOR:        Alan Davies (Lecturer Health Data Science)
EMAIL:         alan.davies-2@manchester.ac.uk
DATE:          17/12/2019
INSTITUTION:   University of Manchester (FBMH)
DESCRIPTION:   Contains the Database class that contains all the methods used for accessing the database
"""

from sqlalchemy.sql import func
from flask import Blueprint

from app import db
from app.database.models import PrescribingData, PracticeData

database = Blueprint('dbutils', __name__, url_prefix='/dbutils')

class Database:
    """Class for managing database queries."""
    def get_total_number_items(self):
        """Return the total number of prescribed items."""
        return int(db.session.query(func.sum(PrescribingData.items).label('total_items')).first()[0])

    def get_prescribed_items_per_pct(self):
        """Return the total items per PCT."""
        return db.session.query(func.sum(PrescribingData.items).label('item_sum')).group_by(PrescribingData.PCT).all()

    def get_distinct_pcts(self):
        """Return the distinct PCT codes."""
        return db.session.query(PrescribingData.PCT).distinct().all()

    def get_n_data_for_PCT(self, pct, n):
        """Return all the data for a given PCT."""
        return db.session.query(PrescribingData).filter(PrescribingData.PCT == pct).limit(n).all()

    def get_avg_ACTCOST(self):
        """Return average cost of all items"""
        return round(float(db.session.query(func.avg(PrescribingData.ACT_cost).label('average_ACT')).first()[0]), 2)
        
    def get_top_prescribed_item(self):
        """Return a list of the name top prescribed item, its count and the percentage out of all items"""

        top_pres_item = db.session.execute(''
        ' SELECT sum(items) AS total_number, BNFNAME' 
        '   FROM practice_level_prescribing' 
        '   GROUP BY BNFNAME'
        '   ORDER BY total_number DESC LIMIT 1').first()

        total_prescription = db.session.query(func.sum(PrescribingData.items).label('top_pres'), PrescribingData.BNF_name).first()
        # (total_count, item, percentage)

        return (top_pres_item[0], top_pres_item[1], round((top_pres_item[0]/ total_prescription[0]* 100), 2)) 


    def get_unique_drugs(self):
        """Return the total number of distinct items"""
        return db.session.query(PrescribingData.BNF_name).distinct().count()
