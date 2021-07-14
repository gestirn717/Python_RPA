from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# ws.insert_rows(8) #8번째 줄이 비워짐(행 추가)
# ws.insert_rows(8,5) #8번째줄부터 5줄 행 추가

ws.insert_cols(2) #B번째 열이 비워짐(열 추가)
ws.insert_cols(2,3) #B번째 열부터 3열 추가 


# wb.save("sample_insert_rows.xlsx")
wb.save("sample_insert_cols.xlsx")