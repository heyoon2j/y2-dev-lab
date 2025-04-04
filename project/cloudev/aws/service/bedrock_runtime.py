from ..aws_client import AWSClient
from botocore.exceptions import ClientError

class BedrockRuntime(AWSClient):
    service_name = 'bedrock-runtime'

    def __init__(self, region_name=None, iam_role_arn=None, aws_access_key_id=None, aws_secret_access_key=None, aws_session_token=None, profile_name=None, default=None):
        super().__init__(BedrockRuntime.service_name ,region_name=region_name, iam_role_arn=iam_role_arn, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, aws_session_token=aws_session_token, profile_name=profile_name, default=default)


    def start_instances(self, instance_ids):
        # Argument set
        id_list = None
        if type(instance_ids) != list:
            id_list = [instance_ids]
        else:
            id_list = instance_ids


