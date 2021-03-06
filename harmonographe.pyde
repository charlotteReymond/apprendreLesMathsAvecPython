t=0
points=[]
def setup():
    size(800,800)
    colorMode(HSB)
def draw():
    global t,points
    translate(width/2,height/2)
    background(0)

    while t < 220:
        points.append(harmonographe(t))
        t+=0.1
        
    for i,p in enumerate(points):
    
        if i < len(points)-1:
            stroke(i/50+3,250,i-100)
            strokeWeight(2)
            line(p[0],p[1],points[i+1][0],points[i+1][1])
    
    
def harmonographe(t):
    a1,a2,a3,a4 = 170,170,170,170
    f1,f2,f3,f4 = 1,2,2,1
    p1,p2,p3,p4 = -PI/2,0,-PI/16,0
    d1,d2,d3,d4 = 0.02,0.02,0.02,0.02

    
    x=a1*cos(f1*t+p1)*exp(-d1*t)+a3*cos(f3*t+p3)*exp(-d3*t)
    y=a2*cos(f2*t+p2)*exp(-d2*t)+a4*cos(f4*t+p4)*exp(-d4*t)
    
    return[x,y]
