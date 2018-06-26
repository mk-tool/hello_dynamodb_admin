import boto3

dynamodb = boto3.resource('dynamodb', region_name='localhost:8000', endpoint_url="http://localhost:8008")

table = dynamodb.Table('Movies')

response = table.put_item(
  Item={
      'id': 1,
      'title': "hello",
  }
)
