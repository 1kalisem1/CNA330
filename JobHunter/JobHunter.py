# This script pulls from a job website and stores positions into a database. If there is a new posting it notifies the user.
# CNA 330
# Semion Kalinin sskalinin@student.rtc.edu
#Alan, Brandon, Emily and Sam helped me with the project

import mysql.connector
import sys
import json
import urllib.request
import os
import time

# Connect to database
# You may need to edit the connect function based on your local settings.
def connect_to_sql():
    conn = mysql.connector.connect(user='root', password='',
                                  host='127.0.0.1',
                                  database='cna330')
    return conn

# Create the table structure
def create_tables(cursor, table):
    ## Add your code here. Starter code below
    cursor.execute('''CREATE TABLE IF NOT EXISTS Table jobhunter {
 ID INTEGER PRIMARY KEY AUTOINCREMENT,
 Type varchar
 Title varchar
 Description text
 Job_id varchar
 Created_at DATE
 Company varchar
 Location varchar
 How_to_apply varchar
}
    return
# Query the database.
# You should not need to edit anything in this function
def query_sql(cursor, query):
    cursor.execute(query)
    return cursor
# Add a new job
def add_new_job(cursor, jobdetails):
    ## Add your code here
    query = "INSERT INTO jobhunter (ID, Type, Title,Description, Job_id, Created_at, Company, Location, How-to_apply ) VALUES (1, "IT", "system admin", "any", "Oct 23 2019", "any", "Everett", "Online app")
    return query_sql(cursor, query)
# Check if new job
def check_if_job_exists(cursor, jobdetails):
    ## Add your code here
    query = "SELECT FROM WHERE = ("ID", "Type", Title", "Job_id") 
    return query_sql(cursor, query)
def delete_job(cursor, jobdetails):
    ## Add your code here
    Job_id = get_job_id(cursor, jobdetails)
    query = "UPDATE"
    return query_sql(cursor, query)
# Grab new jobs from a website
def fetch_new_jobs(arg_dict):
    # Code from https://github.com/RTCedu/CNA336/blob/master/Spring2018/Sql.py
    query = "https://jobs.github.com/positions.json?" + "location=seattle" ## Add arguments here
    jsonpage = 0
    try:
        contents = urllib.request.urlopen(query)
        response = contents.read()
        jsonpage = json.loads(response)
    except:
        pass
    return jsonpage
# Load a text-based configuration file
def load_config_file(filename):
    argument_dictionary = 0
    # Code from https://github.com/RTCedu/CNA336/blob/master/Spring2018/FileIO.py
    rel_path = os.path.abspath(os.path.dirname(__file__))
    file = 0
    file_contents = 0
    try:
        file = open(filename, "r")
        file_contents = file.read()
    except FileNotFoundError:
        print("File not found, it will be created.")
        file = open(filename, "w")
        file.write("")
        file.close()
    ## Add in information for argument dictionary
    return argument_dictionary
    
    for row in How_to_apply:
    argument_dictionary += row
    return argument_dictionary 
# Main area of the code.
def jobhunt(arg_dict):
    # Fetch jobs from website
    jobpage = fetch_new_jobs(arg_dict)
    # print (jobpage)
    for job in jobpage:
    if check_if_job_exists(cursor, job):
    return jobpage
   
# Setup portion of the program. Take arguments and set up the script
# You should not need to edit anything here.
def main():
    # Connect to SQL and get cursor
    conn = connect_to_sql()
    cursor = conn.cursor()
    create_tables(cursor, "table")
    # Load text file and store arguments into dictionary
    arg_dict = 0 (sys.argv[1])
    while(1):
        jobhunt(arg_dict)
        time.sleep(3600) # Sleep for 1h
    if __name__ == '__main__':
        main()
