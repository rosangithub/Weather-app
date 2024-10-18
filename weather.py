#requirement geopy library 
#timezonefinder 
#pytz
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
root=Tk()
root.title("Weather app")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getWeather():
    try:
        city=textfield.get()
        geolocator=Nominatim(user_agent="geopiExercies")
        location=geolocator.geocode(city)
        obj=TimezoneFinder()
        result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
    
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%p")
        clock.config(text=current_time)
        name.config(text="CURRENT_WEATHER")

        #weather
    # https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=28861aee35882000a38fd212c31d8637"
        json_data=requests.get(api).json()
        condition=json_data['weather'][0]['main']
        description=json_data['weather'][0]['description']
        temp=int(json_data['main']['temp']-273.15)
        pressure=json_data['main']['pressure']
        humidity=json_data['main']['humidity']
        wind=json_data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry!!")

#28861aee35882000a38fd212c31d8637

#search box
Search_image=PhotoImage(file="searchbox.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)
textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25 ,"bold"),bg="#404040",fg="white",border=0)
textfield.place(x=50,y=40)
textfield.focus()

search_icon=PhotoImage(file="search_icon.png")
myimage_icon=Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=400,y=32)

#logo
logo_img=PhotoImage(file="logo.png")
logo=Label(image=logo_img)
logo.place(x=150 ,y=100)

#buttom box
frame_img=PhotoImage(file="box.png")
my_frame_img=Label(image=frame_img)
my_frame_img.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=('arial',15,'bold'))
name.place(x=30,y=100)
clock=Label(root,font=('Helvetica',20))
clock.place(x=30,y=130)

#label
label1=Label(root,text="WIND",font=("Helvetica",15,"bold"),fg="black",bg="#1ab5ef")
label1.place(x=100,y=400)

label2=Label(root,text="HUMIDITY",font=("Helvetica",15,"bold"),fg="black",bg="#1ab5ef")
label2.place(x=260,y=400)

label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,"bold"),fg="black",bg="#1ab5ef")
label3.place(x=450,y=400)

label4=Label(root,text="PRESSURE",font=("Helvetica",15,"bold"),fg="black",bg="#1ab5ef")
label4.place(x=670,y=400)
t=Label(font=("arial",70,'bold'),fg='#ee666d')
t.place(x=400,y=150)
c=Label(font=("arial",15,'bold'))
c.place(x=400,y=250)

w=Label(text="....",font=("arial",20,'bold'),bg="#1ab5ef")
w.place(x=107,y=440)

h=Label(text='....',font=("arial",20,'bold'),bg='#1ab5ef')
h.place(x=280,y=440)

d=Label(text='....',font=('arial',20,'bold'),bg='#1ab5ef')
d.place(x=460,y=440)

p=Label(text='....',font=('arial',20,'bold'),bg='#1ab5ef')
p.place(x=700,y=440)
             

root.mainloop()
