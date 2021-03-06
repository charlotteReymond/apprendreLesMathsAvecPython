r1=100
r2=10
t=0
circleList=[]

def setup():
    size(600,600)

def draw():
    global t,r1,r2,circleList
    
    background(230)
    translate(width/2,height/2)
    noFill()
    stroke(1)
    ellipse(-100,0,2*r1,2*r1)
    
    fill(255,0,0)
    y=r1*sin(t)
    x=r1*cos(t)
    circleList.insert(0,y)
    circleList =[y]+circleList[:249]
    ellipse(x-100,y,r2,r2)
    
    stroke(0,255,0)
    line(x-100,y,100,y)
    fill(0,255,0)
    ellipse(100,y,r2,r2)
    t+=0.05
    
    for i in range(len(circleList)):
        ellipse(100+i,circleList[i],4,4)
