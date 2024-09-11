import os,sys
import customtkinter
import glop

from customtkinter import *
set_appearance_mode("dark")  # Modes: system (default), light, dark
set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
import webbrowser
window = CTk()
window.geometry('630x550')
window.title("Kabbalah Center Connections")
# import datetime as dt

from PIL import Image, ImageTk
from pyluach import dates
from datetime import datetime

basedir = os.path.dirname(__file__)

# window.resizable(False, False)   
window.resizable(0,0)
window.iconbitmap(os.path.join(basedir, "icon.ico"))
# window.iconbitmap("icon.ico")

# button_icon = tk.PhotoImage(file=os.path.join(basedir, "icon.png"))

frame = CTkFrame(master=window,fg_color="black", border_color="#FFFFFF", border_width=12, corner_radius=35)
# frame.pack(expand=True)
frame.pack(fill="both", expand=True)

date =datetime.now()

x = (list(dates.HebrewDate.today()))[0]
y = (list(dates.HebrewDate.today()))[1]
z = (list(dates.HebrewDate.today()))[2]

k = ''
m = ''

u =0           
x = str(x)
for i in x :
    u+=int(i)
v =0  
for j in str(u) :
    v+=int(j)

if y==13:
    y = "Adar II"
    k=12
    m='12L'

if y==1:
    y = 'Nisan'
    k=1
    m='1A'

elif y==2:
    y = 'Iyar'
    k=2
    m='2B'

elif y==3:
    y = 'Sivan'
    k=3
    m='3C'

elif y==4:
    y = 'Tammuz'
    k=4
    m='4D'

elif y==5:
    y = 'Av'
    k=5
    m='5E'

elif y==6:
    y = 'Elul'
    k=6
    m='6F'

elif y==7:
    y = 'Tishre'
    k=7
    m='7G'

elif y==8:
    y = 'Heshvan'
    k=8
    m='8H'

elif y==9:
    y = 'Kishlev'
    k=9
    m='9I'

elif y==10:
    y = 'Tevet'
    k=10
    m='10J'

elif y==11:
    y = 'Shevat'
    k=11
    m='11K'

elif y==12:
    y= "Adar I"
    k=12
    m='12L'

now = datetime.now() 
hour = now.strftime("%H")
if hour >=str(20):
    z=int(z)+1
h = [2,22]   
if z in h:
    y = (f'{z}nd of {y}, {x}')

g = [1,21]   
if z in g:
    y = (f'{z}st of {y}, {x}')

l = [3,23]  
if z in l:
    y = (f'{z}rd of {y}, {x}')

p = [4,5,6,7,8,9,10,11,12,
        13,14,15,16,17,18,19,20,
        24,25,26,27,28,29,30]
    
if z in p:
    y = (f'{z}th of {y}, {x}')











label3 = CTkLabel(master=frame,text=f"{date:%B %d, %Y}", font=("Arial Black", 14))
label3.place(relx=0.07,rely=0.08)
label4 = CTkLabel(master=frame,text=f"{y}", font=("Arial Black", 14))
label4.place(relx=0.65,rely=0.08)

# window.iconbitmap(os.path.join(basedir, "icon.ico")) 

# src = (os.path.join(basedir,"new+app/tkinter/xxx/images/"))
src = (os.path.join(basedir,"images/"))

# im = Image.open(src+str(i)+".jpg")
# for i in range(2):
  
img1 = CTkImage(light_image=Image.open(src+str(k)+".png"), 
    dark_image=Image.open(src+str(k)+".png"),size=(80,40))

img2 = CTkImage(light_image=Image.open(src+str(m)+".png"), 
    dark_image=Image.open(src+str(m)+".png"),size=(90,40))


label = CTkLabel(master=frame,text="", image=img1)
# label.place(relx=0.13,rely=0.18)
label.place(relx=0.08,rely=0.75)

