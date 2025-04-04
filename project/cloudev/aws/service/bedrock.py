from ..aws_client import AWSClient
from botocore.exceptions import ClientError

class Bedrock(AWSClient):
    service_name = 'bedrock'

    def __init__(self, region_name=None, iam_role_arn=None, aws_access_key_id=None, aws_secret_access_key=None, aws_session_token=None, profile_name=None, default=None):
        super().__init__(Bedrock.service_name ,region_name=region_name, iam_role_arn=iam_role_arn, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, aws_session_token=aws_session_token, profile_name=profile_name, default=default)


    def start_instances(self, instance_ids):
        # Argument set
        id_list = None
        if type(instance_ids) != list:
            id_list = [instance_ids]
        else:
            id_list = instance_ids

        # Action
        try: 
            self.client.start_instances(InstanceIds=id_list)
            print(f"EC2 인스턴스 {instance_ids}를 시작합니다.")
        except ClientError as e:
            print(f"Error with starting instance {instance_ids}: {e}")            


    def stop_instances(self, instance_ids):
        # Argument set
        id_list = None
        if type(instance_ids) != list:
            id_list = [instance_ids]
        else:
            id_list = instance_ids

        # Action
        try: 
            self.client.stop_instances(InstanceIds=id_list)
            print(f"EC2 인스턴스 {instance_ids}를 종료합니다.")
        except ClientError as e:
            print(f"Error with stopping instance {instance_ids}: {e}")    


    def describe_instances(self, filters=None):
        # Argument set
        if not filters:
            filters = [
                {
                    'Name': 'instance-state-name',
                    'Values': ['running', 'stopping', 'stopped']
                }
            ]

        # Action
        instances = []
        next_token = None

        while True:
            if next_token:
                response = self.client.describe_instances(
                    Filters=filters,
                    NextToken=next_token
                )
            else:
                response = self.client.describe_instances(
                    Filters=filters
                )

            for reservation in response['Reservations']:
                for instance in reservation['Instances']:
                    # instances.append({
                    #     'InstanceId': instance['InstanceId'],
                    #     'State': instance['State']['Name']
                    # })
                    instances.append(instance)
            # 다음 페이지가 있는지 확인
            next_token = response.get('NextToken')

            if not next_token:
                break

        return instances
