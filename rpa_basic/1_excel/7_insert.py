from openpyxl import load_workbook

wb = load_workbook("sample.xlsx")
ws = wb.active

#ws.insert_rows(8) # 8번째 행에 삽입
#ws.insert_rows(8,5) # 8번째 행에 5개줄 삽입
#wb.save("sample_insert_rows.xlsx")

#ws.insert_cols(2)   # B번째 열이 비워짐
ws.insert_cols(2,3)   # B번째 열이 줄이 비워짐
wb.save("sample_insert_cols.xlsx")
