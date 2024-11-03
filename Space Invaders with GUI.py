from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox
import mysql.connector as sql
import turtle
import math
import random
import time

global cursor
global obj

#TKinter Windows
'''
PageOne()-win1 LOGIN,REGISTER,EXIT
login()-win2 LOGIN,BACK
register()-win3 SUBMIT,BACK
new_window()-win4 PLAY,UPDATE...
view1()-win5 HIGHSCORE
view2()-win6 STATISTICS
update_screen()-win7 UPDATE,BACK
view3()-win8 UPDATED DATA
final_window()-win9 RATE,LOGOUT
'''


#Connection
obj=sql.connect(host='localhost',user='<YOUR MYSQL USERNAME>',password='<YOUR MYSQL PASSWORD>',database='login_details')
cursor=obj.cursor()

#Fisrt Page
def PageOne():    
    global win1
    
    win1=Tk()
    win1.title("SPACE INVADERS")
    win1.geometry("125x120")

    l1=Label(win1,text="SPACE INVADERS",font=("bold",10))
    l1.grid(row=0,column=0)
    
    b1=Button(win1,text="Login",command=login).grid(row=1,column=0)
    b2=Button(win1,text="Register",command=register).grid(row=2,column=0)
    b3=Button(win1,text="Exit",command=close).grid(row=3,column=0)
    mainloop()

#Exit
def close():
    obj.close()
    quit()

def close2():

    obj=sql.connect(host='localhost',user='<YOUR MYSQL USERNAME>',password='<YOUR MYSQL PASSWORD>',database='login_details')
    cursor=obj.cursor()
    rate=v_1.get()
    try:
        qs="update details set experience ={} where username='{}'".format(rate,username)
        cursor.execute(qs)
        obj.commit()
    except:
        pass
    obj.close()
    quit()

#Redirection
def L_redirect():
    win2.destroy()
    PageOne()

def R_redirect():
    win3.destroy()
    PageOne()

def G_redirect():
    win4.destroy()
    PageOne()

def U_redirect():
    win7.destroy()
    PageOne()

def v1_redirect():
    win5.destroy()

def v2_redirect():
    win6.destroy()

def v3_redirect():
    win8.destroy()

#Login
def login():

    global T1
    global T2
    global win2

    win1.destroy()
    win2=Tk()
    win2.geometry('250x100')
    win2.title("Login Screen")
   
    l1=Label(win2,text="Enter Username")
    l1.grid(row=1,column=0)
    V1=StringVar()
    T1=Entry(win2,textvariable=V1)
    T1.grid(row=1,column=1)

    l2=Label(win2,text="Enter Password")
    l2.grid(row=2,column=0)
    V2=StringVar()
    T2=Entry(win2,textvariable=V2)
    T2.grid(row=2,column=1)

    b1=Button(win2,text="Login",command=call)
    b1.grid(row=3,column=0)
    b2=Button(win2,text="Back",command=L_redirect)
    b2.grid(row=4,column=0)

    win2.mainloop()

def call():

    global username
    global password
    username=T1.get()
    password=T2.get()
    print(username)
    print(password)

    cursor=obj.cursor()

    qs="select * from details where username='{}' and password='{}'".format(username,password)
    cursor.execute(qs)
    data=cursor.fetchall()

    if cursor.rowcount>0:
        new_window()     
    else:
        tkinter.messagebox.showinfo("User Information","Username or Password is Incorrect")

#Registration
def register():

    global v1
    global v2
    global v3
    global v4
    global win3
    
    win1.destroy()
    win3=Tk()
    win3.geometry('500x150')
    win3.title("Registration Screen")
   
    l1=Label(win3,text="Name",width=20,font=('bold',10)) #NAME
    l1.grid(row=1,column=0)
    v1=StringVar()
    t1=Entry(win3,textvariable=v1)
    t1.grid(row=1,column=1)

    l2=Label(win3,text="Gender",width=20,font=("bold",10)) #GENDER
    l2.grid(row=2,column=0)
    v2=StringVar()
    v2.set(None)
    r1=Radiobutton(win3,text="Male",variable=v2,value="M")
    r1.grid(row=2,column=1)
    r2=Radiobutton(win3,text="Female",variable=v2,value="F")
    r2.grid(row=2,column=2)

    l3=Label(win3,text="Username",width=20,font=('bold',10)) #USERNAME
    l3.grid(row=3,column=0)
    v3=StringVar()
    t3=Entry(win3,textvariable=v3)
    t3.grid(row=3,column=1)

    l4=Label(win3,text="Password",width=20,font=("bold",10)) #PASSWORD
    l4.grid(row=4,column=0)
    v4=StringVar()
    t4=Entry(win3,textvariable=v4)
    t4.grid(row=4,column=1)

    b1=Button(win3,text="Submit",width=20,command=save) #SUBMIT BUTTON
    b1.grid(row=6,columnspan=2)
    b2=Button(win3,text="Back",width=20,command=R_redirect) #BACK BUTTON
    b2.grid(row=7,columnspan=2)

    win3.mainloop()

