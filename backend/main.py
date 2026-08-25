from fastapi import FastAPI, UploadFile, File
import boto3
import os

app = FastAPI()

MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT", "http://localhost:9000")
ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY", "minioadmin")
SECRET_KEY = os.getenv("MINIO_SECRET_KEY", "minioadmin")

s3_client = boto3.client(
    "s3",
    endpoint_url=MINIO_ENDPOINT,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)

@app.get("/")
def read_root():
    return {"status": "Backend Active", "system": "FastAPI on K8s"}

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    bucket_name = "documents"

    try:
        s3_client.create_bucket(Bucket=bucket_name)
    except Exception:
        pass

    s3_client.upload_fileobj(file.file, bucket_name, file.filename)

    return {
        "filename": file.filename,
        "status": "Uploaded to Local S3"
    }
