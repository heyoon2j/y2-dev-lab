from ..aws_client import AWSClient

class Aurora(AWSClient):
    service_name = 'rds'

    def __init__(self, region_name, iam_role_arn=None, aws_access_key_id=None, aws_secret_access_key=None, profile_name=None):
        super().__init__(Aurora.service_name ,region_name, iam_role_arn, aws_access_key_id, aws_secret_access_key, profile_name)

    def start_cluster(self, cluster_id):
        self.client.start_db_cluster(DBClusterIdentifier=cluster_id)
        print(f"Aurora 데이터베이스 클러스터 {cluster_id}를 시작합니다.")

    def stop_cluster(self, cluster_id):
        self.client.stop_db_cluster(DBClusterIdentifier=cluster_id)
        print(f"Aurora 데이터베이스 클러스터 {cluster_id}를 중지합니다.")