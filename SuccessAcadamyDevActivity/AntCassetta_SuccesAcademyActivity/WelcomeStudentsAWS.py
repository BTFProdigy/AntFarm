import boto3
import botocore.exceptions
import re
import sys


def validate_email(student_email):
    email = student_email

    # Validate the email is a proper format. somthing@somewhere.com
    pattern = re.compile("^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")

    if pattern.match(student_email):
        return True
    else:
        return False


def get_students():
    # Get the service resource.
    dynamodb = boto3.resource('dynamodb')

    # Get table.
    try:
        table = dynamodb.Table('Student')
    except botocore.exceptions.ResourceNotFoundException as e:
        "Student table not found {e}"
        sys.exit(1)

    try:
        response = table.scan()
        student_data = response['Items']

        # Batched way to scan in the data
        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            student_data.extend(response['Items'])

    except botocore.exceptions.ClientError as e:
        print('Client encountered and issue {0}')

    # Quick check to be sure student data isn't empty.
    # Ideally I'd also have some logic in place to ensure there isn't any duplicates or other issues
    if not student_data:
        print('student data could not be retrieved please check data source and settings')
        sys.exit(1)
    else:
        return student_data


def send_student_email(data):

    aws_region = "us-east-1"

    sender = "Success Academy <anthonyrbc89@gmail.com>"

    for student in data:

        recipient = student['email']

        if validate_email(recipient):

            subject = "TEST! Welcome {0} to Success Academy Charter Schools".format(student['Name'])

            # The email body for recipients with non-HTML email clients.
            body_text = ("This is a Test (Python) welcome email!\r\n"
                         "This email was sent with Amazon SES using the "
                         "AWS SDK for Python (Boto)."
                         )

            # The HTML body of the email.
            body_html = """<html>
            <head></head>
            <body>
            <h1>TEST welcome to Success Academy {0}</h1>
              <p>This email was sent with
                <a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the
                <a href='https://aws.amazon.com/sdk-for-python/'>
                  AWS SDK for Python (Boto)</a>.</p>
            </body>
            </html>
                        """.format(student['Name'])

            # The character encoding for the email.
            char_set = "UTF-8"

            # Create a new SES resource and specify a region.
            client = boto3.client('ses', region_name=aws_region)

            # Try to send the email.
            try:
                # Provide the contents of the email.
                response = client.send_email(
                    Destination={
                        'ToAddresses': [
                            recipient,
                        ],
                    },
                    Message={
                        'Body': {
                            'Html': {
                                'Charset': char_set,
                                'Data': body_html,
                            },
                            'Text': {
                                'Charset': char_set,
                                'Data': body_text,
                            },
                        },
                        'Subject': {
                            'Charset': char_set,
                            'Data': subject,
                        },
                    },
                    Source=sender,

                )
            # Display an error if something goes wrong.
            except botocore.exceptions.ClientError as e:
                print(e.response['Error']['Message'])
            else:
                print("Email sent! Message ID:"),
                print(response['MessageId'])
        else:
            print('Invalid Student {0} email {1}'.format(student['ID'], student['email']))


def main():
    student_data = get_students()
    send_student_email(student_data)


if __name__ == '__main__':
    main()
