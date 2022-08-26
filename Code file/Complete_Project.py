
from tkinter import *

root= Tk()
root.title("Moving objects")
root.geometry("600x600")

w, h = 500 , 500
canvas=Canvas(root, width=w, height=h,bg = "white" )
canvas.pack(pady=20)

# For displaying score
label=Label(root, text="")
label.pack(pady=20)

sling=PhotoImage(file="sling.png")
bird=PhotoImage(file="red-bird3.png")
pig=PhotoImage(file="pig.png")

# Creating pictures of pig on our canvas
pig_points = [(300,300),(400,50),(100, 200),(350,350),(450,450)]
pig1=canvas.create_image(pig_points[0][0],pig_points[0][1],image=pig)
pig2=canvas.create_image(pig_points[1][0],pig_points[1][1],image=pig)
pig3=canvas.create_image(pig_points[2][0],pig_points[2][1],image=pig)
pig4=canvas.create_image(pig_points[3][0],pig_points[3][1],image=pig)
pig5=canvas.create_image(pig_points[4][0],pig_points[4][1],image=pig)

# endpoints of band (line)
p1=(216, 176)
p2=(256, 175)
slingmp = ( (p1[0]+p2[0])/2 ,(p1[1]+p2[1])/2 )

# initializing variables
on_canvas=canvas.create_image (slingmp[0],slingmp[1],image=bird)
sli = canvas.create_image(w/2,h/2, image= sling)
l1, l2 = canvas.create_line(0,0,1,1) , canvas.create_line(0,0,1,1)
score=0
pig1bool = False
pig2bool = False
pig3bool = False
pig4bool = False
pig5bool = False


def pressed(event):

    global on_canvas
    global l1
    global l2
    global sli
    global x
    global y


    canvas.delete(l1)
    canvas.delete(l2)
    canvas.delete(on_canvas)
    canvas.delete(sli)

    # order is important
    l2 = canvas.create_line(p2[0], p2[1], event.x, event.y, fill="black",width=5)
    on_canvas = canvas.create_image(event.x, event.y, image=bird)
    sli=canvas.create_image(w / 2, h / 2, image=sling)
    l1 = canvas.create_line(p1[0], p1[1], event.x, event.y, fill="black", width=5)

    x=event.x
    y=event.y

# To get the points on the line through which the bird travels
def getpoints(x,y):

    slope = (y - slingmp[1])/(x - slingmp[0])
    list1 = []
    x1 , y1 = x , y
    if x1 < slingmp[0]:
        while x1 < w and y1 < h and y1 > 0:
            list1.append([x1, y1])
            x1 += 1
            y1 += slope * 1
    else:
        while x1 > 0 and y1 < h and y1 > 0:
            list1.append([x1, y1])
            x1 -= 1
            y1 += slope * (-1)

    return list1


def shoot(event):
    global score
    global on_canvas
    point_list = getpoints(x,y)

    # pigbools created so that score for a single pig is incremented only once
    # Declared globally so that score not incremented when the bird passes through same pig point on different turns
    global pig1bool
    global pig2bool
    global pig3bool
    global pig4bool
    global pig5bool

    for point in point_list:
        canvas.delete(on_canvas)
        on_canvas = canvas.create_image(point[0], point[1], image=bird)
        if abs(point[0]-pig_points[0][0]) < 20 and abs(point[1]-pig_points[0][1]) < 20 :
            if not pig1bool:
                canvas.delete(pig1)
                score += 10
                pig1bool = True
        if abs(point[0]-pig_points[1][0]) < 20 and abs(point[1]-pig_points[1][1]) < 20 :
            if not pig2bool:
                canvas.delete(pig2)
                score += 10
                pig2bool = True
        if abs(point[0]-pig_points[2][0]) < 20 and abs(point[1]-pig_points[2][1]) < 20 :
            if not pig3bool:
                canvas.delete(pig3)
                score += 10
                pig3bool = True
        if abs(point[0] - pig_points[3][0]) < 20 and abs(point[1] - pig_points[3][1]) < 20:
            if not pig4bool:
                canvas.delete(pig4)
                score += 10
                pig4bool = True
        if abs(point[0] - pig_points[4][0]) < 20 and abs(point[1] - pig_points[4][1]) < 20:
            if not pig5bool:
                canvas.delete(pig5)
                score += 10
                pig5bool = True

    canvas.delete(l1)
    canvas.delete(l2)
    label.config(text="Score is: {}".format(score))

root.bind("<B1-Motion>",pressed)
root.bind("a",shoot)
root.mainloop()