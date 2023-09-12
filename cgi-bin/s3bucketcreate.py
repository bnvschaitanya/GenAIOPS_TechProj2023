#!/usr/bin/python3

import boto3
import cgi

print("Content-type: text/html")
print()


form = cgi.FieldStorage()

cmd =form.getvalue("b")

#file = form["d"]
#print(file.filename)
#print(cmd)

s3_client = boto3.client('s3',aws_access_key_id='ACCESS KEY',aws_secret_access_key='SECRET KEY')

response_s3 = s3_client.create_bucket(
       ACL='private',
       Bucket=cmd,
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    }
)

#s3upload = s3_client.upload_file(file.filename,'sidimagebucket','pics')

print("<pre>")
print("Below is your Response")
print(cmd)
print(response_s3)
#print(s3upload)
print("</pre>")