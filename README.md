# metronome-python

Contains python code that interacts with the NodeJS webserver.

push_data.py:  Grabs the event data that can be found on google drive. It downloads the CSV and pushes each row to NodeJS and in turn the mysql backend databases.  I have found that this file took over 15 minutes to insert the 185K rows.  Yikes! This could easily be improved by changing the NodeJS server to accept batches of rows rather than injected each row one at a time. 

query.py:  Queries the NodeJS API endpoint to grab the requested data.  The NodeJS server contains the actual SQL logic.  This contains a couple of simple queries of various customer_ids and start/end times.  The output of commands found in query.py can be found in output.txt

push_data.py must be ran first to populate the backend database. 

Run the commands below after the kubernetes backend has been setup.

python3 push_data.py
python3 query.py

