#!/usr/bin/env python
# coding: utf-8

# TUNES (MUSIC COMMUNITY)

# In[ ]:


from tkinter import * 
import webbrowser
base = Tk()  
base.geometry("500x500")  
base.title("TUNES") 
base.configure(bg='Black')
  
lb1= Label(base, text="ENTER NAME", width=10, font=("arial",12))  
lb1.place(x=5, y=120)  
en1= Entry(base)  
en1.place(x=200, y=120)  
   
list_of_ms = ("pop", "R&B", "bollywood", "pop electronic")  
cv = StringVar()  
drplist= OptionMenu(base, cv, *list_of_ms)  
drplist.config(width=15)  
cv.set("pop")  
lb2= Label(base, text="GENRE", width=13,font=("arial",12))  
lb2.place(x=5,y=200)  
drplist.place(x=200, y=200)  

def openNewWindow():
    newWindow = Toplevel(base)
    newWindow.title("newpage")
    newWindow.geometry("700x400")
    newWindow.configure(bg='orange')
    Label(newWindow,text ="Click on the below mentioned links to be the part of the music comunity. ").pack()
    label2 = Label(newWindow,text ="pop", width=20)
    label2.place(x=50, y=200)
    label2.bind("<Button-1>", lambda e:
    callback("https://open.spotify.com/playlist/5TDtuKDbOhrfW7C58XnriZ?si=495b391a81164266"))
    label3= Label(newWindow,text ="R&B", width=20)
    label3.place(x=200, y=200)
    label3.bind("<Button-1>", lambda e:
    callback("https://open.spotify.com/album/3wn07z4XXQZsHyyGETCOT9?si=iNipTeSYRIqOjickydmpWw"))
    newWindow.geometry("700x400")
    label4= Label(newWindow,text ="Bollywood", width=20)
    label4.place(x=350, y=200)
    label4.bind("<Button-1>", lambda e:
    callback("https://open.spotify.com/playlist/0S7boBN3rPfo2F1DXX5U7k?si=73bdf4b4902d4fad"))
    newWindow.geometry("700x400")
    label5= Label(newWindow,text ="Pop Electronic", width=20)
    label5.place(x=500, y=200)
    label5.bind("<Button-1>", lambda e:
    callback("https://open.spotify.com/playlist/37i9dQZF1EIgiybBTM5LX0?si=b01bd9adabbf44f5"))
    newWindow.geometry("700x400")
    label6= Label(newWindow,text ="click to join the discord server", width=100)
    label6.place(x=5, y=300)
    label6.bind("<Button-1>", lambda e:
    callback("https://discord.gg/ay2Htenw"))
    newWindow.geometry("700x400")
   
   
   
   
    

          
def callback(url):
    webbrowser.open_new_tab(url)   
    
Button(base, text="click to join comunity", width=30, command=openNewWindow).place(x=150,y=300)  
base.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