def save():

    name1=v1.get()
    gender1=v2.get()
    username1=v3.get()
    password1=v4.get()

    rate1=0

    print(name1)
    print(gender1)
    print(username1)
    print(password1)
    
    cursor=obj.cursor()

    try:

        qs2="insert into details values('{}','{}','{}','{}',{})".format(name1,gender1,username1,password1,rate1) 
        cursor.execute(qs2)
        obj.commit()
        print(cursor.rowcount)

        if cursor.rowcount>0:
            tkinter.messagebox.showinfo("User Information","Data Saved")
        else:
            tkinter.messagebox.showinfo("User Information","Data cannot be Saved")
    
    except:
        tkinter.messagebox.showinfo("User Information","Username is Taken, Please Enter a different one") 
#GAME

def background():
    global win10
    #Screen
 
    win10=turtle.Screen()
    win10.bgcolor("black")
    win10.title("Space Invaders")    
    
    #Border

    border_pen=turtle.Turtle()
    border_pen.speed(0)
    border_pen.color("white")
    border_pen.penup()
    border_pen.setposition(-300,-300)
    border_pen.pendown()
    border_pen.pensize(3)

    for side in range(4):
        border_pen.fd(600)
        border_pen.lt(90)
            
    border_pen.hideturtle()
    

#Movement (Left, Right, Down and Up)
def move_left():
    x=player.xcor()
    x-=playerspeed
    if x<-280:
        x=-280
    player.setx(x)

def move_right():
    x=player.xcor()
    x+=playerspeed
    if x>280:
        x=280
    player.setx(x)

def move_down():
    y=player.ycor()
    y-=playerspeed
    if y<-280:
        y=-280
    player.sety(y)

def move_up():
    y=player.ycor()
    y+=playerspeed
    if y>280:
        y=280
    player.sety(y)
def fire_bullet():
    #Declare bulletstate as a global if it needs change
    global bulletstate

    if bulletstate=="ready":
        bulletstate="fire"
        #Move bullet just above the player
        x=player.xcor()
        y=player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()

def isCollision(t1,t2):
    distance=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance<16:
        return True
    else:
        return False        

def stopWatch(value):
    
    #From seconds to Hours:Minutes:Seconds
    global new_value

    valueD = (((value/60)/24)/365)
    Days = int (valueD)

    valueH = (valueD-Days)*365
    Hours = int(valueH)

    valueM = (valueH - Hours)*24
    Minutes = int(valueM)

    valueS = (valueM - Minutes)*60
    Seconds = int(valueS)

    new_value=str(Hours)+":"+str(Minutes)+":"+str(Seconds)
    print (new_value)



