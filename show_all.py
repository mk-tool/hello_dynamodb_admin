import boto3

client = boto3.client('dynamodb', endpoint_url='http://localhost:8008', region_name='localhost:8000')
response = client.list_tables()
print(response)