labelx = CTkLabel(master=frame,text="", image=img2)
labelx.place(relx=0.76,rely=0.75)


Bd = CTkButton(master=frame, text ="London Shabbat Connections",width=250,height=37, border_width=3,corner_radius=20,hover_color="green",border_color="yellow",font=("Arial Black", 17), command =lambda: webbrowser.open('https://www.kabbalah.com/en/events/?region=europe&location=london&category=shabbat&template=&delivery_method=streaming&type=&instructor=&language=en'))
Bd.place(relx=0.244,rely=0.18)

# label2 = CTkLabel(master=frame,text=f"{date:%B %d}", font=("Arial", 13))

B1 = CTkButton(master=frame, text ="Insights From Rav Berg",width=264,height=39, border_width=3,corner_radius=38,hover_color="green",border_color="yellow",font=("Arial Black", 17),
                             command=lambda: webbrowser.open('https://www.kabbalah.com/en/online-courses/lessons/beresheet-the-blessing-in-the-beginning/'))
B1.place(relx=0.04,rely=0.298)

B2 = CTkButton(master=frame, text ="Teachings of Rav Berg",width=250,height=39, border_width=3,corner_radius=38,hover_color="green",border_color="yellow",font=("Arial Black", 17), command =lambda: webbrowser.open('https://www.kabbalah.com/en/online-courses/lessons/3568-the-new-moon-of-cancer-removing-confusion/'))
B2.place(relx=0.53,rely=0.298)

B3 = CTkButton(master=frame, text ="Live Streams",width=276,height=39, border_width=3,corner_radius=38,hover_color="green",border_color="yellow",font=("Arial Black", 17), command =lambda: webbrowser.open('https://www.kabbalah.com/en/events/streams/'))
B3.place(relx=0.04,rely=0.41)
B4 = CTkButton(master=frame, text ="Kabbalistic Meditation",width=250,height=39, border_width=3,corner_radius=38,hover_color="green",border_color="yellow",font=("Arial Black", 17), command =lambda: webbrowser.open('https://www.kabbalah.com/en/online-courses/lessons/72-names-13-heaven-on-earth/'))
B4.place(relx=0.53,rely=0.41)
B5 = CTkButton(master=frame, text ="Upcoming Events/Classes",width=250,height=39, border_width=3,corner_radius=38,hover_color="green",border_color="yellow",font=("Arial Black", 17), command =lambda: webbrowser.open('https://www.kabbalah.com/en/events/'))
B5.place(relx=0.04,rely=0.52)
B6 = CTkButton(master=frame, text ="Online Stores",width=250,height=39, border_width=3,corner_radius=38,hover_color="green",border_color="yellow",font=("Arial Black", 17), command =lambda: webbrowser.open('https://store.kabbalah.com/') )
B6.place(relx=0.53,rely=0.52)
B7 = CTkButton(master=frame, text ="Online Zohar",width=276,height=39, border_width=3,corner_radius=38,hover_color="green",border_color="yellow",font=("Arial Black", 17), command = lambda: webbrowser.open('https://www.zohar.com/zohar') )
B7.place(relx=0.04,rely=0.63)
B8 = CTkButton(master=frame, text ="Online Torah",width=250,height=39, border_width=3,corner_radius=38,hover_color="green",border_color="yellow",font=("Arial Black", 17), command = lambda: webbrowser.open('https://www.chabad.org/parshah/otherparshas_cdo/aid/9175/jewish/All-Parshahs.htm'))
B8.place(relx=0.53,rely=0.63)

label1 = CTkLabel(master=frame,text="- SUPPORT -", font=("Arial Black", 15))
label1.place(relx=0.4,rely=0.72)

label1 = CTkLabel(master=frame,text="Account Name:- Shlomo and Shlomo Consult.\nBank Name:- Access\nAccount Number:- 1225959863", font=("Arial", 13,))
label1.place(relx=0.27,rely=0.77)










window.mainloop()