def play():

    global player
    global enemies
    global playerspeed
    global enemyspeed
    global bullet
    global bulletstate
    global score

    #Background
    background()
    
    #Set the score to 0
    score=0

    #Set the time
    start_time=time.time()
    
    #Draw Score
    score_pen=turtle.Turtle()
    score_pen.speed(0)
    score_pen.color("white")
    score_pen.penup()
    score_pen.setposition(-290,258)
    scorestring="Score: %s" %score
    score_pen.write(scorestring,False,align="left", font=("Ariel",13,"normal"))
    score_pen.hideturtle()
    
    #Draw Username
    user_pen=turtle.Turtle()
    user_pen.speed(0)
    user_pen.color("white")
    user_pen.penup()
    user_pen.setposition(-290,275)
    user_pen.write(username,False,align="left", font=("Ariel",13,"normal"))
    user_pen.hideturtle()
    print(username)
    
    #Player
    player=turtle.Turtle()
    player.color("blue")
    player.shape("triangle")
    player.penup()
    player.speed(0)
    player.setposition(0,-250)
    player.setheading(90)

    playerspeed=15

    #Choose the number of enemies
    n=5
    enemies=[]
    #Add enemies to the list

    
    for i in range(n):
        enemies.append(turtle.Turtle())

    for enemy in enemies:
        enemy.color("red")
        enemy.shape("circle")
        enemy.penup()
        enemy.speed(0)
        x=random.randint(-200,200)
        y=random.randint(100,250)
        enemy.setposition(x,y)

    enemyspeed=5

    #Bullets
    bullet=turtle.Turtle()
    bullet.color("white")
    bullet.shape("square")
    bullet.penup()
    bullet.speed(0)
    bullet.setheading(90)
    bullet.shapesize(0.25,0.5)
    bullet.hideturtle()
    x=player.xcor()
    y=player.ycor() - 100
    bullet.setposition(x,y)
    bulletspeed=20

    #Bullet State

    #Ready to Fire
    #Fire
    bulletstate="ready"
        
    #Keyboard Binding
    turtle.listen()

    turtle.onkeypress(move_left,"a")
    turtle.onkeypress(move_right,"d")
    turtle.onkeypress(move_down,"s")
    turtle.onkeypress(move_up,"w")
    turtle.onkey(fire_bullet,"space")
        
    #Main Game Loop
    while True:
        gamestatus=1
        for enemy in enemies:
            #Move The Enemy
            x=enemy.xcor()
            x+=enemyspeed
            enemy.setx(x)

            #Move the Enemy Back and Down
            if enemy.xcor()>280:
                #Move all the enemies down
                for e in enemies:
                    y=e.ycor()
                    y-=40
                    e.sety(y)
                #Change enemy direction
                enemyspeed*=-1

            if enemy.xcor()<-280:
                #Move all the enemies down
                for e in enemies:
                    y=e.ycor()
                    y-=40
                    e.sety(y)
                #Change enemy direction
                enemyspeed*=-1    

            
            #Check for collision between bullet and enemy
            if isCollision(bullet,enemy):
                #Reset the bullet
                bullet.hideturtle()
                bulletstate="ready"
                bullet.setposition(0,-400)
                #Reset the enemy
                x=random.randint(-200,200)
                y=random.randint(100,250)
                enemy.setposition(x,y)
                #Update the score
                score+=10
                scorestring="Score: %s" %score
                score_pen.clear()
                score_pen.write(scorestring,False,align="left", font=("Ariel",13,"normal"))

            #GAME OVER
            if enemy.ycor()<-240 or isCollision(player,enemy):
                enemies=[]
                end_time=time.time() #End the time
                value=end_time-start_time
                stopWatch(value)
                print(score)
                highscore()
                statistics()
                win10.clear()
                final_window()
                gamestatus=0
                

        #Move the bullet
        if bulletstate=="fire":
            y=bullet.ycor()
            y+=bulletspeed
            bullet.sety(y)

        #Check to see if the bullet has gone to the top
        if bullet.ycor()>275:
            bullet.hideturtle()
            bulletstate="ready"

        if gamestatus==0:
            win10.bye()
            win10.mainloop()
            
            
#Highscore

def highscore():

    global obj
    obj.close()
    obj=sql.connect(host='localhost',user='<YOUR MYSQL USERNAME>',password='YOUR MYSQL PASSWORD>',database='login_details')
    cursor=obj.cursor()

    if score > 0:
        qs="insert into highscore values('{}',{})".format(username,score)
        cursor.execute(qs)
        obj.commit()

def pull1():
    global obj
    obj.close()
    obj=sql.connect(host='localhost',user='<YOUR MYSQL USERNAME>',password='<YOUR MYSQL PASSWORD>',database='login_details')
    cursor=obj.cursor()
    
    qs="select * from highscore order by score desc"
    cursor.execute(qs)
    data=cursor.fetchmany(10)
    for i in data:
        tree.insert('','end',values=(i))
    tree.grid(row=1,column=0)

def view1():

    global win5
    global tree
    win5=Tk()

    win5.title("SCOREBOARD")
    win5.geometry("700x300")
    tree=Treeview(win5)
    tree["columns"]=(1,2)
    tree.column(1,width=200)
    tree.column(2,width=150)
    tree.heading(1,text="Username")
    tree.heading(2,text="Score")
    b1=Button(win5,text="Back",command=v1_redirect).grid(row=3,column=0)
    pull1()

