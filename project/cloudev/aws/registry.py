from typing import Dict, Tuple


ServiceDict = Dict[str, Tuple[str, ...]]

COMPUTING_SERVICES : ServiceDict = {
    "ec2": ("EC2",),
    "rds": ("RDS",),
    "aurora": ("Aurora",)
}

NETWORK_SERVICES : ServiceDict = {
    "vpc": ("VPC",),
    "network_firewall": ("NetworkFirewall",),
    "tgw": ("TGW", "TransitGateway")
}

STORAGE_SERVICES : ServiceDict = {
    "s3": ("S3", "ObjectStorage"),
    "efs": ("EFS", "FileStorage")
}

SERVICES : ServiceDict = {
    "ec2": ("EC2",),
    "rds": ("RDS",),
    "aurora": ("Aurora",),
    "s3": ("S3", "ObjectStorage"),
    "efs": ("EFS", "FileStorage"),
    "vpc": ("VPC",),
    "network_firewall": ("NetworkFirewall",),
    "tgw": ("TGW", "TransitGateway")    
}