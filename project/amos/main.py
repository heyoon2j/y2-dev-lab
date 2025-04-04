
class CLOUD:
    def __init__(self):
        #self.os_info = 
        pass

class AWS(CLOUD):
    hostDomain = "aws.kpay-in.net"
    



class GCP(CLOUD):
    hostDomain = "gcp.kpay-in.net"


class KC(CLOUD):
    hostDomain = "kc.kpay-in.net"


    def set_provider(self):
        super().set_provider()



    def __init__(self, service_name=None, region_name=None, iam_role_arn=None, aws_access_key_id=None, aws_secret_access_key=None, aws_session_token=None, profile_name=None, default=None):
        self.service_name = service_name
        self.credentials = None
        self.client = None
        self.aws_session_token = None
        #self.region_name = region_name
        
        # 자격 증명 초기화
        # 1) IAM Role 사용하는 경우
        if iam_role_arn:
            self.credentials = AWSCredential.get_iam_credentials(iam_role_arn)
        # 2) 직접 입력하는 경우
        elif aws_access_key_id and aws_secret_access_key:
            self.credentials = AWSCredential.get_static_credentials(aws_access_key_id, aws_secret_access_key)
        # 3) Profile 사용하는 경우
        elif profile_name:
            self.credentials = AWSCredential.get_profile_credentials(profile_name)
        elif default:
            self.credentials = {}
        else:
            raise ValueError("IAM 역할 또는 자격 증명을 제공해야 합니다.")

        self.client = self.create_client(region_name=region_name)
        

    def create_client(self, region_name):#, service_name=None):
        return boto3.client(
            service_name=self.service_name,
            region_name=region_name,
            **self.credentials
        )class AWS(CLOUD):


def update_os_info(key):


def call_cloud_info():
    pass

def call_osdata_info():
    



def set_hostname():
    # print()
    set_provider = instance_provider_result


def call_cloud_info():





def main():
    pass