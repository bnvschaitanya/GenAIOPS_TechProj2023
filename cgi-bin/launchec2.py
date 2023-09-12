#!/usr/bin/python3

import boto3 as bt
import cgi

print("Content-type: text/html")
print()

myec2 = bt.client("ec2",region_name='ap-south-1')

response = myec2.run_instances(
ImageId = "ami-0ded8326293d3201b",
InstanceType ="t2.micro",
MaxCount=1,
MinCount=1,
)

print("<pre>")
print("Below is your Response")
print(response)
print("</pre>")