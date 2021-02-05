# CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Features
 * Requirements
 * Configuration
 * Troubleshooting
 * Developers
 
# INTRODUCTION
------------

The Prescribing dashboard provides primary care trust level prescribing data which is accessible to CCGs and physicians

#FEATURES
-----------
*A calculator is available to calculate creatinine clearance
*It is possible to view the percentages of each antimicrobial type from the main dahboard <br>
*A PDF report can be generated from the main page to summarise the data.<br>
*Antibiotic prescriptions can be interrogated by selecting a PCT from the dropdown and viewing the prescribing centres within each PCT<br>
 
  * after installing Flask, and running run.py, the database will load at http://127.0.0.1:5000/dashboard/home

 * For a full description of the dashboard, visit the project page:
   https://trello.com/b/gLyOVe8r/cfb-group-reticulated

 * To submit bug reports and feature suggestions, or track changes:
   https://github.com/uomdatascience/dashboard-reticulated2021/issues
   
# REQUIREMENTS
------------

The dashboard requires:

The tests have been written based on the downloaded database, and will not 
function as intended on a live version of the database 

 * Flask: <code>conda install -c anaconda flask </code>
 * Flask-squalchemy: <code> conda install -c conda-forge flask-sqlalchemy </code>
 * sqlalchemy:  <code>conda install -c anaconda sqlalchemy</code>

 
The test modules require:
 * Selenium: <code>conda install selenium</code>
 * nose:<code> conda install -c conda-forge nose2</code>
 * app.database.controllers: <code>from app.database.controllers import Database</code>
 * os module: <code>import os</code>
 * the driver for google chrome must be installed in the dashboard-reticulated2021 folder

 
# CONFIGURATION
-------------

The module has no menu or modifiable settings. There is no configuration. 

# TROUBLESHOOTING
---------------

 * If the page does not display, check the following:

   - Is the database file saved in the appropriate location
   

   
# DEVELOPERS
-----------

*PRODUCT OWNER - Igor Malashchuk<br>
*SCRUM MASTER - Jay Miles<br>
*DEVELOPERS - Yongwun Ju, Viveck Kingsley, Sophie Maxey<br>