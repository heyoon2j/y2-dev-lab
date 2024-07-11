
import cloudev
from botocore.exceptions import ClientError
import json

def get_account_ids(client, ou_id=None):
    return client.list_accounts_for_parent(ou_id)


def invoke_lambda(client, function_name, invocation_type, payload):
    return client.invoke(function_name, invocation_type, payload)


def main():
    """
    0) 기본 설정
    """
    iam_role_arn = None
    aws_access_key_id = None
    aws_secret_access_key = None
    profile_name = 'yo_test'
    
    region_name = 'ap-northeast-2'

    ou_id = 'ou-xxxx-xxxxxxxx'
    role_name = 'test'

    lambda_function_name = 'testFunction'
    invocation_type = 'Event' # 'RequestResponse'


    """
    1) OU 목록 가지고오기
    """
    service = getattr(cloudev, 'OU')
    ou_client = service(region_name=region_name, iam_role_arn=iam_role_arn, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, profile_name=profile_name)

    account_ids = get_account_ids(ou_client, ou_id)

    """
    2) 계정별 람다 실행
    """
    service = getattr(cloudev, 'Lambda')

    for account_id in account_ids:
        role_arn = f'arn:aws:iam::{account_id}:role/{role_name}'
        lambda_client = service(iam_role_arn=role_arn)
        payload = {
            "role_arn": role_arn,
        }

        response = invoke_lambda(lambda_client, function_name=lambda_function_name, invocation_type=invocation_type, payload=json.dump(payload))

        # 2-1) 비동기에 대한 처리 확인       
        if not response or response['StatusCode'] != 202:
            print(f"Failed to invoke Lambda function for account {account_id}: Event type")
            """
            SNS 추가
            """
        else:
            print(f"Invoked Lambda function {lambda_function_name} successfully for account {account_id} : Event type")



if __name__ == '__main__':
    main()