#Statistics
def statistics():
    obj=sql.connect(host='localhost',user='<YOUR MYSQL USERNAME>',password='<YOUR MYSQL PASSWORD>',database='login_details')
    cursor=obj.cursor()
    
    qs="insert into statistics values('{}',{},'{}')".format(username,score/10,new_value)
    cursor.execute(qs)
    obj.commit()

def pull2():

    global Matches
    global obj
    
    obj.close()
    obj=sql.connect(host='localhost',user='<YOUR MYSQL USERNAME>',password='<YOUR MYSQL PASSWORD>',database='login_details')
    cursor=obj.cursor()
    
    qs="select kills,time from statistics where username = '{}'".format(username)
    cursor.execute(qs)
    data=cursor.fetchall()
    Matches=cursor.rowcount
    print(Matches)

    for j in data:
        tree2.insert('','end',values=(j))
    tree2.grid(row=1,column=0)

def view2():

    global win6
    global tree2
    
    print(username,'Details')
    win6=Tk()

    win6.title("STATISTICS")
    win6.geometry("500x300")
    tree2=Treeview(win6)
    tree2["columns"]=(1,2)
    tree2.column(1,width=100)
    tree2.column(2,width=100)
    tree2.heading(1,text="Invader Kills")
    tree2.heading(2,text="Time Duration")
    b1=Button(win6,text="Back",command=v2_redirect).grid(row=3,column=0)
    
    pull2()

#Change Details and History
def update_screen():

    global T_1
    global T_2
    global win7

    win4.destroy()
    win7=Tk()
    win7.geometry('300x150')
    win7.title("Update Screen")

    l1=Label(win7,text="Enter New Username")
    l1.grid(row=0,column=0)
    V_1=StringVar()
    T_1=Entry(win7,textvariable=V_1)
    T_1.grid(row=0,column=1)

    l2=Label(win7,text="Enter New Password")
    l2.grid(row=1,column=0)
    V_2=StringVar()
    T_2=Entry(win7,textvariable=V_2)
    T_2.grid(row=1,column=1)

    b1=Button(win7,text="Update",command=call2)
    b1.grid(row=2,column=0)
    
    b3=Button(win7,text="Back",command=U_redirect)
    b3.grid(row=4,column=0)

    win7.mainloop()

def call2():
    global username2
    global obj
    
    obj.close()
    obj=sql.connect(host='localhost',user='<YOUR MYSQL USERNAME>',password='<YOUR MYSQL PASSWORD>',database='login_details')
    cursor=obj.cursor()
    
    username2=T_1.get()
    password2=T_2.get()
    print(username2)
    print(password2)

    try:
        qs="select name from details where username='{}'".format(username)
        cursor.execute(qs)
        data2=cursor.fetchall()
        NAME1=data2[0]
        print(data2)
        NAME2=NAME1[0]
        print(NAME2)

        qs1="update details set username='{}' where username='{}'".format(username2,username)
        cursor.execute(qs1)
        obj.commit()
            
        qs2="update details set password='{}' where username='{}'".format(password2,username2)
        cursor.execute(qs2)
        obj.commit()
            
        qs3="update highscore set username='{}' where username='{}'".format(username2,username)
        cursor.execute(qs3)
        obj.commit()

        qs4="update statistics set username='{}' where username='{}'".format(username2,username)
        cursor.execute(qs4)
        obj.commit()

        qs5="insert into new_details  values('{}','{}','{}','{}','{}')".format(username,password,username2,password2,NAME2)
        cursor.execute(qs5)
        obj.commit()

        if cursor.rowcount>0:
            tkinter.messagebox.showinfo("User Information","Data Updated")
        else:
            tkinter.messagebox.showinfo("User Information","Data cannot be Updated")
    except:

        tkinter.messagebox.showinfo("User Information","Username is Taken, Please enter a different Username")

def pull3():

    global obj
    
    obj.close()

    obj=sql.connect(host='localhost',user='<YOUR MYSQL USERNAME>',password='<YOUR MYSQL PASSWORD>',database='login_details')
    
    cursor=obj.cursor()

    qs="select name from details where username='{}'".format(username)
    cursor.execute(qs)
    data3=cursor.fetchall()
    NAME2=data3[0]
    print(data3)
    NAME3=NAME2[0]
    print(NAME3)
    
    qs1="select old_username,old_password,new_username,new_password from new_details where name = '{}'".format(NAME3)
    cursor.execute(qs1)
    data=cursor.fetchall()

    for j in data:
        tree3.insert('','end',values=(j))
    tree3.grid(row=1,column=0)

