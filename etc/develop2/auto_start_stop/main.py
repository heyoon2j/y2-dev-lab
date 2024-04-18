class 

####################
# Cron 형태로 동작
# 1) cron_start
# 2) cron_stop
# 3) 예외 처리

# Default
# 1) 공유일 시 Start/Stop는 제외

######################### Cron 동작 #####################################




########################### Pause ######################################
response = client.pause_cluster(
    ClusterIdentifier='string'
)



########################### Resume ######################################
response = client.resume_cluster(
    ClusterIdentifier='string'
)



########################### Describe ######################################
response = client.describe_clusters(
    ClusterIdentifier='string',
    MaxRecords=123,
    Marker='string',
    TagKeys=[
        'string',
    ],
    TagValues=[
        'string',
    ]
)