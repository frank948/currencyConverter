from tkinter import *
import urllib.request
import json
import datetime as DT
from datetime import date
import re
import os
import requests


window = Tk()
window.title('Currency Conversions')

main_w = Frame(window)

main_w.grid(column=0, row=0, sticky='nsew')
main_w.columnconfigure(0, weight=1)
main_w.rowconfigure(0, weight=1)

today = DT.date.today()
week_ago = today - DT.timedelta(days=7)

currencies = []
symbols = open('symbols.txt', 'r')
for line in symbols:
    x = re.findall('[A-Z]+', line)
    currencies = x
    currencies.sort()

base = StringVar()
base.set('Base')
base_options = OptionMenu(main_w, base, *currencies).grid(column=1, row=1, sticky='w')


quote = StringVar()
quote.set('Quote')
quote_options = OptionMenu(main_w, quote, *currencies).grid(column=2, row=1, sticky='sw')

base_out = StringVar()
base_out.set('Base1')
quote_out = StringVar()
quote_out.set('Quote1')

rate = StringVar()
rate.set('Exchange Rate')
#rate.set('https://api.exchangeratesapi.io/history?start_at={}&end_at={}&symbols={}&base={}'.format(weekago,today,base.get(), quote.get(),base.get()))

#update_base = Label(main_w, textvariable=base_out).grid(column=3, row=1, sticky='nw')
#update_quote = Label(window, textvariable=quote_out).grid(column=4,row=1,sticky='nw')
update_rate = Label(main_w, textvariable=rate).grid(column=3,row=1,sticky='s')



def get_rate():

    def set_rate_quote(*args):
        if base.get() == 'Base':
            quote_out.set(quote.get())
        else:
            today = DT.date.today()
            week_ago = today - DT.timedelta(days=7)
            rate.set(
                'https://api.exchangeratesapi.io/history?start_at={}&end_at={}&symbols={}&base={}'.format(week_ago, today,
                                                                                                          quote.get(),
                                                                                                          base.get()))
            link = rate.get()
            link_open = requests.get(link)
            for line in link_open:
                d_line = line.decode()
                x = re.search('[0-9]+[.]\d+', d_line)
                rate.set(x.group())

    def set_rate_base(*args):
        if quote.get() == 'Quote':
            base_out.set(base.get())
        else:
            today = DT.date.today()
            week_ago = today - DT.timedelta(days=7)
            rate.set(
                'https://api.exchangeratesapi.io/history?start_at={}&end_at={}&symbols={}&base={}'.format(week_ago, today,
                                                                                                          quote.get(),
                                                                                                          base.get()))
            link = rate.get()
            link_open = requests.get(link)
            for line in link_open:
                d_line = line.decode()
                x = re.search('[0-9]+[.]\d+', d_line)
                rate.set(x.group())

    quote.trace('w',set_rate_quote)
    base.trace('w', set_rate_base)

get_rate()
window.mainloop()
