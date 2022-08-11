time=input()
if(time[-2]=="A"):
    if(time[0:2]=="12"):
        y="00"
        print(y,end="")
        print(time[2:8])
    else:
        print(time[0:8])
if(time[-2]=="P"):
    if(time[0]=="1" and time[1]=="2"):
        print("12",end="")
        print(time[2:8])
    else:
        a=(time[:2])
        x=int(a)
        b=x+12
        print(b,end="")
        print(time[2:8])