# Argumnet or 환경변수
"""
AWS_SERVICE : EC2, RDS, AURORA, REDSHIFT
COUNTRY : Korea
CURRENT_YEAR : 2024

TOLERANCE : 스케줄링에 대한 시간 오차 범위
TAG : 
- START_TIME : AutoStart
- STOP_TIME : AutoStop
- EXCEPT_PERIOD : Online_period
- 
"""

# Algorithm
"""
* 람다 스케줄 시간은 매 10분간격 기준으로 실행 (미정)
* 람다 정보 확인
    - Timeout 시간 확인 (실행 시간을 위한)
    - 메모리 사이즈 
    - 환경 변수
1) 해당 나라, 해당 년도 휴일 읽어오기 (S3 또는 코드 or 환경변수 상으로)
    => 현재는 환경 변수에 일일히 추가 중
    => 휴일 생성 람다를 통해 S3 또는 환경 변수에 추가 (12월 말 기준 스케줄링) or 해당 람다에서 코드 상으로 가져오기 (방화벽 확인 필요)
    - ex> 20240606

코드짜줘
1) 휴일 가져오기
2) 인스턴스 목록 가지고 오기
3) 인스턴스에 대한 태그를 비교하여 Start/Stop 동작
3-1) 인스턴스 태그 확인 
3-2) 호출한 시간 비교 및 실행
    - SCHEDULE_WORKING == TRUE 인 경우, 제외
    - EXCEPT_PERIOD 인 경우, 제외
    - START_TIME인 경우, 시작
    - STOP_TIME인 경우, 중지
    ====================================================
    - RUN_SCHEDULE : daily / daily_period / nonStop_period / stop_period
    - RUN_SCH_TIMESTAMP
        - 매일 : 10:00_20:00
        - 매일 (일정 기간만 지정): 2024-04-05_2024-04-10#10:00_20:00
        - 일정기간 무중단 : 2024-04-05T10:00_2024-04-10T20:00 => 10일까지 AutoStop/AutoStart 기능 중지. 5일에 Start 실행
        - 일정기간 중단 : 2024-04-05T10:00_2024-04-10T20:00 => 10일까지 AutoStop/AutoStart 기능 중지. 5일에 Stop 실행

4) Error 또는 Excpetion 발생 시, 알람


* 우선 순위
기본 전제: 스케줄링을 거는 이유는 무중단용 서버가 아닌 비용 절약을 위한 서버들을 대상으로 진행. 아닌 경우 태그를 모두 삭제
- PeriodUnInterruption
- PeriodInterruption
- AutoStart/AutoStop : 휴일에는 Start 실행하지 않음.


"""

import cloudev
#import holidays
from datetime import datetime, timedelta



def main():
    """lambda 함수 변경 시
    iam_role_arn = event.get('role_arn')
    aws_access_key_id = None
    aws_secret_access_key = None
    profile_name = None
    region_name = 'ap-northeast-2'
    """
    
    """
    0) 기본 설정 (입력값)
    """
    iam_role_arn = None
    aws_access_key_id = None
    aws_secret_access_key = None
    profile_name = 'yo_test'

    region_name = 'ap-northeast-2'
    #service_name = 'EC2'

    for svc in ['EC2', 'RDS', 'Aurora']:
        handle_schedule(service_name=svc, region_name=region_name, iam_role_arn=iam_role_arn, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, profile_name=profile_name)



def handle_schedule(service_name, region_name, iam_role_arn=None, aws_access_key_id=None, aws_secret_access_key=None, profile_name=None):
    """
    1) 기본 설정
        1-1) 현재 시간 가져오기
        1-2) 휴일 가져오기
        1-3) 사용잘 서비스 자격증명
    """
    # 1-1)
    cur_datetime = datetime.now()

    # 1-2)
    holiday_list = get_holidays()
    
    # 1-3)
    service = getattr(cloudev, service_name)
    service_client = service(region_name=region_name, iam_role_arn=iam_role_arn, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, profile_name=profile_name)
    
    """ 2) 자원 목록 가지고 오기 """ 
    resource_list = get_resource_list(service_name, service_client)

    """ 3) 인스턴스에 대한 태그를 비교하여 Start/Stop 동작 """    
    for resource in resource_list:
        """ 3-1) 인스턴스 태그 확인 """
        tags = get_tags(service_name, resource)

        resource_id = tags[0]
        sch_except = tags[1].get('RUN_SCH_EXCEPT')
        sch_start = tags[1].get('RUN_SCH_START')
        sch_stop = tags[1].get('RUN_SCH_STOP')

        """ 3-2) 호출한 시간 비교 및 실행 """
        print(resource_id, sch_except, sch_start, sch_stop)
        run_schedule(resource_id, service_client.start_instances, service_client.stop_instances, holiday_list, sch_except, sch_start, sch_stop, cur_datetime)


