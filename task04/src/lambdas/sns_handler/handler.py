from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger('SnsHandler-handler')


class SnsHandler(AbstractLambda):

    def validate_request(self, event) -> dict:
        # Assuming the validation logic will be implemented here
        pass
        
    def handle_request(self, event, context):
        """
        Process the incoming SNS event and log the message content.
        """
        # Log the entire event for debugging purposes
        _LOG.info(f"Received event: {event}")

        # Process each record in the event
        for record in event['Records']:
            sns_message = record['Sns']

            # Extract the message details
            message_body = sns_message['Message']
            message_subject = sns_message.get('Subject', 'No subject')
            message_id = sns_message['MessageId']
            timestamp = sns_message['Timestamp']

            # Log the message details
            _LOG.info(f"Message ID: {message_id}")
            _LOG.info(f"Timestamp: {timestamp}")
            _LOG.info(f"Subject: {message_subject}")
            _LOG.info(f"Message: {message_body}")

        return {
            'statusCode': 200,
            'body': 'Processed SNS messages successfully'
        }

HANDLER = SnsHandler()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
