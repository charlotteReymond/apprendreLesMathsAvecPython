def setup():
    size(600,600)
    rectMode(CENTER)
    colorMode(HSB)
t=0
def draw():
    background(255)
    global t
    translate(width/2,height/2)
    for i in range(90):
        rotate(radians(360/90))
        pushMatrix()
        translate(200,0)
        rotate(radians(t+i*2*360/90))
        strokeWeight(2)
        stroke(i*360/90,255,180)
        tri(100)
        popMatrix()
    
    t+=1
    
def tri(length):
    noFill()
    triangle(0,-length,-length*sqrt(3)/2,length/2,length*sqrt(3)/2,length/2)
