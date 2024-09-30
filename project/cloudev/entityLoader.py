import importlib
from typing import Dict, Tuple

from .aws.registry import SERVICES as AWS_SERVICES
from .azure.registry import SERVICES as AZURE_SERVICES
from .kubernetes.registry import SERVICES as K8S_SERVICES

"""
ServiceDict = Dict[str, Tuple[str, ...]]

COMPUTING_SERVICES : ServiceDict = {
    "ec2": ("EC2"),
    "rds": ("RDS"),
    "aurora": ("Aurora"),
}

NETWORK_SERVICES : ServiceDict = {
    "vpc": ("VPC"),
    "network_firewall": ("NetworkFirewall"),
    "tgw": ("TGW", "TransitGateway")
}

STORAGE_SERVICES : ServiceDict = {
    "s3": ("S3", "ObjectStorage"),
    "efs": ("EFS", "FileStorage"),
}
"""

class EntityLoader:
    def __init__(self, path: str, *args, **kwargs) -> None:
        """
        entity : Class (== One of module attributes)
        module_name : Module name
        entity_name : Class name in module
        """
        entity_path = path.split(".")
        self.entity = None 
        self.module_name = ".".join(entity_path[0:-1])
        self.entity_name = entity_path[-1]

    def __call__(self, *args, **kwargs):
        """
        Create instance of class
        """
        cls = self.get_entity()        
        return cls(*args, **kwargs)

    def __getattr__(self, __name: str):
        pass


    def get_entity(self):
        # Get Module information
        if self.entity is None:
            self.entity = getattr(importlib.import_module(self.module_name), self.entity_name)
        return self.entity


    @staticmethod
    def load(prefix: str, scope: dict):
        """
        Load service entities.
        
        ex>
        scope {
            'entity1' : EntityLoader('prifix.module.entity1'),
            'entity2' : EntityLoader('prifix.module.entity2')
        }
        """

        entity_mapping = None
        if prefix == 'aws':
            entity_mapping = AWS_SERVICES
        elif prefix == 'azure':
            entity_mapping = AZURE_SERVICES
        elif prefix == 'k8s':
            entity_mapping = K8S_SERVICES
        else:
            # raise 
            print("This is not the correct category.")
            return ValueError


        for module, entities in entity_mapping.items():
            for entity in entities:
                scope.update(
                    {    
                        entity: EntityLoader(f"cloudev.{prefix}.service.{module}.{entity}")
                    }
                )
