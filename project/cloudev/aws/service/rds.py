from ..aws_client import AWSClient
from botocore.exceptions import ClientError

class RDS(AWSClient):
    service_name = 'rds'

    def __init__(self, region_name, service_name='rds', iam_role_arn=None, aws_access_key_id=None, aws_secret_access_key=None, profile_name=None):
        super().__init__(RDS.service_name, region_name, iam_role_arn, aws_access_key_id, aws_secret_access_key, profile_name)


    def start_db_instance(self, db_instance_identifier):
        try:
            response = self.client.start_db_instance(
                DBInstanceIdentifier=db_instance_identifier
            )
            print(f"Starting RDS instance {db_instance_identifier}")
            return response
        except ClientError as e:
            print(f"Failed to start RDS instance {db_instance_identifier}: {str(e)}")
            return None
        except Exception as e:
            return None

    def stop_db_instance(self, db_instance_identifier):
        try:
            response = self.client.stop_db_instance(
                DBInstanceIdentifier=db_instance_identifier
            )
            print(f"Stopping RDS instance {db_instance_identifier}")
            return response
        except ClientError as e:
            print(f"Failed to stop RDS instance {db_instance_identifier}: {str(e)}")
            return None
        except Exception as e:
            return None

    def describe_db_instances(self, filters=None):
        db_instances = []
        next_token = None

        while True:
            response = self.client.describe_db_instances(
                Filters=filters,
                MaxRecords=100,  # 한 번에 반환할 최대 레코드 수
                Marker=next_token
            )

            for db_instance in response['DBInstances']:
                # Cluster에 포함된 리더 인스턴스와 라이터 인스턴스 제외
                if db_instance['Engine'] not in ['aurora', 'aurora-mysql', 'aurora-postgresql']:
                    db_instances.append({
                        'DBInstanceIdentifier': db_instance['DBInstanceIdentifier'],
                        'DBInstanceStatus': db_instance['DBInstanceStatus'],
                        # 필요한 다른 정보 추가
                    })

            next_token = response.get('Marker')

            if not next_token:
                break

        return db_instances
