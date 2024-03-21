# ElastiCache to S3 Data Exporter

This Python Project exports data from Amazon ElastiCache for Redis to Amazon S3. It retrieves data from a specified Redis hash key and exports it to S3 as both CSV and JSON files.

## Project Structure
```bash
.
├── README.md
└── gitlab-ci.yaml
```

## Prerequisites

Before running the Project, make sure you have the following:

- **AWS Credentials**: Access key and secret key with permissions to interact with Amazon S3 and ElastiCache.
- **Python 3**: Installed on your system.
- **boto3 Library**: Installed via pip (`pip install boto3`).

## Configuration

1. **AWS Credentials**: Replace `'your_aws_access_key'`, `'your_aws_secret_key'`, and `'your_aws_region'` placeholders with your actual AWS access key, secret key, and region in the Python Project.
2. **Redis Endpoint**: Replace `'your_redis_endpoint'` placeholder with the endpoint of your Amazon ElastiCache for Redis instance.
3. **S3 Bucket Name**: Replace `'your_s3_bucket_name'` placeholder with the name of your Amazon S3 bucket.

## Usage

1. **Run the Project**: Execute the Python Project (`python redis_s3_data_exporter.py`) to export data from ElastiCache to S3.
2. **Check S3 Bucket**: After running the Project, check your Amazon S3 bucket for the exported CSV and JSON files.


