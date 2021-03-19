import pygame
from pygame.locals import*

import  pygame.gfxdraw
root =pygame.display.set_mode([200,200])




def dd(v,gx=0,gy=1):
     return int(v[gx]),int(v[gy])
def ddli (v0,v1,gx=0,gy=1):
     a,b =dd(v0,gx,gy)
     c,d =dd(v1,gx,gy)
     return a,b,c,d

def ddLigne(v0,v1,gx=0,gy=1,dx=0,dy=0):
     a,b,c,d =ddli(v0,v1,gx,gy)
     pygame.gfxdraw.line(root,a+dx,b+dy,c+dx,d+dy,[120,20,80])
     
v0 =pygame.Vector3(0,0,0)
v1 =pygame.Vector3(50,0,0)
v2 =pygame.Vector3(50,50,0)
v3 =pygame.Vector3(0,50,0)
v4 =pygame.Vector3(25,25,50)
vr =pygame.Vector3(1,0,0)
de =0
gx,gy  =0,1
while 1:
     de +=1
     root.fill([255,250,250])
     for event in pygame.event.get()    :
          if(event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
               pygame()
    
     pygame.display.set_caption(str(de)+"3D PYRAMIDE")
     if de >360:de=0

     v0 =v0.rotate(de,vr)
     v1 =v1.rotate(de,vr)
     v2 =v2.rotate(de,vr)
     v3 =v3.rotate(de,vr)
     v4 =v4.rotate(de,vr)
     
     ddLigne(v0,v1,gx,gy,50,50)
     ddLigne(v1,v0,gx,gy,50,50)
     ddLigne(v1,v2,gx,gy,50,50)
     ddLigne(v2,v3,gx,gy,50,50)
     ddLigne(v3,v0,gx,gy,50,50)

     ddLigne(v0,v4,gx,gy,50,50)
     ddLigne(v1,v4,gx,gy,50,50)
     ddLigne(v2,v4,gx,gy,50,50)
     ddLigne(v3,v4,gx,gy,50,50)

     pygame.display.update()
     pygame.time.wait(500)
