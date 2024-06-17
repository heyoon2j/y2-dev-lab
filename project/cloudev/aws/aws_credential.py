import boto3

class AWSCredential:
    @staticmethod
    def get_iam_credentials(iam_role_arn):
        # IAM 역할을 이용하여 임시 자격 증명 얻기
        sts_client = boto3.client('sts')
        response = sts_client.assume_role(
            RoleArn=iam_role_arn,
            RoleSessionName='session'
        )

        # 임시 자격 증명 얻기
        credentials = response['Credentials']
        return {
            'aws_access_key_id': credentials['AccessKeyId'],
            'aws_secret_access_key': credentials['SecretAccessKey'],
            'aws_session_token': credentials['SessionToken']
        }

    @staticmethod
    def get_static_credentials(aws_access_key_id, aws_secret_access_key):
        return {
            'aws_access_key_id': aws_access_key_id,
            'aws_secret_access_key': aws_secret_access_key
        }

    @staticmethod
    def get_profile_credentials(profile_name):
        session = boto3.Session(profile_name=profile_name)
        return {
            'aws_access_key_id': session.get_credentials().access_key,
            'aws_secret_access_key': session.get_credentials().secret_key,
            'aws_session_token': session.get_credentials().token
        }