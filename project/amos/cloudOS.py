import utils 

class CloudOS:

    def __init__(self, os_type=None, os_major_version=None, cpu_arch=None, conf_directory=None):
        self.os_type            = os_type
        self.os_major_version   = os_major_version
        self.cpu_arch           = cpu_arch
        self.conf_directory     = conf_directory


            
    def set_repository(self):
        pass


class Rocky(CloudOS):
    def __init__(self):
        super().__init__(os_type="rocky", os_major_version=8)

    def set_repository(self):
        super().set_repository()
        if self.os_major_version == 8 or self.os_major_version == 9:
            script = f"cat {self.conf_directory}/conf/repo/rocky-infra.repo > /etc/yum.repos.d/rocky-infra.repo"
        else:
            return False

        utils.subprocess(script)
        return True



class Ubuntu(CloudOS):
    def __init__(self):
        super().__init__()

    def set_repository(self):
        super().set_repository()
        if self.os_major_version == 20 or self.os_major_version == 22:
            script = f"cat {self.conf_directory}/conf/repo/u{self.os_major_version}_source_{self.arch}.list > /etc/apt/sources.list"
        else:
            print()
            return False
        
        utils.subprocess(script)
        return True
