
xmin=-2
xmax=2
ymin=-2
ymax=2
rangex= xmax-xmin
rangey =ymax-ymin

def cAdd(a,b):
    return [a[0]+b[0],a[1]+b[1]]

def cMult(u,v):
    return[u[0]*v[0]-u[1]*v[1],u[1]*v[0]+u[0]*v[1]]

def magnitude(z):
    from math import sqrt
    return sqrt(z[0]**2+z[1]**2)

def julia(z,c,num):
    count=0
    z1=z
    while count <= num:
        if magnitude(z1) > 2.0:
            return count
        z1=cAdd(cMult(z1,z1),c)
        count+=1
    return num


def setup():
    global xscl,yscl
    size(600,600)
    noStroke()
    xscl=float(rangex)/width
    yscl=float(rangey)/height
    colorMode(HSB)
    
def draw():
    global xscl,yscl,ymin,xmin
    translate(width/2,height/2)
    x=xmin
    
    while x < xmax:
        y=ymin
        while y < ymax:
            z=[x,y]
            c=[0.29,0.016]
            col=julia(z,c,100)
            if col == 100:
                fill(0,255,0)
                rect(x*100,100*y,1,1)
                println(x)
            else :
                fill(255,col*3,255)
                rect(x*100,100*y,1,1)
            y+=0.01
        x+=0.01
                
                
#0.29-0.016i
