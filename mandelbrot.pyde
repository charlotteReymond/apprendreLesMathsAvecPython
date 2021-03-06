
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

def mandelbrot(z,num):
    count=0
    z1=z
    while count <= num:
        if magnitude(z1) > 2.0:
            return count
        z1=cAdd(cMult(z1,z1),z)
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
    #background(100,100,100)
    
    for x in range(-300,300):
        for y in range(-300,300):

            z=[(xmin + x * xscl),(ymin + y * yscl)]
            col=mandelbrot(z,100)
            if col == 100:
                fill(0)
                rect(x,y,1,1)
            else :
                fill(col*3+150,255,200)
                rect(x,y,1,1)
                
