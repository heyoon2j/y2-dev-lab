from ..aws_client import AWSClient

class EC2(AWSClient):
    service_name = 'ec2'

    def __init__(self, region_name=None, iam_role_arn=None, aws_access_key_id=None, aws_secret_access_key=None, profile_name=None):
        super().__init__(EC2.service_name, region_name, iam_role_arn, aws_access_key_id, aws_secret_access_key, profile_name)

    def start_instance(self, instance_id):
        self.client.start_instances(InstanceIds=[instance_id])
        print(f"EC2 인스턴스 {instance_id}를 시작합니다.")

    def stop_instance(self, instance_id):
        self.client.stop_instances(InstanceIds=[instance_id])
        print(f"EC2 인스턴스 {instance_id}를 중지합니다.")


test = 