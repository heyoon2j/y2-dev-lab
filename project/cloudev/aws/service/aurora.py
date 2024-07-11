from ..aws_client import AWSClient
from botocore.exceptions import ClientError

class Aurora(AWSClient):
    service_name = 'rds'

    def __init__(self, region_name, iam_role_arn=None, aws_access_key_id=None, aws_secret_access_key=None, profile_name=None):
        super().__init__(Aurora.service_name ,region_name, iam_role_arn, aws_access_key_id, aws_secret_access_key, profile_name)

    def start_db_cluster(self, cluster_id):
        try:
            self.client.start_db_cluster(DBClusterIdentifier=cluster_id)
            print(f"Aurora 데이터베이스 클러스터 {cluster_id}를 시작합니다.")
        except ClientError as e:
            print(f"Failed to stop RDS instance {cluster_id}: {str(e)}")
            return None
        except Exception as e:
            return None

    def stop_db_cluster(self, cluster_id):
        try:
            self.client.stop_db_cluster(DBClusterIdentifier=cluster_id)
            print(f"Aurora 데이터베이스 클러스터 {cluster_id}를 중지합니다.")
        except ClientError as e:
            print(f"Failed to stop RDS instance {cluster_id}: {str(e)}")
            return None
        except Exception as e:
            return None


    def describe_db_clusters(self, filters=None):
        clusters = []
        next_token = None

        while True:
            response = self.client.describe_db_clusters(
                Filters=filters,
                MaxRecords=100,  # 한 번에 반환할 최대 레코드 수
                Marker=next_token
            )

            for cluster in response['DBClusters']:
                clusters.append({
                    'DBClusterIdentifier': cluster['DBClusterIdentifier'],
                    'Status': cluster['Status']
                    # 필요한 다른 정보 추가
                })

            next_token = response.get('Marker')

            if not next_token:
                break

        return clusters