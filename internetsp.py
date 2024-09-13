from tkinter import *
import speedtest

def speedcheck():
    sp= speedtest.Speedtest()
    sp.get_servers()
    down= (round(sp.download()/(10**6),3))
    up= (round(sp.upload()/(10**6),3))
    lab_down.config(text=down)
    lab_up.config(text=up)



sp= Tk()
sp.title("internet speed test")
sp.geometry("500x650")
sp.config(bg="Blue")
lab=Label(sp,text="internet speed test",font=("Time New Roman",30,"bold"),fg="Red")
lab.place(x=60,y=40,height=50,width=380)

lab=Label(sp,text="download speed test",font=("Time New Roman",30,"bold"))
lab.place(x=60,y=130,height=50,width=380)

lab_down=Label(sp,text="00",font=("Time New Roman",30,"bold"))
lab_down.place(x=60,y=200,height=50,width=380)

lab=Label(sp,text="upload speed test",font=("Time New Roman",30,"bold"))
lab.place(x=60,y=290,height=50,width=380)

lab_up=Label(sp,text="00",font=("Time New Roman",30,"bold"))
lab_up.place(x=60,y=360,height=50,width=380)


button =Button(sp,text="check speed",font=("Time New Roman",30,"bold"),relief=RAISED,bg="Red",command= speedcheck)
button.place(x=60,y=460,height=50,width=380)
sp.mainloop()