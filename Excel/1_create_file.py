from openpyxl import Workbook
wb = Workbook() #새 워크북 생성
ws = wb.active #활성화된 sheet 가져옴
ws.title = "mergisheet" #sheet 이름을 변경
wb.save("sample.xlsx") #파일 저장
wb.close() #파일 닫기
 