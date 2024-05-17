import json
import boto3

from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger('SqsHandler-handler')


class SqsHandler(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):
        """
        Explain incoming event here
        """
        # todo implement business logic
        # return 200
        _LOG.info(f"Received event: {json.dumps(event)}")
        # Process each record in the event
        for record in event['Records']:
            # Each record represents one SQS message
            message_body = record['body']

            # Log the message body
            _LOG.info(f"Message body: {message_body}")

        return {
            'statusCode': 200,
            'body': json.dumps('Processed messages successfully')
        }
        

HANDLER = SqsHandler()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
