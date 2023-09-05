from google.cloud import bigquery
import time
import sys

def fetch_data(num_rows):
    # Initialize a BigQuery client
    client = bigquery.Client()

    # Define your query
    query = f"""
        SELECT *
        FROM `your_project_id.your_dataset_id.your_table_id`
        LIMIT {num_rows}
    """

    # Record the start time
    start_time = time.time()

    # Execute the query
    query_job = client.query(query)

    # Wait for the query to finish
    results = query_job.result()

    # Record the end time
    end_time = time.time()

    # Calculate the fetch time
    fetch_time = end_time - start_time

    # Print the fetched rows and fetch time
    print("Fetched rows:")
    for row in results:
        print(row)
    print(f"Fetch time: {fetch_time:.2f} seconds")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <num_rows>")
        sys.exit(1)

    num_rows = int(sys.argv[1])
    fetch_data(num_rows)
