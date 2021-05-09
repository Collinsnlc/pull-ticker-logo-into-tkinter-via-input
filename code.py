import yfinance as yf
from tkinter import *
from PIL import Image, ImageTk
import urllib.request
import io

root = Tk()
ticker_symbol = input("enter ticker symbol: ")
ticker_data = yf.Ticker(ticker_symbol)

show = Label(root)
show.pack()
img_url = ticker_data.info['logo_url']
with urllib.request.urlopen(img_url) as url:
    temp_file = io.BytesIO(url.read())
img = Image.open(temp_file)
tkimg = ImageTk.PhotoImage(image=img)
show.config(image=tkimg)




root.mainloop()
