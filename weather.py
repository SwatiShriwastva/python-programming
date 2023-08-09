from tkinter import *
from tkinter import ttk
import requests

def data_get():
   city=city_name.get()
   data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=20ff644bac1475359cc963e3ace58594").json()
   w_label1.config(text=data["weather"][0]["main"])
   wd_label1.config(text=data["weather"][0]["description"])
   temp_label1.config(text=int(data["main"]["temp"]-273.15))
   per_label1.config(text=data["main"]["pressure"])

win = Tk()
win.title("Swati Weather App")
win.config(bg="grey")
win.geometry("490x570")
win.resizable(False,False)
   
name_label =Label(win,text="Swati Weather App",font=("Time New Roman",30))
name_label.place(x=25,y=50,height=50,width=450)

city_name = StringVar()

list_name=["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com=ttk.Combobox(win,text="swati weather app",values=list_name,font=("Time New Roman",15),textvariable=city_name)

com.place(x=25,y=120,height=50,width=450)

w_label=Label(win,text=" Weather Climate",font=("Time New Roman",15))
w_label.place(x=25,y=260,height=50,width=210)

w_label1 = Label(win,text="",font=("Time New Roman",15))
w_label1.place(x=250,y=260,height=50,width=210)

wd_label = Label(win,text="Weather Description",font=("Time New Roman",15))
wd_label.place(x=25,y=330,height=50,width=210)

wd_label1 = Label(win,text="",font=("Time New Roman",15))
wd_label1.place(x=250,y=330,height=50,width=210)

temp_label = Label(win,text="Temperature (in °C)",font=("Time New Roman",15))
temp_label.place(x=25,y=400,height=50,width=210)

temp_label1 = Label(win,text="",font=("Time New Roman",15))
temp_label1.place(x=250,y=400,height=50,width=210)

per_label = Label(win,text="Pressure (in Pa)",font=("Time New Roman",15))
per_label.place(x=25,y=470,height=50,width=210)

per_label1 = Label(win,text="",font=("Time New Roman",15))
per_label1.place(x=250,y=470,height=50,width=210)

done_button = Button(win,text="Submit",font=("Time New Roman",15,"bold"),command=data_get)
done_button.place(y=190,height=50,width=110,x=200)
   
win.mainloop()