from ..aws_client import AWSClient
from botocore.exceptions import ClientError

class Lambda(AWSClient):
    service_name = 'lambda'

    def __init__(self, region_name=None, iam_role_arn=None, aws_access_key_id=None, aws_secret_access_key=None, aws_session_token=None, profile_name=None, default=None):
        super().__init__(Lambda.service_name ,region_name=region_name, iam_role_arn=iam_role_arn, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, aws_session_token=aws_session_token, profile_name=profile_name, default=default)


    def invoke(self, function_name, invocation_type, payload):
        try:
            response = self.client.invoke(
                FunctionName=function_name,
                InvocationType=invocation_type,
                Payload=payload
            )
            print(f"Invoked Lambda function {function_name}")
            return response

        except ClientError as e:
            print(f"Error invoking Lambda function {function_name}: {e}")
            return None
