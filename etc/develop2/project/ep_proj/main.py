from file_handlers.excel_file_handler import ExcelFileHandler
from file_handlers.json_file_handler import JsonFileHandler

def main():
    # Excel 파일 처리
    excel_handler = ExcelFileHandler()
    excel_data = excel_handler.read_file("example.xlsx")
    if excel_data is not None:
        # 데이터 조작 및 처리
        # 여기에 필요한 작업을 수행하세요.
        excel_handler.write_file(excel_data, "output.xlsx")

    # JSON 파일 처리
    json_handler = JsonFileHandler()
    json_data = json_handler.read_file("example.json")
    if json_data is not None:
        # 데이터 조작 및 처리
        # 여기에 필요한 작업을 수행하세요.
        json_handler.write_file(json_data, "output.json")

if __name__ == "__main__":
    main()