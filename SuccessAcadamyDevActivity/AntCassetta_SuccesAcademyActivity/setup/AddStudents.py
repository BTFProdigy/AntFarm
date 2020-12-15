import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Get table.
table = dynamodb.Table('Student')

with table.batch_writer() as batch:
    batch.put_item(
        Item={
            'ID': 101,
            'Name': 'Block,Jenny',
            'email': 'anthonyrbc89+jenny@gmail.com',
        }
    )
    batch.put_item(
        Item={
            'ID': 102,
            'Name': 'Star,Ringo',
            'email': 'anthonyrbc89+ringo@gmail.com',
        }
    )
    batch.put_item(
        Item={
            'ID': 103,
            'Name': 'Lipa,Dua',
            'email': 'anthonyrbc89+Dua@gmail.com',
        }
    )


# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='Student')

# Print out some data about the table.
try:
    print(table.item_count > 3)
except AssertionError as e:
    print("New Student upload failed")
