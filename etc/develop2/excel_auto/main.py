import pandas as pd
from openpyxl import load_workbook

# 엑셀 파일 읽기
df = pd.read_excel('원본파일.xlsx')

# 데이터프레임에서 작업 수행 (예: 새로운 열 추가)
df['New_Column'] = df['Existing_Column'] * 2

# 수정된 데이터프레임을 엑셀 파일로 저장
with pd.ExcelWriter('수정된파일.xlsx', engine='openpyxl') as writer:
    writer.book = load_workbook('원본파일.xlsx')  # 기존 엑셀 파일을 열고
    writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)  # 기존 시트를 유지하고
    df.to_excel(writer, index=False)  # 수정된 데이터프레임을 새 시트에 쓰기
    writer.save()  # 변경사항 저장
