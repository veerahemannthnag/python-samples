# pip install simba.connector.bigquery

import simba.connector.bigquery as bigquery

# Create a connection object
connection = bigquery.Connection(
    project_id="my-project-id",
    credentials="my-service-account.json",
)

# Run a query
query = "SELECT * FROM my_dataset.my_table"
results = connection.query(query)

# Print the results
for row in results:
    print(row)