"""
1) 휴일 가져오기
"""
def get_holidays():
    pass
    # kr_holidays = holidays.KR(years=datetime.now().year)
    # return list(kr_holidays.keys())


"""
2) 자원 목록 가지고 오기
"""
def get_resource_list(service_name, service_client):
    if service_name == 'EC2':
        return service_client.describe_instances()
    elif service_name == 'RDS':
        return service_client.describe_db_instances()
    elif service_name == 'Aurora':
        return service_client.describe_db_clusters()


def get_tags(service_name, resource):
    if service_name == 'EC2':
        tags = {}
        resource_id = resource.get('InstanceId')
        for tag in resource.get('Tags',[]):
            tags[tag['Key']] = tag['Value']
    
    elif service_name in ['RDS']:
        tags = {}
        resource_id = resource.get('DBInstanceIdentifier')
        for tag in resource.get('TagList',[]):
            tags[tag['Key']] = tag['Value']
    
    elif service_name in ['Aurora']:
        tags = {}
        resource_id = resource.get('DBClusterIdentifier')
        for tag in resource.get('TagList',[]):
            tags[tag['Key']] = tag['Value']

    return [resource_id, tags]


"""
3) 인스턴스에 대한 태그를 비교하여 Start/Stop 동작
"""
def run_schedule(resource_id, start_func, stop_func, holiday_list, sch_except=None, sch_start=None, sch_stop=None, cur_datetime=None): 
# 3-2) 호출한 시간 비교 
    # - RUN_SCHEDULE : daily / daily_period / nonStop_period / stop_period
    # - RUN_SCH_TIMESTAMP
    #     - 매일 : 10:00_20:00
    #     - 매일 (일정 기간만 지정): 2024-04-05_2024-04-10#10:00_20:00
    #     - 일정기간 무중단 : 2024-04-05T10:00_2024-04-10T20:00 => 10일까지 AutoStop/AutoStart 기능 중지. 5일에 Start 실행
    #     - 일정기간 중단 : 2024-04-05T10:00_2024-04-10T20:00 => 10일까지 AutoStop/AutoStart 기능 중지. 5일에 Stop 실행
        # sch_except = "2024-07-03T08:00_2024-07-12T22:00"
        # holiday = ["2024-07-03", "2024-07-10"]
        # sch_start = "08:00"
        # sch_stop = "20:00"

    #cur_datetime = datetime.now()
    cur_time = cur_datetime.replace(minute=cur_datetime.minute // 10 * 10, second=0, microsecond=0).time()


    # 1) 무중단 일자, 
    if sch_except:
        # Parsing
        start, end = sch_except.split('_')
        start_datetime  = datetime.strptime(start, '%Y-%m-%dT%H:%M')
        end_datetime = datetime.strptime(end, '%Y-%m-%dT%H:%M')

        if start_datetime.date() == cur_datetime.date() and start_datetime.time().hour == cur_time.hour and start_datetime.time().minute:
            start_func(resource_id)
            return
        elif cur_datetime.date() == end_datetime.date() and cur_time.hour == end_datetime.time().hour and cur_time.minute == end_datetime.time().minute:
            stop_func(resource_id)
            return
        else:
            return


    # 2) 휴일이거나 토,일요일인 경우, 종료
    if cur_datetime.date() in holiday_list or cur_datetime.weekday() in [5, 6]:
        return


    # 3) Stop/Start

    start_time = datetime.strptime(sch_start, '%H:%M').time()
    if start_time.hour == cur_time.hour and start_time.minute == cur_time.minute:
        # try:
        start_func(resource_id)
        return
        # except Exception as e:
        #     print("Error starting instance {}: {}".format(instance_id, str(e)))
    
    stop_time = datetime.strptime(sch_stop, '%H:%M').time()
    if stop_time.hour == cur_time.hour and stop_time.minute == cur_time.minute:
        # try:
        stop_func(resource_id)
        return
        # except Exception as e:
        #     print("Error stopping instance {}: {}".format(instance_id, str(e)))
   


if __name__ == '__main__':
    main()