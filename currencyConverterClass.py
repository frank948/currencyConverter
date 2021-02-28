from tkinter import *
import urllib.request
import json
import datetime as DT
from datetime import date
import re
import os

window = Tk()
window.title('Currency Conversions')
main_w = Frame(window, width=10, height=10)

main_w.grid(column=0, row=0, sticky='nsew')
main_w.columnconfigure(0, weight=1)
main_w.rowconfigure(0, weight=1)

today = DT.date.today()
weekago = today - DT.timedelta(days=7)
location = os.getcwd()
print(location)

currencies = []

base = StringVar()
base.set(currencies[0])
base_options = OptionMenu(window, base, *currencies).grid(column=1, row=1, sticky='nw')

quote = StringVar()
quote.set(currencies[2])
quote_options = OptionMenu(window, quote, *currencies).grid(column=2, row=1, sticky='nw')

base_out = StringVar()
base_out.set('Base1')
quote_out = StringVar()
quote_out.set('Quote1')

rate = StringVar()
rate.set('https://api.exchangeratesapi.io/history?start_at={}&end_at={}&symbols={}&base={}'.format(weekago,today,base.get(), quote.get(),base.get()))

#update_base = Label(window, textvariable=base_out).grid(column=3, row=1, sticky='nw')
#update_quote = Label(window, textvariable=quote_out).grid(column=4,row=1,sticky='nw')
update_rate = Label(window, textvariable=rate).grid(column=3,row=1,sticky='ne')

def get_rate():
    link = rate.get()
    print(link)
    link_open = urllib.request.urlopen(link)
    for line in link_open:
        d_line = line.decode()
        x = re.search('[0-9]+[.]\d+', d_line)
        rate.set(x.group())

    def get_quote(*args):
        quote_out.set(quote.get())

    def set_rate(*args):
        today = DT.date.today()
        weekago = today - DT.timedelta(days=7)
        rate.set('https://api.exchangeratesapi.io/history?start_at={}&end_at={}&symbols={}&base={}'.format(weekago,today,quote.get(), base.get()))
        link = rate.get()
        print(link)
        link_open = urllib.request.urlopen(link)
        for line in link_open:
            d_line = line.decode()
            x = re.search('[0-9]+[.]\d+', d_line)
            rate.set(x.group())





    quote.trace('w',set_rate)
    base.trace('w', set_rate)
    #base.trace('w', get_base)
    quote.trace('w',get_quote)

get_rate()





window.mainloop()
