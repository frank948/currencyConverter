from tkinter import *
import urllib.request
import json

window = Tk()
window.title('Currency Conversions')
main_w = Frame(window, width=10, height=10)

main_w.grid(column=0, row=0, sticky='nsew')
main_w.columnconfigure(0, weight=1)
main_w.rowconfigure(0, weight=1)

currencies = [
    'USD',
    'EUR',
    'CAD'
]

base = StringVar()
base.set(currencies[0])
base_options = OptionMenu(window, base, *currencies).grid(column=1, row=1, sticky='nw')

quote = StringVar()
quote.set(currencies[1])
quote_options = OptionMenu(window, quote, *currencies).grid(column=2, row=1, sticky='nw')

base_out = StringVar()
base_out.set('Base1')
quote_out = StringVar()
quote_out.set('Quote1')

rate = StringVar()
rate.set('https://api.exchangeratesapi.io/history?start_at=2018-01-01&end_at=2018-09-01&symbols={},{} HTTP/1.1'.format(base.get(), quote.get()))

update_base = Label(window, textvariable=base_out).grid(column=3, row=1, sticky='nw')
update_quote = Label(window, textvariable=quote_out).grid(column=4,row=1,sticky='nw')
update_rate = Label(window, textvariable=rate).grid(column=5,row=2,sticky='ne')

def get_base(*args):
    base_out.set(base.get())

def get_quote(*args):
    quote_out.set(quote.get())

def set_rate(*args):
    rate.set('https://api.exchangeratesapi.io/history?start_at=2018-01-01&end_at=2018-09-01&symbols={},{} HTTP/1.1'.format(base.get(), quote.get()))


quote.trace('w',set_rate)
base.trace('w', set_rate)
base.trace('w', get_base)
quote.trace('w',get_quote)


window.mainloop()
