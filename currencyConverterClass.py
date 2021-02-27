from tkinter import *
import urllib.request
import json

window = Tk()
window.title('Currency Conversions')
main_w = Frame(window, width=10, height=10)

main_w.grid(column=0, row=0, sticky='nsew')
main_w.columnconfigure(0, weight=1)
main_w.rowconfigure(0, weight=1)

currencies = []

base = Label(window, text='Base').grid(column=1,row=0,sticky='nw')
quote = Label(window, text='Quote').grid(column=2,row=0,sticky='nw')
exchange_rate = Label(window, text='Rate').grid(column=3,row=0,sticky='nw')

base_ = StringVar()
quote_ = StringVar()
rate_ = StringVar()
base_.set(currencies[0])
quote_.set(currencies[0])
base_options = OptionMenu(window, base_, *currencies).grid(column=1,row=1,sticky='nw')
quote_options = OptionMenu(window, quote_, *currencies).grid(column=2,row=1,sticky='nw')
rate = Entry(window).grid(column=3,row=1)


window.mainloop()