import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open ("Teste").sheet1

data = sheet.get_all_records()

row = sheet.row_values(3)
col = sheet.col_values(3)
cell = sheet.cell(1,2).value
sheet.delete_row(7)
sheet.update_cell (5,3,50)