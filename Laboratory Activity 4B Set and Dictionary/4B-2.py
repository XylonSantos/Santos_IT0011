import csv

def load_currency_data(filename):
    currency_data = {}
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            currency_data[row['code']] = float(row['rate'])
    return currency_data

def convert_currency(amount, currency_code, currency_data):
    if currency_code in currency_data:
        rate = currency_data[currency_code]
        return amount * rate
    else:
        return None

def main():

    currency_data = load_currency_data('currency.csv')

    amount_usd = float(input("How much dollar do you have? "))

    currency_code = input("What currency you want to have? ").strip().upper()

    converted_amount = convert_currency(amount_usd, currency_code, currency_data)

    print(f"Dollar: {amount_usd} USD")
    if converted_amount is not None:
        print(f"{currency_code}: {converted_amount}")
    else:
        print("Currency code not found.")

if __name__ == "__main__":
    main()