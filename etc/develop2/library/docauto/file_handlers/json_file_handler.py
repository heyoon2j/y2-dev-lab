from .file_handler_interface import FileHandlerInterface
from ..utils.pandas_utils import read_json, write_json

class JsonFileHandler(FileHandlerInterface):
    def read_file(self, file_path):
        return read_json(file_path)
    
    def write_file(self, data, file_path):
        write_json(data, file_path)
