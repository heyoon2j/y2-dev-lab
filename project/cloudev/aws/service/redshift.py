from ..aws_client import AWSClient

class Redshift(AWSClient):
    service_name = 'redshift'

    def __init__(self, region_name=None, iam_role_arn=None, aws_access_key_id=None, aws_secret_access_key=None, aws_session_token=None, profile_name=None, default=None):
        super().__init__(Redshift.service_name ,region_name=region_name, iam_role_arn=iam_role_arn, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, aws_session_token=aws_session_token, profile_name=profile_name, default=default)

    def start_instance(self, cluster_identifier):
        self.client.resume_cluster(ClusterIdentifier=cluster_identifier)
        print(f"Redshift 클러스터 {cluster_identifier}를 시작합니다.")

    def stop_instance(self, cluster_identifier):
        self.client.pause_cluster(ClusterIdentifier=cluster_identifier)
        print(f"Redshift 클러스터 {cluster_identifier}를 일시 중지합니다.")