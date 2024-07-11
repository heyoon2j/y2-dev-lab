from ..aws_client import AWSClient
from botocore.exceptions import ClientError

class Organizations(AWSClient):
    service_name = 'organizations'

    def __init__(self, region_name=None, iam_role_arn=None, aws_access_key_id=None, aws_secret_access_key=None, profile_name=None):
        super().__init__(Organizations.service_name, region_name, iam_role_arn, aws_access_key_id, aws_secret_access_key, profile_name)


    def list_accounts_for_parent(self, ou_id=None):
        account_ids = []

        try:
            next_token = None

            while True:
                if next_token:
                    response = self.client.list_accounts_for_parent(ParentId=ou_id, NextToken=next_token)
                else:
                    response = self.client.list_accounts_for_parent(ParentId=ou_id)
                
                for account in response['Accounts']:
                    account_ids.append(account['Id'])
                
                next_token = response.get('NextToken')
                if not next_token:
                    break
            
            print("Successfully get acccount ids")
        except ClientError as e:
            print(f"Error getting account ids : {e}")

        return account_ids
