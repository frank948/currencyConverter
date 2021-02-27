import tkinter as tk
from currencyConverterClass import currency_convert

convert = currency_convert('EUR', 'USD')
print(convert.base, convert.quote)