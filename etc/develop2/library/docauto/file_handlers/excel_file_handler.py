from .file_handler_interface import FileHandlerInterface
from ..utils.pandas_utils import read_excel, write_excel

class ExcelFileHandler(FileHandlerInterface):
    def read_file(self, file_path):
        return read_excel(file_path)
    
    def write_file(self, data, file_path):
        write_excel(data, file_path)