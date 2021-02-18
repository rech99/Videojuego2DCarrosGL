from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *

def dibujarCalle():

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    glVertex3f(-1.0,1.0,0.0)
    glVertex3f(1.0,1.0,0.0)
    glVertex3f(1.0,-1.0,0)
    glVertex3f(-1.0,-1.0,0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glColor3f(.4, .4, .4)
    glBegin(GL_QUADS)
    glVertex3f(-0.4, 1, 0.0)
    glVertex3f(0.45, 1, 0.0)
    glVertex3f(0.45, -1, 0.0)
    glVertex3f(-0.4, -1, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glColor3f(.9, .9, .0)
    glBegin(GL_QUADS)
    glVertex3f(-0.01, .8, 0.0)
    glVertex3f(0.06, .8, 0.0)
    glVertex3f(0.06, .6, 0.0)
    glVertex3f(-0.01, .6, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()    
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glColor3f(.9, .9, .0)
    glBegin(GL_QUADS)
    glVertex3f(-0.01, .5, 0.0)
    glVertex3f(0.06, .5, 0.0)
    glVertex3f(0.06, .3, 0.0)
    glVertex3f(-0.01, .3, 0.0)
    glEnd()
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glColor3f(.9, .9, .0)
    glBegin(GL_QUADS)
    glVertex3f(-0.01, .2, 0.0)
    glVertex3f(0.06, .2, 0.0)
    glVertex3f(0.06, .0, 0.0)
    glVertex3f(-0.01, .0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glBegin(GL_QUADS)
    glColor3f(.9, .9, .0)
    glVertex3f(-0.01, -.6, 0.0)
    glVertex3f(0.06, -.6, 0.0)
    glVertex3f(0.06, -.4, 0.0)
    glVertex3f(-0.01, -.4, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glBegin(GL_QUADS)
    glColor3f(.9, .9, .0)
    glVertex3f(-0.01, -.3, 0.0)
    glVertex3f(0.06, -.3, 0.0)
    glVertex3f(0.06, -.1, 0.0)
    glVertex3f(-0.01, -.1, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glBegin(GL_QUADS)
    glColor3f(.9, .9, .0)
    glVertex3f(-0.01, -.9, 0.0)
    glVertex3f(0.06, -.9, 0.0)
    glVertex3f(0.06, -.7, 0.0)
    glVertex3f(-0.01, -.7, 0.0)
    glEnd()
    glPopMatrix()

def dibujarJugador():

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    glColor3f(1.0,1.0,1.0)
    glVertex3f(-1.0,1.0,0.0)
    glVertex3f(1.0,1.0,0.0)
    glVertex3f(1.0,-1.0,0)
    glVertex3f(-1.0,-1.0,0)
    glEnd()
    glPopMatrix()


    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glBegin(GL_QUADS)
    glColor3f(.9, 0, .1)
    glVertex3f(-0.3, -.6, 0.0)
    glVertex3f(-0.3, .6, 0.0)
    glVertex3f(0.3, .6, 0.0)
    glVertex3f(0.3, -.6, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glBegin(GL_QUADS)
    glColor3f(0, .0, .0)
    glVertex3f(0.1, -.6, 0.0)
    glVertex3f(0.05, -.6, 0.0)
    glVertex3f(0.05, .6, 0.0)
    glVertex3f(0.1, .6, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glBegin(GL_QUADS)
    glColor3f(0, .0, .0)
    glVertex3f(-0.1, -.6, 0.0)
    glVertex3f(-0.05, -.6, 0.0)
    glVertex3f(-0.05, .6, 0.0)
    glVertex3f(-0.1, .6, 0.0)
    glEnd()
    glPopMatrix()

    

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glBegin(GL_QUADS)
    glColor3f(.0, 1, 1)
    glVertex3f(-.3, .3, 0.0)
    glVertex3f(-.3, .5, 0.0)
    glVertex3f(.3, .5, 0.0)
    glVertex3f(.3, .3, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glBegin(GL_QUADS)
    glColor3f(1,  0, .1)
    glVertex3f(-.4, -.4, 0.0)
    glVertex3f(-.4, -.5, 0.0)
    glVertex3f(.4, -.5, 0.0)
    glVertex3f(.4, -.4, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glBegin(GL_QUADS)
    glColor3f(.0,  0, .0)
    glVertex3f(-.4, -.45, 0.0)
    glVertex3f(-.4, -.475, 0.0)
    glVertex3f(.4, -.475, 0.0)
    glVertex3f(.4, -.45, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glBegin(GL_QUADS)
    glColor3f(.0,  0, .0)
    glVertex3f(-.4, -.42, 0.0)
    glVertex3f(-.4, -.445, 0.0)
    glVertex3f(.4, -.445, 0.0)
    glVertex3f(.4, -.42, 0.0)
    glEnd()
    glPopMatrix()

def dibujarPolicia():

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    glVertex3f(-1.0,1.0,0.0)
    glVertex3f(1.0,1.0,0.0)
    glVertex3f(1.0,-1.0,0)
    glVertex3f(-1.0,-1.0,0)
    glEnd()
    glPopMatrix()


    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glColor3f(.1, .0, .6)
    glBegin(GL_QUADS)
    glVertex3f(-0.3, -.6, 0.0)
    glVertex3f(-0.3, .6, 0.0)
    glVertex3f(0.3, .6, 0.0)
    glVertex3f(0.3, -.6, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glVertex3f(-0.2, -.5, 0.0)
    glVertex3f(-0.2, .5, 0.0)
    glVertex3f(0.2, .5, 0.0)
    glVertex3f(0.2, -.5, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex3f(-0.15, -.4, 0.0)
    glVertex3f(-0.15, .2, 0.0)
    glVertex3f(-0.1, .2, 0.0)
    glVertex3f(-0.1, -.4, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex3f(-0.15, .25, 0.0)
    glVertex3f(-0.15, .2, 0.0)
    glVertex3f(0.15, .2, 0.0)
    glVertex3f(0.15, .25, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex3f(0.15, .0, 0.0)
    glVertex3f(0.15, .25, 0.0)
    glVertex3f(0.10, .25, 0.0)
    glVertex3f(0.10, .0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex3f(-0.15, .25, 0.0)
    glVertex3f(-0.15, .2, 0.0)
    glVertex3f(0.15, .2, 0.0)
    glVertex3f(0.15, .25, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex3f(-0.15, .05, 0.0)
    glVertex3f(-0.15, .0, 0.0)
    glVertex3f(0.15, .0, 0.0)
    glVertex3f(0.15, .05, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glBegin(GL_QUADS)
    glColor3f(.9, .0, .1)
    glVertex3f(-.3, .3, 0.0)
    glVertex3f(-.3, .5, 0.0)
    glVertex3f(.1, .5, 0.0)
    glVertex3f(.1, .3, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glBegin(GL_QUADS)
    glColor3f(.3, .2, 1)
    glVertex3f(0.3, .5, 0.0)
    glVertex3f(0.3, .3, 0.0)
    glVertex3f(0.0, .3, 0.0)
    glVertex3f(0.0, .5, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glBegin(GL_QUADS)
    glColor3f(.3, .2, 1)
    glVertex3f(0.3, .5, 0.0)
    glVertex3f(0.3, .3, 0.0)
    glVertex3f(0.0, .3, 0.0)
    glVertex3f(0.0, .5, 0.0)
    glEnd()
    glPopMatrix()

def dibujarCono():

    
    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    glVertex3f(-1.0,1.0,0.0)
    glVertex3f(1.0,1.0,0.0)
    glVertex3f(1.0,-1.0,0)
    glVertex3f(-1.0,-1.0,0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    glColor3f(1, 0.6, 0.0)
    glVertex3f(-.4, -.5, 0.0)
    glVertex3f(0.4, -.5, 0.0)
    glVertex3f(0, .8, 0.0)
    glEnd()
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glBegin(GL_QUADS)
    glColor3f(1, .7, 0.0)
    glVertex3f(-.45, -.35, 0.0)
    glVertex3f(0.45, -.35, 0.0)
    glVertex3f(0.45, -.5, 0.0)
    glVertex3f(-.45, -.5, 0.0)
    glEnd()
    glPopMatrix()
    
def dibujarRoca():

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    glVertex3f(-1.0,1.0,0.0)
    glVertex3f(1.0,1.0,0.0)
    glVertex3f(1.0,-1.0,0)
    glVertex3f(-1.0,-1.0,0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glColor3f(.7, .7, .7)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos (angulo) ,sin (angulo)  ,0.0)
    glEnd()
    glPopMatrix()

def dibujarMarco():

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    glVertex3f(-1.0,1.0,0.0)
    glVertex3f(1.0,1.0,0.0)
    glVertex3f(1.0,-1.0,0)
    glVertex3f(-1.0,-1.0,0)
    glEnd()
    glPopMatrix()


    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glBegin(GL_QUADS)
    glColor3f(0.6, 1, 0)
    glVertex3f(-1, -1, 0.0)
    glVertex3f(-.95, -1, 0.0)
    glVertex3f(-0.95, 1, 0.0)
    glVertex3f(-1, 1, 0.0)
    glEnd()
    glPopMatrix()    


    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glBegin(GL_QUADS)
    glColor3f(0.6, 1, 0)
    glVertex3f(1, 1, 0.0)
    glVertex3f(.95, 1, 0.0)
    glVertex3f(0.95, -1, 0.0)
    glVertex3f(1, -1, 0.0)
    glEnd()  
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glBegin(GL_QUADS)
    glColor3f(0.6, 1, 0)
    glVertex3f(1, 1, 0.0)
    glVertex3f( 1, .95, 0.0)
    glVertex3f(-1,  0.95, 0.0)
    glVertex3f( -1, 1, 0.0)
    glEnd() 
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glBegin(GL_QUADS)
    glColor3f(0.6, 1, 0)
    glVertex3f(-1, -1, 0.0)
    glVertex3f( -1, -.95, 0.0)
    glVertex3f(1,  -0.95, 0.0)
    glVertex3f( 1, -1, 0.0)
    glEnd() 
    glPopMatrix()

def dibujarBarril():
        
    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    glVertex3f(-1.0,1.0,0.0)
    glVertex3f(1.0,1.0,0.0)
    glVertex3f(1.0,-1.0,0)
    glVertex3f(-1.0,-1.0,0)
    glEnd()
    glPopMatrix()

   
  
    
    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glBegin(GL_QUADS)
    glColor3f(.7, 1, 0)
    glVertex3f(-0.4, -.7, 0.0)
    glVertex3f(-0.4, .4, 0.0)
    glVertex3f(0.4, .4, 0.0)
    glVertex3f(0.4, -.7, 0.0)
    glEnd()
    glPopMatrix()
 

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glRotate(0, 0, 0, 1)
    glBegin(GL_QUADS)
    glColor3f(0, 0, 0)
    glVertex3f(0.2, .0, 0.0)
    glVertex3f(-0.2, .0, 0.0)
    glVertex3f(-0.2, -.4, 0.0)
    glVertex3f(0.2, -.4, 0.0)
   
    glEnd()
    glPopMatrix()
 
    

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.,1.0,1.0)  
    glBegin(GL_POLYGON)
    glColor3f(.1, 1, 0)

    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos (angulo) * 0.4 + 0 ,sin (angulo) * 0.3 + 0.4 ,0.0)
    
    glEnd()
    glPopMatrix()

def dibujarSol():

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    glVertex3f(-1.0,1.0,0.0)
    glVertex3f(1.0,1.0,0.0)
    glVertex3f(1.0,-1.0,0)
    glVertex3f(-1.0,-1.0,0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glBegin(GL_QUADS)
    glColor3f(1, .8, 0)
    glVertex3f(.6, .6, 0.0)
    glVertex3f(-.6, .6, 0.0)
    glVertex3f(-.6, -.6, 0.0)
    glVertex3f(.6, -.6, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glRotate(30,0,0,1)
    glBegin(GL_QUADS)
    glColor3f(1, .8, 0)
    glVertex3f(.6, .6, 0.0)
    glVertex3f(-.6, .6, 0.0)
    glVertex3f(-.6, -.6, 0.0)
    glVertex3f(.6, -.6, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glRotate(60,0,0,1)
    glBegin(GL_QUADS)
    glColor3f(1, .8, 0)
    glVertex3f(.6, .6, 0.0)
    glVertex3f(-.6, .6, 0.0)
    glVertex3f(-.6, -.6, 0.0)
    glVertex3f(.6, -.6, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glRotate(90,0,0,1)
    glBegin(GL_QUADS)
    glColor3f(1, .8, 0)
    glVertex3f(.6, .6, 0.0)
    glVertex3f(-.6, .6, 0.0)
    glVertex3f(-.6, -.6, 0.0)
    glVertex3f(.6, -.6, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glColor3f(.9,1, .1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos (angulo) * 0.7 + 0 ,sin (angulo) * 0.7 + 0 ,0.0)
    glEnd()
    glPopMatrix()

def dibujarCielo():

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    glVertex3f(-1.0,1.0,0.0)
    glVertex3f(1.0,1.0,0.0)
    glVertex3f(1.0,-1.0,0)
    glVertex3f(-1.0,-1.0,0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glColor3f(.2, .6, 1)
    glBegin(GL_POLYGON)
    glVertex3f(-1.0,1.0,0.0)
    glVertex3f(1.0,1.0,0.0)
    glVertex3f(1.0,-1.0,0)
    glVertex3f(-1.0,-1.0,0)
    glEnd()
    glPopMatrix()

def dibujarPajaro():
    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    glVertex3f(-1.0,1.0,0.0)
    glVertex3f(1.0,1.0,0.0)
    glVertex3f(1.0,-1.0,0)
    glVertex3f(-1.0,-1.0,0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    glVertex3f(-1.0,1.0,0.0)
    glVertex3f(1.0,1.0,0.0)
    glVertex3f(1.0,-1.0,0)
    glVertex3f(-1.0,-1.0,0)
    glEnd()
    glPopMatrix()


def dibujarPonchaLlantas():

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    glVertex3f(-1.0,1.0,0.0)
    glVertex3f(1.0,1.0,0.0)
    glVertex3f(1.0,-1.0,0)
    glVertex3f(-1.0,-1.0,0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glBegin(GL_QUADS)
    glColor3f(0.4, .4, .4)
    glVertex3f(-.65, .4, 0.0)
    glVertex3f(0.65, .4, 0.0)
    glVertex3f(.65, .35, 0.0)
    glVertex3f(-.65, .35, 0.0)
    glEnd()
    glPopMatrix() 

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1,1,1)
    glBegin(GL_POLYGON)
    glColor3f(0.4, .4, .4)
    glVertex3f(-.65, .6, 0.0)
    glVertex3f(-.60, .35, 0.0)
    glVertex3f(-.7, .35, 0.0)
    glEnd()
    glPopMatrix() 

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1,1,1)
    glBegin(GL_POLYGON)
    glColor3f(0.4, .4, .4)
    glVertex3f(-.55, .6, 0.0)
    glVertex3f(-.50, .35, 0.0)
    glVertex3f(-.6, .35, 0.0)
    glEnd()
    glPopMatrix() 

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1,1,1)
    glBegin(GL_POLYGON)
    glColor3f(0.4, .4, .4)
    glVertex3f(-.45, .6, 0.0)
    glVertex3f(-.40, .35, 0.0)
    glVertex3f(-.5, .35, 0.0)
    glEnd()
    glPopMatrix() 

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1,1,1)
    glBegin(GL_POLYGON)
    glColor3f(0.4, .4, .4)
    glVertex3f(-.35, .6, 0.0)
    glVertex3f(-.30, .35, 0.0)
    glVertex3f(-.4, .35, 0.0)
    glEnd()
    glPopMatrix() 
    
    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1,1,1)
    glBegin(GL_POLYGON)
    glColor3f(0.4, .4, .4)
    glVertex3f(-.25, .6, 0.0)
    glVertex3f(-.20, .35, 0.0)
    glVertex3f(-.3, .35, 0.0)
    glEnd()
    glPopMatrix() 

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1,1,1)
    glBegin(GL_POLYGON)
    glColor3f(0.4, .4, .4)
    glVertex3f(-.15, .6, 0.0)
    glVertex3f(-.10, .35, 0.0)
    glVertex3f(-.2, .35, 0.0)
    glEnd()
    glPopMatrix() 

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1,1,1)
    glBegin(GL_POLYGON)
    glColor3f(0.4, .4, .4)
    glVertex3f(-.05, .6, 0.0)
    glVertex3f(-.0, .35, 0.0)
    glVertex3f(-.1, .35, 0.0)
    glEnd()
    glPopMatrix() 

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1,1,1)
    glBegin(GL_POLYGON)
    glColor3f(0.4, .4, .4)
    glVertex3f(-.05, .6, 0.0)
    glVertex3f(.010, .35, 0.0)
    glVertex3f(.0, .35, 0.0)
    glEnd()
    glPopMatrix() 

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1,1,1)
    glBegin(GL_POLYGON)
    glColor3f(0.4, .4, .4)
    glVertex3f(.65, .6, 0.0)
    glVertex3f(.60, .35, 0.0)
    glVertex3f(.7, .35, 0.0)
    glEnd()
    glPopMatrix() 

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1,1,1)
    glBegin(GL_POLYGON)
    glColor3f(0.4, .4, .4)
    glVertex3f(.55, .6, 0.0)
    glVertex3f(.50, .35, 0.0)
    glVertex3f(.6, .35, 0.0)
    glEnd()
    glPopMatrix() 

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1,1,1)
    glBegin(GL_POLYGON)
    glColor3f(0.4, .4, .4)
    glVertex3f(.45, .6, 0.0)
    glVertex3f(.40, .35, 0.0)
    glVertex3f(.5, .35, 0.0)
    glEnd()
    glPopMatrix() 

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1,1,1)
    glBegin(GL_POLYGON)
    glColor3f(0.4, .4, .4)
    glVertex3f(.35, .6, 0.0)
    glVertex3f(.30, .35, 0.0)
    glVertex3f(.4, .35, 0.0)
    glEnd()
    glPopMatrix() 
    
    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1,1,1)
    glBegin(GL_POLYGON)
    glColor3f(0.4, .4, .4)
    glVertex3f(.25, .6, 0.0)
    glVertex3f(.20, .35, 0.0)
    glVertex3f(.3, .35, 0.0)
    glEnd()
    glPopMatrix() 

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1,1,1)
    glBegin(GL_POLYGON)
    glColor3f(0.4, .4, .4)
    glVertex3f(.15, .6, 0.0)
    glVertex3f(.10, .35, 0.0)
    glVertex3f(.2, .35, 0.0)
    glEnd()
    glPopMatrix() 

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1,1,1)
    glBegin(GL_POLYGON)
    glColor3f(0.4, .4, .4)
    glVertex3f(.05, .6, 0.0)
    glVertex3f(.0, .35, 0.0)
    glVertex3f(.1, .35, 0.0)
    glEnd()
    glPopMatrix() 
    
def dibujarSeñal():

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    glVertex3f(-1.0,1.0,0.0)
    glVertex3f(1.0,1.0,0.0)
    glVertex3f(1.0,-1.0,0)
    glVertex3f(-1.0,-1.0,0)
    glEnd()
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glBegin(GL_QUADS)
    glColor3f(0.7, 0.7, 0.6)
    glVertex3f(-0.2, -.7, 0.0)
    glVertex3f(-0.2, .3, 0.0)
    glVertex3f(0.2, .3, 0.0)
    glVertex3f(0.2, -.7, 0.0)
    

    glEnd()
    glPopMatrix()
    

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)  
    glBegin(GL_POLYGON)
    glColor3f(1, 0, 0)

    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos (angulo) * 0.4 + 0 ,sin (angulo) * 0.4 + 0.5 ,0.0)
    
    glEnd()
    glPopMatrix()

def dibujarValla():
    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    glVertex3f(-1.0,1.0,0.0)
    glVertex3f(1.0,1.0,0.0)
    glVertex3f(1.0,-1.0,0)
    glVertex3f(-1.0,-1.0,0)
    glEnd()
    glPopMatrix()


    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glBegin(GL_QUADS)
    glColor3f(0.4, .1, 0)
    glVertex3f(-.7, 0, 0.0)
    glVertex3f(-.65, 0, 0.0)
    glVertex3f(-0.65, .65, 0.0)
    glVertex3f(-.7, .65, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glBegin(GL_QUADS)
    glColor3f(0.4, .1, 0)
    glVertex3f(.7, 0, 0.0)
    glVertex3f(.65, 0, 0.0)
    glVertex3f(0.65, .65, 0.0)
    glVertex3f(.7, .65, 0.0)
    glEnd()
    glPopMatrix()  

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glBegin(GL_QUADS)
    glColor3f(0.4, .4, .4)
    glVertex3f(-.65, .6, 0.0)
    glVertex3f(0.65, .6, 0.0)
    glVertex3f(.65, .55, 0.0)
    glVertex3f(-.65, .55, 0.0)
    glEnd()
    glPopMatrix()  

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glBegin(GL_QUADS)
    glColor3f(0.4, .4, .4)
    glVertex3f(-.65, .5, 0.0)
    glVertex3f(0.65, .5, 0.0)
    glVertex3f(.65, .45, 0.0)
    glVertex3f(-.65, .45, 0.0)
    glEnd()
    glPopMatrix()  

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glBegin(GL_QUADS)
    glColor3f(0.4, .4, .4)
    glVertex3f(-.65, .4, 0.0)
    glVertex3f(0.65, .4, 0.0)
    glVertex3f(.65, .35, 0.0)
    glVertex3f(-.65, .35, 0.0)
    glEnd()
    glPopMatrix() 

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glBegin(GL_QUADS)
    glColor3f(0.4, .4, .4)
    glVertex3f(-.65, .3, 0.0)
    glVertex3f(0.65, .3, 0.0)
    glVertex3f(.65, .25, 0.0)
    glVertex3f(-.65, .25, 0.0)
    glEnd()
    glPopMatrix() 

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glBegin(GL_QUADS)
    glColor3f(0.4, .4, .4)
    glVertex3f(-.65, .2, 0.0)
    glVertex3f(0.65, .2, 0.0)
    glVertex3f(.65, .15, 0.0)
    glVertex3f(-.65, .15, 0.0)
    glEnd()
    glPopMatrix() 

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glBegin(GL_QUADS)
    glColor3f(0.4, .4, .4)
    glVertex3f(-.65, .1, 0.0)
    glVertex3f(0.65, .1, 0.0)
    glVertex3f(.65, .05, 0.0)
    glVertex3f(-.65, .05, 0.0)
    glEnd()
    glPopMatrix() 

def dibujarNubes():

    glPushMatrix()
    glTranslatef(0.0,0.0,0)
    glScalef(1.0,1.0,1.0)
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    glVertex3f(-1.0,1.0,0.0)
    glVertex3f(1.0,1.0,0.0)
    glVertex3f(1.0,-1.0,0)
    glVertex3f(-1.0,-1.0,0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.1,0.0,0)
    glScalef(1.0,1.0,1.0)
    glColor3f(1,.9,.9)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos (angulo) * 0.3 + 0.3 ,sin (angulo) * 0.2 + .1 ,0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.1,0.0,0)
    glScalef(1.0,1.0,1.0)
    glColor3f(1,.9,.9)
    glBegin(GL_POLYGON)
    glColor3f(1,.9,.9)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos (angulo) * 0.3 - .0 ,sin (angulo) * 0.2 - .1 ,0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.1,0.0,0)
    glScalef(1.0,1.0,1.0)
    glColor3f(1,.9,.9)
    glBegin(GL_POLYGON)
    glColor3f(1,.9,.9)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos (angulo) * 0.3 + -.3 ,sin (angulo) * 0.2 + .1 ,0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.1,0.0,0)
    glScalef(1.0,1.0,1.0)
    glColor3f(1,.9,.9)
    glBegin(GL_POLYGON)
    glColor3f(1,.9,.9)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos (angulo) * 0.3 - .0 ,sin (angulo) * 0.2 + .3 ,0.0)
    glEnd()
    glPopMatrix()

def dibujar():
    dibujarCalle()
    dibujarPolicia()
    dibujarCono()
    dibujarRoca()
    dibujarMarco()
    dibujarSeñal()
    dibujarNubes()
    dibujarSol()
    dibujarJugador()
    dibujarValla()
    dibujarPonchaLlantas()
    dibujarBarril()
    dibujarCielo()


def main():
    #inicia glfw
    ancho= 800
    alto = 800
    if not glfw.init():
        return
    
    #crea la ventana, 
    # independientemente del SO que usemos
    window = glfw.create_window(ancho,alto,"Mi ventana", None, None)

    #Configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    #Establecemos el contexto
    glfw.make_context_current(window)

    #Activamos la validación de 
    # funciones modernas de OpenGL
    glewExperimental = True

    #Inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #Obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    while not glfw.window_should_close(window):
        #Establece regiond e dibujo
        glViewport(0,0, ancho, alto)
        #Establece color de borrado
        glClearColor(0.9,0.8,0.5,1)
        #Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Dibujar
        dibujar()

        #Preguntar si hubo entradas de perifericos
        #(Teclado, mouse, game pad, etc.)
        glfw.poll_events()
        #Intercambia los buffers
        glfw.swap_buffers(window)

    #Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #Termina los procesos que inició glfw.init
    glfw.terminate()

if __name__ == "__main__":
    main()