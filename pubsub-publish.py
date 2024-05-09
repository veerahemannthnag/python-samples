import os
from google.cloud import pubsub_v1

def publish_to_pubsub(project_id, topic_name, file_path):
  """Publishes content from a text file to a Pub/Sub topic.

  Args:
      project_id: Your Google Cloud project ID.
      topic_name: The name of the Pub/Sub topic to publish to.
      file_path: The path to the text file containing the data to publish.
  """

  publisher = pubsub_v1.PublisherClient()
  topic_path = publisher.topic_path(project_id, topic_name)

  # Read the text file
  try:
      with open(file_path, 'rb') as file:
          data = file.read()
  except FileNotFoundError:
      print(f"Error: File not found: {file_path}")
      return

  # Publish the data to the Pub/Sub topic
  future = publisher.publish(topic_path, data)
  message_id = future.result()

  print(f"Published message with ID: {message_id}")

if __name__ == "__main__":
  import argparse

  parser = argparse.ArgumentParser(description='Publish content to Pub/Sub topic')
  parser.add_argument('--project_id', help='Your Google Cloud project ID', required=True)
  parser.add_argument('--topic_name', help='The name of the Pub/Sub topic', required=True)
  parser.add_argument('--file_path', help='The path to the text file', required=True)

  args = parser.parse_args()

  publish_to_pubsub(args.project_id, args.topic_name, args.file_path)



# python publish_to_pubsub.py --project_id your-project-id --topic_name your-topic-name --file_path path/to/your/text.txt
