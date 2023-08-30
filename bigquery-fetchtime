from google.cloud import bigquery
import time

# Initialize a BigQuery client
client = bigquery.Client()

# Define your query
query = """
    SELECT * FROM `project-2021-vmw.mydataset.my_table` LIMIT 1000
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
