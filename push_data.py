import requests
import csv
from io import StringIO
from dateutil import parser
import timeit

def download_csv_from_google_drive(url: str) -> [str]:
    # Get file ID from URL.  This will grab the second to last / which contains the file ID
    file_id = url.split("/")[-2]

    # Set up the URL for downloading the file
    download_url = f"https://drive.google.com/u/0/uc?id={file_id}&export=download"

    # Download the file contents
    response = requests.get(download_url)

    # Parse the CSV file contents
    lines = response.text.split("\n")

    # Convert CSV to list of dictionaries
    data = []
    for line in lines:
        row = line.split(",")
        data.append(row)
    return data


def inject_into_nodejs(row:[str]) -> None:
    if len(row) != 4:
        print ("Bad Row!")
        return

    url = "http://localhost:8080/api/insert"
    data = {
        "customer_id": row[0],
        "event_type": row[1],
        "transaction_id": row[2],
        "timestamp": parser.parse(row[3]).isoformat()
    }
    #Make the PUT request
    response = requests.put(url, json=data)
    #Check the response
    if response.status_code != 201:
        print(response)
        print("Error updating resource")

# URL from the typical "Share with Anyone who has a link" in google drive.
data = download_csv_from_google_drive("https://drive.google.com/file/d/1AmG477mTMaO8bqLe8fVnhDpOgRUJ9wV7/view?usp=sharing")
start_time = timeit.default_timer()
for row in data:
    inject_into_nodejs(row)
end_time = timeit.default_timer()
print("Time taken for insert of CSV:", end_time - start_time, "seconds")
