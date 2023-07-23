import json

import boto3

from src.config.enviroments import ENVS


class SQSClient:
    def __init__(self):
        self.data = ""

    @staticmethod
    def send_message(message):
        sqs_client = boto3.client('sqs')
        message_attributes = {
            'MessageType': {
                'DataType': 'String',
                'StringValue': 'JSON'
            }
        }

        return sqs_client.send_message(QueueUrl=ENVS.SQS_URL,MessageBody=json.dumps(message),MessageAttributes=message_attributes)

    @staticmethod
    def receive_messages():
        sqs_client = boto3.client('sqs')
        response = sqs_client.receive_message(
            QueueUrl=ENVS.SQS_URL,
            MaxNumberOfMessages=1,
            WaitTimeSeconds=10,
        )

        if 'Messages' in response:
            message = response['Messages'][0]  # Get the first message (if multiple messages are received)

            print("Received Message:")
            print("Message ID:", message['MessageId'])
            print("Receipt Handle:", message['ReceiptHandle'])
            print("Message Body:", message['Body'])

            # Now you can delete the message from the queue
            delete_response = sqs_client.delete_message(
                QueueUrl=ENVS.SQS_URL,
                ReceiptHandle=message['ReceiptHandle']
            )
            print("Message deleted successfully.")
        else:
            print("No messages in the queue.")