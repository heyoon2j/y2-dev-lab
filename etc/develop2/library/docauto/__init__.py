from .file_handlers.excel_file_handler import ExcelFileHandler
from .file_handlers.json_file_handler import JsonFileHandler
from .file_handlers.file_handler_interface import FileHandlerInterface

from .utils.pandas_utils import read_excel, write_excel, read_json, write_json


# 버전 정보 포함
__version__ = '1.0.0'

# 다른 패키지 또는 모듈에 대한 alias 지정
pandas_utils = __import__('docauto.utils.pandas_utils')

# 초기화 코드 (예: 패키지 로드 메시지 출력)
print("docauto 패키지가 로드되었습니다.")

# 외부에서 공개할 모듈 지정
__all__ = [
    'ExcelFileHandler',
    'JsonFileHandler',
    'FileHandlerInterface',
    'read_excel',
    'write_excel',
    'read_json',
    'write_json',
    'pandas_utils',
    '__version__'
]