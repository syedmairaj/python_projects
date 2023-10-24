from forex_python.converter import CurrencyRates

c = CurrencyRates()

def currency_converter(amount, from_currency, to_currency):
    try:
        exchange_rate = c.get_rate(from_currency, to_currency)
        converted_amount = amount * exchange_rate
        converted_amount = round(converted_amount, 2)
        return converted_amount, from_currency, to_currency
    except ValueError:
        return "Invalid currency code or conversion not possible."

amount = float(input("Enter the amount: "))
from_currency = input("From Currency (e.g., USD): ").upper()
to_currency = input("To Currency (e.g., EUR): ").upper()

result = currency_converter(amount, from_currency, to_currency)

if isinstance(result, tuple):
    converted_amount, from_currency, to_currency = result
    print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
else:
    print(result)