def view3():

    global win8
    global tree3
    print(username,'New_Details')
    
    win8=Tk()

    win8.title("UPDATED INFORMATION")
    win8.geometry("800x300")
    tree3=Treeview(win8)
    tree3["columns"]=(1,2,3,4)
    tree3.column(1,width=120)
    tree3.column(2,width=120)
    tree3.column(3,width=120)
    tree3.column(4,width=120)
    tree3.heading(1,text="OLD USERNAME")
    tree3.heading(2,text="OLD PASSWORD")
    tree3.heading(3,text="NEW USERNAME")
    tree3.heading(4,text="NEW PASSWORD")
    b1=Button(win8,text="Back",command=v3_redirect).grid(row=3,column=0)
    pull3()

#Main Menu

def new_window():

    global win4
    global num
    global obj
    
    obj.close()
    obj=sql.connect(host='localhost',user='<YOUR MYSQL USERNAME>',password='<YOUR MYSQL PASSWORD>',database='login_details')   
    cursor=obj.cursor()

    num=0
    
    win2.destroy()
    win4=Tk()
    win4.geometry("200x200")
    win4.title("Main Menu")

    l=Label(win4,text="MAIN MENU",font=('bold',10)).grid(row=0,column=0)

    l1=Label(win4,text="w - Move Up").grid(row=3,column=1)
    l2=Label(win4,text="s - Move Back").grid(row=4,column=1)
    l3=Label(win4,text="a - Move Left").grid(row=5,column=1)
    l4=Label(win4,text="d - Move Right").grid(row=6,column=1)
    l5=Label(win4,text="Spacebar - Shoot").grid(row=7,column=1)
    
    b1=Button(win4,text="Play",command=play).grid(row=2,column=0)
    b2=Button(win4,text="Highscore",command=view1).grid(row=3,column=0)
    b2=Button(win4,text="Statistics",command=view2).grid(row=4,column=0)
    b4=Button(win4,text="Update Info",command=update_screen).grid(row=5,column=0)
    b5=Button(win4,text="Info History",command=view3).grid(row=6,column=0)
    b6=Button(win4,text="Back",command=G_redirect).grid(row=7,column=0)
 
    qs="select name from details where username='{}'".format(username)
    cursor.execute(qs)
    data1=cursor.fetchall()
    NAME=data1[0]
    print(data1)
    print(NAME)

    qs="select gender from details where username='{}'".format(username)
    cursor.execute(qs)
    data2=cursor.fetchall()
    print(data2)
    print(data2[0][0])

    qs="select experience from details where username='{}'".format(username)
    cursor.execute(qs)
    data3=cursor.fetchall()
    print(data3)
    RATE=data3[0][0]
    print(RATE)

    if RATE>0 and RATE<=3:
        Label(win4,text="Rating: %s/10"%RATE).grid(row=1,column=1)
    elif RATE>3 and RATE<=7:
        Label(win4,text="Rating: %s/10"%RATE).grid(row=1,column=1)
    elif RATE>7 and RATE<=10:
        Label(win4,text="Rating: %s/10"%RATE).grid(row=1,column=1)
        
        
    if data2[0][0]=='M':
        Label(win4,text="Hello Mr. %s !"%NAME).grid(row=1,column=0)
    elif data2[0][0]=='F':
        Label(win4,text="Hello Ms. %s !"%NAME).grid(row=1,column=0)
        
    win4.mainloop()

#Last Page 
def final_window():

    global win9
    global v_1
    win4.destroy()
    win9=Tk()
    win9.geometry("180x75")
    win9.title("Game Over Screen")
    l=Label(win9,text="GAME OVER !!!",font=('bold',10)).grid(row=0,column=0)

    l1=Label(win9,text="Rate your Experience").grid(row=1,column=0)
    list1=['','1','2','3','4','5','6','7','8','9','10']
    v_1=StringVar()
    droplist=OptionMenu(win9,v_1,*list1)
    v_1.set("Select")
    droplist.grid(row=1,column=1)
    
    b1=Button(win9,text="Log-Out",command=close2).grid(row=2,column=0)

PageOne()
