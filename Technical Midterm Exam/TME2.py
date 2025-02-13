from datetime import datetime

def convert_date_format(date_str):
    date_obj = datetime.strptime(date_str, '%m/%d/%Y')
    return date_obj.strftime('%B %d, %Y')

date_input = input("Enter the date (mm/dd/yyyy): ")
try:
    formatted_date = convert_date_format(date_input)
    print(f"Date Output: {formatted_date}")
except ValueError:
    print("Invalid date format. Please use mm/dd/yyyy.")