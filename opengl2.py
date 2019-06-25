from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
def draw():
    glClearBufferfv(GL_COLOR, 0,(0.5,0.5,0.5))
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutInitWindowSize(400, 400)
glutCreateWindow(b"First")
glutDisplayFunc(draw)
glutMainLoop() 
