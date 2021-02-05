"""
NAME:          views\controllers.py
AUTHOR:        Alan Davies (Lecturer Health Data Science)
EMAIL:         alan.davies-2@manchester.ac.uk
DATE:          18/12/2019
INSTITUTION:   University of Manchester (FBMH)
DESCRIPTION:   Views module. Renders HTML pages and passes in associated data to render on the
               dashboard.
"""

from flask import Blueprint, render_template, request
from app.database.controllers import Database

views = Blueprint('dashboard', __name__, url_prefix='/dashboard')

# get the database class
db_mod = Database()

# Set the route and accepted methods
@views.route('/home/', methods=['GET', 'POST'])
def home():
    """Render the home page of the dashboard passing in data to populate dashboard."""
    pcts = [r[0] for r in db_mod.get_distinct_pcts()]
    if request.method == 'POST':
        # if selecting PCT for table, update based on user choice
        form = request.form
        selected_pct_data = db_mod.get_n_data_for_PCT(str(form['pct-option']), 5)
        selected_pct_gp_anti = db_mod.get_antibiotic_total_in_gp_in_pct(str(form['pct-option']))

        print(selected_pct_gp_anti)
        # need to send pct-option 

    else:
        # pick a default PCT to show
        selected_pct_data = db_mod.get_n_data_for_PCT(str(pcts[0]), 5)
        selected_pct_gp_anti = db_mod.get_antibiotic_total_in_gp_in_pct(str(pcts[0]))

    # prepare data
    bar_data = generate_barchart_data()
    bar_values = bar_data[0]
    bar_labels = bar_data[1]

    anti_total, gp_name = generate_barchart_data_gp(selected_pct_gp_anti)

    title_data_items = generate_data_for_tiles()
    title_data_pct = generate_data_for_pcts()

    # render the HTML page passing in relevant data
    return render_template('dashboard/index.html', tile_data=title_data_items,tile_pct=title_data_pct,
                           pct={'data': bar_values, 'labels': bar_labels},
                           pct_list=pcts, pct_data=selected_pct_data, pct1={'data': anti_total, 'labels': gp_name})


def generate_barchart_data_gp(gp_data):
    """Generate the data needed to populate the gp barchart."""
    gp_name = []
    anti_total = []
    for data in gp_data: 
        gp_name.append(data[0])
        anti_total.append(data[1])
    return anti_total, gp_name

def generate_barchart_data():
    """Generate the data needed to populate the barchart."""
    data_values = db_mod.get_prescribed_items_per_pct()
    pct_codes = db_mod.get_distinct_pcts()

    # convert into lists and return
    data_values = [r[0] for r in data_values]
    pct_codes = [r[0] for r in pct_codes]
    return [data_values, pct_codes]



def generate_data_for_tiles():
    """Generate the data for the four home page titles."""
    return db_mod.get_total_number_items(), db_mod.get_avg_ACTCOST(), db_mod.get_top_prescribed_item(), db_mod.get_unique_drugs() 

def generate_data_for_pcts():
    """Generate the data for the four home page titles."""
    total_infection_drugs = db_mod.total_infection_drugs()
    list = ((db_mod.get_infection_drug_percentage_antibacterial()/total_infection_drugs)*100), ((db_mod.get_infection_drug_percentage_antifungal()/total_infection_drugs)*100), ((db_mod.get_infection_drug_percentage_antiviral()/total_infection_drugs)*100), ((db_mod.get_infection_drug_percentage_antiprotozoal()/total_infection_drugs)*100), ((db_mod.get_infection_drug_percentage_anthelmintics()/total_infection_drugs)*100)
    rounded_list = [round(num, 2) for num in list]
    return rounded_list