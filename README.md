# CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Requirements
 * Configuration
 * Troubleshooting
 
 * Developers
 
# INTRODUCTION
------------

The Prescribing dashboard provides primary care trust level prescribing data which is accessible to CCGs and physicians
A calculator is available to calculate creatinine clearance
It is possible to view the percentages of each antimicrobial type from the main dahboard
A PDF report can be generated from the main page to summarise the data. 
 * after installing Flask, and running run.py, the database will load at http://127.0.0.1:5000/dashboard/home

 * For a full description of the module, visit the project page:
   https://trello.com/b/gLyOVe8r/cfb-group-reticulated

 * To submit bug reports and feature suggestions, or track changes:
   https://github.com/uomdatascience/dashboard-reticulated2021/issues
   
# REQUIREMENTS
------------

The dashboard requires:

This app must be run on Google Chrome

 * Flask: conda install -c anaconda flask
 * Flask-squalchemy: conda install -c conda-forge flask-sqlalchemy
 * sqlalchemy:  conda install -c anaconda sqlalchemy

 
The test modules require:
 * Selenium: conda install selenium
 * nose: conda install -c conda-forge nose2
 * app.database.controllers: from app.database.controllers import Database
 * os module: import os
 * the driver for your browser must be installed in the dashboard-reticulated2021 folder

 
# CONFIGURATION
-------------

The module has no menu or modifiable settings. There is no configuration. When
enabled, the module will prevent the links from appearing. To get the links
back, disable the module and clear caches.

# TROUBLESHOOTING
---------------

 * If the page does not display, check the following:

   - Is the database file saved in the appropriate location
   

   
# DEVELOPERS
-----------

*PRODUCT OWNER - Igor Malashchuk<br>
*SPRINT MASTER - Jay Miles<br>
*DEVELOPERS - Yongwun Ju, Viveck Kingsley, Sophie Maxey<br>