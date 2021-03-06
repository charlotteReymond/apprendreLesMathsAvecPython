xmin=-10
xmax=10
ymin=-10
ymax=10
rangex=xmax-xmin
rangey=ymax-ymin

def setup():
    global xscl,yscl
    size(600,600)
    xscl = width / rangex
    yscl = -height / rangey
def draw():
    global xscl,yscl
    background(255)
    translate(width/2,height/2)
    gride()
    graphFunction()
def graphFunction():
    x=xmin
    while x <=xmax:
        stroke(255,0,0)
        line(x*xscl,f(x)*yscl,(x+0.1)*xscl,f(x+0.1)*yscl)
        x += 0.1
             
def f(x):
    return(sin(x))
def gride():
    strokeWeight(1)
    stroke(0,125,255)
    for i in range(xmin,xmax+1):
        line(i*xscl,ymin*yscl,i*xscl,xmax*yscl)
        line(xmin*xscl,i*yscl,xmax*xscl,i*yscl)
    strokeWeight(2)
    stroke(0)
    line(xmin*xscl,0,xmax*xscl,0)
    line(0,ymin*yscl,0,ymax*yscl)
    
