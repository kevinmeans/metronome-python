import requests

URL = "http://localhost:8080/api/query"

def query_customer_id_events_hour_buckets(customer_id: str, start_time: str, end_time: str) -> []:
    # Define the query parameters
    query_params = {
        "customer_id": customer_id,
        "start_time": start_time,
        "end_time": end_time
    }
    # Make the HTTP request
    response = requests.get(URL, params=query_params)

    # Check the response status code
    if response.status_code == 200:
        # Success, parse the response content
        return response.json()
    else:
        # Error, print the response
        print(response.text)

print("Customer: b4f9279a0196e40632e947dd1a88e857',start: '2021-03-01 00:00:23',end: '2021-03-03 00:00:00'")
results = query_customer_id_events_hour_buckets('b4f9279a0196e40632e947dd1a88e857','2021-03-01 00:00:23','2021-03-03 00:23:59')
for row in results:
    print(row)

print("Customer: '30330c9c4e7173ba9474c46ee5191570',start: '2021-03-01 00:00:23',end: '2021-03-03 00:00:00'")
results = query_customer_id_events_hour_buckets('30330c9c4e7173ba9474c46ee5191570','2021-03-01 00:00:23','2021-03-03 00:23:59')
for row in results:
    print(row)

print("Customer: 009b178fa33bd5d0459d8b2cb825f9f4',start: '2021-03-01 00:00:23',end: '2021-03-03 00:00:00'")
results = query_customer_id_events_hour_buckets('009b178fa33bd5d0459d8b2cb825f9f4','2021-03-01 00:00:23','2021-03-03 00:23:59')
for row in results:
    print(row)
