import gspread
from oauth2client.service_account import ServiceAccountCredentials

def fetch_rows_from_sheet(sheet_id, json_keyfile, sheet_gid):
    # Setup Google Sheets access
    scope = ['https://www.googleapis.com/auth/spreadsheets.readonly', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(json_keyfile, scope)
    client = gspread.authorize(credentials)
    spreadsheet = client.open_by_key(sheet_id)  # Open the spreadsheet by its ID

    # Find the worksheet with the specified gid
    sheet = None
    for worksheet in spreadsheet.worksheets():
        if worksheet.id == sheet_gid:
            sheet = worksheet
            break

    if sheet is None:
        raise ValueError(f"No sheet found with gid: {sheet_gid}")

    # Fetch values from column B (1-based index: B=2)
    column_b_values = sheet.col_values(2)  # Get all values from column B

    # Extract the first 9 values
    data = column_b_values[:9]  # Adjust slice if fewer than 9 rows
    print(data)
    return data
