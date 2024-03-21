import boto3
import redis
import csv
import io
import json

# AWS credentials and region
AWS_ACCESS_KEY = 'aws_access_key'
AWS_SECRET_KEY = 'aws_secret_key'
AWS_REGION = 'aws_region'

# ElastiCache for Redis endpoint
REDIS_ENDPOINT = 'redis_endpoint'
REDIS_PORT = 6379

# S3 bucket name
S3_BUCKET_NAME = 's3_bucket_name'

# Connect to ElastiCache for Redis
redis_client = redis.StrictRedis(host=REDIS_ENDPOINT, port=REDIS_PORT, decode_responses=True)

# Connect to S3
s3_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY, region_name=AWS_REGION)

def export_to_csv(data, filename):
    # Create CSV string from data
    csv_buffer = io.StringIO()
    csv_writer = csv.writer(csv_buffer)
    csv_writer.writerows(data)

    # Upload CSV file to S3
    s3_client.put_object(Body=csv_buffer.getvalue(), Bucket=S3_BUCKET_NAME, Key=filename)

def export_to_json(data, filename):
    # Convert data to JSON string
    json_data = json.dumps(data)

    # Upload JSON file to S3
    s3_client.put_object(Body=json_data, Bucket=S3_BUCKET_NAME, Key=filename)

def main():
    # Example: Export data to CSV
    data = redis_client.hgetall('my_hash_key')
    export_to_csv(data.items(), 'data.csv')

    # Example: Export data to JSON
    data = redis_client.hgetall('my_hash_key')
    export_to_json(data, 'data.json')

if __name__ == '__main__':
    main()
