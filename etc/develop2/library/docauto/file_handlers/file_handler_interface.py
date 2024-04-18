from abc import ABC, abstractmethod

class FileHandlerInterface(ABC):
    @abstractmethod
    def read_file(self, file_path):
        pass
    
    @abstractmethod
    def write_file(self, data, file_path):
        pass