from tkinter import *
import speedtest

# Creating speed checking function
def speed_check():
    spt=speedtest.Speedtest()
    spt.get_servers()
    down=str(round(spt.download()/(10**6),3)) + "Mbps"
    up=str(round(spt.upload()/(10**6),3)) + "Mbps"
    downspeed_label.config(text=down)
    upspeed_label.config(text=up)



# Creating GUI
st=Tk()
st.title("Net speed test")
st.geometry("600x600")
st.config(bg="black")

test_label=Label(st,text="The Internet Speed Test", font=("Times New Roman",20,"bold"),bg="black",fg="white")
test_label.place(x=90,y=40)

down_label=Label(st,text="Download Speed", font=("Times New Roman",20,"bold"),bg="black",fg="white")
down_label.place(x=90,y=120)

downspeed_label=Label(st,text="00", font=("Times New Roman",20,"bold"),fg="black")
downspeed_label.place(x=90,y=220,height=40, width=150)

up_label=Label(st,text="Upload Speed", font=("Times New Roman",20,"bold"),bg="black",fg="white")
up_label.place(x=90,y=290)


upspeed_label=Label(st,text="00", font=("Times New Roman",20,"bold"),fg="black")
upspeed_label.place(x=90,y=390,height=40, width=150)

check_button=Button(st,text="Check Speed",font=("Times New Roman",20,"bold"),bg="red",relief=RAISED, command=speed_check)
check_button.place(x=90,y=490,height=40,width=200)



st.mainloop()