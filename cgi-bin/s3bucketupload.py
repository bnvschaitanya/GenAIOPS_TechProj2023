#!/usr/bin/env python3
import cgi
import boto3
import os

AWS_ACCESS_KEY = 'AWS ACCESS KEY'
AWS_SECRET_KEY = 'AWS SECRET KEY'
BUCKET_NAME = 'sidimagebucket'

if not AWS_ACCESS_KEY or not AWS_SECRET_KEY:
    print("Content-Type: text/html\n")
    print("<h2>Error: AWS credentials not provided.</h2>")
    exit()

s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)

print("Content-Type: text/html\n\n")

form = cgi.FieldStorage()
file_item = form['file']

if file_item.filename:
    file_data = file_item.file.read()
    file_name = file_item.filename

    try:
        # Upload the file to S3
        s3.upload_fileobj(file_item.file, BUCKET_NAME, file_name)
        print("<h2>File uploaded successfully!</h2>")
    except Exception as e:
        print("<h2>Error uploading file: {}</h2>".format(e))
else:
    print("<h2>No file selected.</h2>")