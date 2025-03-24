import os
import boto3
from dotenv import load_dotenv

# Load environment variables from .env file
env_file = r"C:\Users\ASUS\Desktop\AILabEngineers\lab1\.env-non-dev"
load_dotenv(env_file)


# Read environment variables
S3_ENDPOINT_URL = os.getenv("S3_ENDPOINT_URL")
S3_ACCESS_KEY = os.getenv("S3_ACCESS_KEY")
S3_SECRET_KEY = os.getenv("S3_SECRET_KEY")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

# Function to check connection
def connect_s3():
    if not all([S3_ENDPOINT_URL, S3_ACCESS_KEY, S3_SECRET_KEY, S3_BUCKET_NAME]):
        raise ValueError("Error: Missing environment variables!")
    else:
        print("Successfully connected to MinIO!")

# Function to upload a file to MinIO
def upload_s3(file_path, object_name):
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    # Create MinIO client
    s3 = boto3.client(
        "s3",
        endpoint_url=S3_ENDPOINT_URL,
        aws_access_key_id=S3_ACCESS_KEY,
        aws_secret_access_key=S3_SECRET_KEY,
    )

    # Upload file
    s3.upload_file(file_path, S3_BUCKET_NAME, object_name)
    print(f"File '{file_path}' uploaded to '{S3_BUCKET_NAME}' as '{object_name}'")

# Main execution
if __name__ == "__main__":
    connect_s3()

    # usage
    file_path = "C:/Users/ASUS/Desktop/AILabEngineers/lab1/data/orders.csv"
    object_name = "orders_backup.csv"  # Stored with this name in MinIO

    upload_s3(file_path, object_name)
