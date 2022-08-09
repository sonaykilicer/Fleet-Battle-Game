from OpenGL.GL import *
from OpenGL.GL import glBegin
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
from math import *
import random
import PIL
from PIL import Image
import numpy
import time

sys.setrecursionlimit(10000)
oyna = 0
kazanmaekranı = 0
tutturmao = 0
tutturmay = 0
ax,ay=0,0
baslama = 0
tutmakontrol1 = 0
gemi = 0
mousex = 0
mousey = 0
oyuncu = 0


xc1,xc2,yc1,yc2,xc3,yc3,xc4,yc4,xc5,yc5=0,0,0,0,0,0,0,0,0,0 # gemi translate değişkenleri



#gemi viewportları

w1 = -90
h1 = 360
w2 = -230
h2 = 360
w3=-230
h3 = 360-280
w4 = -90
h4 = 360-280
w5 = -230
h5 = 360-490

#deneme karesi viewport

dw1 = 735
dh1 = 395

#yapay zeka deneme karesi viewport
dw2 = 15
dh2 = 395

di1 = 735
di2 = 395



tıkla1 = -1
oynandi = 0
tutmakontrol1 = 0
yatay1,yatay2,yatay3,yatay4,yatay5 = 0,0,0,0,0 # gemi yatay kontrolü
angle1,angle2,angle3,angle4,angle5 = 0,0,0,0,0 # gemi açı
rx = 0 # rastgele x kordinatı
ry = 0 # rastgele y kordinatı

#gemi kordinat listeleri
listx  = []
listy  = []
listt = []

#deneme karesi kordinat listeleri
listdx = []
listdy = []
listdt = []


#gemi tutma listeleri
listdw1 = []
listdh1 = []

listdw2 = []
listdh2 = []
#gemi tutmama listeleri

listdwn1 = []
listdhn1 = []

listdwn2 = []
listdhn2 = []

#rastgele gemi kordinatlarını tutan listeler
listyx = []
listyy = []
listyt = []
list2yy = []
list3yy = []

#rastgele kordinatları tutan listeler
listrx = []
listry = []
listrt = []

#liste atamaları
for j in range(10):

    listrx.append(j)

for j in range(0,-10,-1):

    listry.append(j)


for j in range(9):

    listyx.append(j)

for j in range(0,-9,-1):

    listyy.append(j)

for j in range(0,-7,-1):

    list2yy.append(j)

for j in range(0,-6,-1):

    list3yy.append(j)




listx.append(0)
listy.append(0)
listdx.append(0)
listdy.append(0)

for i in range (14):

    listt.append([listx[0],listy[0]])

listdt.append([listdx[0],listdy[0]])



#gemi yerlestirme sirasi
yerlestirmesayisi1 = 0

#işaret gemi tutma kontrol değişkeni
tutmakontrol = 0







def loadTexture(nameimage):#gemi ve anaekran texture fonksiyonu

    img = PIL.Image.open(nameimage)
    img_data = numpy.array(list(img.getdata()), numpy.int8)

    glEnable(GL_TEXTURE_2D)
    id = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, id)

    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
    return id

def loadTexture2(nameimage):#you win ve you lose texture fonksiyonu

    img = PIL.Image.open(nameimage)
    img_data = numpy.array(list(img.getdata()), numpy.int8)

    glEnable(GL_TEXTURE_2D)
    id = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, id)

    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_MIRRORED_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_MIRRORED_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
    return id



def InitGL():

    glClearColor(0,1, 1.0, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-5.0, 5.0, -5.0, 5.0)
    glMatrixMode(GL_MODELVIEW)

def menudraw():#menu cizdirme fonksiyonu


    glPushMatrix()

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, loadTexture2("anaekran.jpg"))

    glTranslatef(-6,-6,0)
    glScalef(4,4,4)
    glBegin(GL_QUADS)

    glTexCoord2f(1, 1)
    glVertex3f(4, 0, 0)

    glTexCoord2f(1, 0)
    glVertex3f(4, 3, 0)

    glTexCoord2f(0, 0)

    glVertex3f(0, 3, 0)
    glTexCoord2f(0, 1)

    glVertex3f(0, 0, 0)

    glEnd()

    glPopMatrix()


def drawfunc():#main çizdirme fonksiyonu


    global dw1,dh1,oynandi,listdw1,listdh1,listdhn1,listdwn1,tutmakontrol,listtyt,yerlestirmesayisi1,listrt,listrx,listry,tutmakontrol1,listtxt,ry,rx
    global tutturmay,tutturmao,kazanmaekranı,oyna

    glClear(GL_COLOR_BUFFER_BIT)

    if(oyna == 0):

        menudraw()

    elif(oyna==1):

        if(kazanmaekranı == 0):

            drawplayer1()

            if (oynandi == 1):

                for i in range (14):

                    if(listdt[0] == listyt[i]):#gemi tutma kontrolü

                            tutmakontrol = 1
                            tutturmao += 1
                            listdw1.append(dw1)
                            listdh1.append(dh1)

                            for i in range(len(listdw1)):

                                drawx(listdw1[i], listdh1[i])

                            oynandi = 0
                            if (tutturmao == 14):#kazanan kontrolü
                                kazanmaekranı = 1
                            break

                if(tutmakontrol == 0):

                            listdwn1.append(dw1)
                            listdhn1.append(dh1)

                            for i in range(len(listdwn1)):
                                drawy(listdwn1[i], listdhn1[i])

                            yerlestirmesayisi1 += 1

                            oynandi = 0

            tutmakontrol = 0


            for i in range(len(listdw1)):
                drawx(listdw1[i], listdh1[i])

            for i in range(len(listdwn1)):
                drawy(listdwn1[i], listdhn1[i])

            if (yerlestirmesayisi1 == 6):#yapay zeka sırası


                yapayzekadeneme()#rastgele kordinat

                for i in range (14):


                    if(listrt[0] == listt[i]):#gemi tutma kontrolü


                            tutmakontrol1 = 1
                            tutturmay += 1
                            listdw2.append(dw2+70*rx)
                            listdh2.append(dh2+70*ry)

                            for i in range(len(listdw2)):

                                drawx(listdw2[i], listdh2[i])





                            if(tutturmay == 14):#kazanma kontrolü

                                kazanmaekranı += 2




                            break

                if(tutmakontrol1 == 0):


                            listdwn2.append(dw2+(70*rx))
                            listdhn2.append(dh2+(70*ry))

                            for i in range(len(listdwn1)):

                                drawy(listdwn1[i], listdhn1[i])

                            yerlestirmesayisi1 -= 1




            tutmakontrol1 = 0

            for i in range(len(listdw2)):
                drawx(listdw2[i], listdh2[i])

            for i in range(len(listdwn2)):
                drawy(listdwn2[i], listdhn2[i])


        elif(kazanmaekranı==1):

            drawkazanan()


        elif (kazanmaekranı == 2):

            drawkaybeden()

    glutSwapBuffers()
    glutPostRedisplay()

def drawkazanan():#you win resminin çizdirilmesi
        global tutturmao
        glLoadIdentity()
        glMatrixMode(GL_MODELVIEW)

        if(tutturmao==14):

            kazanmaekranı = 1
            glPushMatrix()

            glEnable(GL_TEXTURE_2D)
            glBindTexture(GL_TEXTURE_2D, loadTexture2("youwin.jpg"))

            glViewport(200, 100, 1000, 1000)
            glBegin(GL_QUADS)


            glTexCoord2f(1, 1)
            glVertex3f(4, 0, 0)

            glTexCoord2f(1, 0)
            glVertex3f(4, 2, 0)

            glTexCoord2f(0, 0)

            glVertex3f(0, 2, 0)
            glTexCoord2f(0, 1)

            glVertex3f(0, 0, 0)

            glEnd()

            glPopMatrix()


def drawkaybeden():#you lose resminin çizdirilmesi

    global tutturmay
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)

    if (tutturmay == 14):
        kazanmaekranı = 1
        glPushMatrix()

        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, loadTexture2("youlose.jpg"))

        glViewport(200, 100, 1000, 1000)
        glBegin(GL_QUADS)

        glTexCoord2f(1, 1)
        glVertex3f(4, 0, 0)

        glTexCoord2f(1, 0)
        glVertex3f(4, 2, 0)

        glTexCoord2f(0, 0)

        glVertex3f(0, 2, 0)
        glTexCoord2f(0, 1)

        glVertex3f(0, 0, 0)

        glEnd()

        glPopMatrix()


def drawplayer1():#gemileri ve tabloyu çizdiren fonksyion


    global w1, h1, xc1, yc1, xc2, yc2, angle3, w5, y5,r
    global angle1, angle2, angle3, angle4, angle5
    global yerlestirmesayisi1


    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)

    glPushMatrix()

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, loadTexture("gemi2.jpg"))

    glTranslatef(xc1, yc1, 0)
    glRotatef(angle1, 0, 0, 1)
    glViewport(w1, h1, 700, 700)

    glBegin(GL_QUADS)

    glColor3f(0.1, 1, 1)
    glTexCoord2f(1, 0)
    glVertex2f(0, 1)
    glTexCoord2f(1, 1)
    glVertex2f(-1, 1)
    glTexCoord2f(0, 1)
    glVertex2f(-1, -2)
    glTexCoord2f(0, 0)
    glVertex2f(0, -2)


    glEnd()

    glPopMatrix()

    glPushMatrix()

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, loadTexture("gemi2.jpg"))
    glTranslatef(xc2, yc2, 0)
    glRotatef(angle2, 0, 0, 1)
    glViewport(w2, h2, 700, 700)

    glBegin(GL_QUADS)

    glColor3f(0.1, 1, 1)
    glTexCoord2f(1,0)
    glVertex2f(0, 1)
    glTexCoord2f(1, 1)
    glVertex2f(-1, 1)
    glTexCoord2f(0, 1)
    glVertex2f(-1, -2)
    glTexCoord2f(0, 0)
    glVertex2f(0, -2)

    glEnd()

    glPopMatrix()

    glPushMatrix()
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, loadTexture("gemi1.jpg"))

    glTranslatef(xc3, yc3, 0)
    glRotatef(angle3, 0, 0, 1)
    glViewport(w3, h3, 700, 700)

    glBegin(GL_QUADS)

    glColor3f(0.1, 1, 1)
    glTexCoord2f(1, 0)
    glVertex2f(0, 1)
    glTexCoord2f(1, 1)
    glVertex2f(-1, 1)
    glTexCoord2f(0, 1)
    glVertex2f(-1, -1)
    glTexCoord2f(0, 0)
    glVertex2f(0, -1)

    glEnd()
    glPopMatrix()

    glPushMatrix()
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, loadTexture("gemi1.jpg"))

    glTranslatef(xc4, yc4, 0)
    glRotatef(angle4, 0, 0, 1)
    glViewport(w4, h4, 700, 700)

    glBegin(GL_QUADS)

    glColor3f(0.1, 1, 1)
    glTexCoord2f(1, 0)
    glVertex2f(0, 1)
    glTexCoord2f(1, 1)
    glVertex2f(-1, 1)
    glTexCoord2f(0, 1)
    glVertex2f(-1, -1)
    glTexCoord2f(0, 0)
    glVertex2f(0, -1)

    glEnd()

    glPopMatrix()

    glPushMatrix()

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, loadTexture("gemi3.jpg"))

    glTranslatef(xc5, yc5, 0)
    glRotatef(angle5, 0, 0, 1)
    glViewport(w5, h5, 700, 700)

    glBegin(GL_QUADS)

    glColor3f(0.1, 1, 1)
    glTexCoord2f(1, 0)
    glVertex2f(0, 1)
    glTexCoord2f(1, 1)
    glVertex2f(-1, 1)
    glTexCoord2f(0, 1)
    glVertex2f(-1, -3)
    glTexCoord2f(0, 0)
    glVertex2f(0, -3)

    glEnd()

    glPopMatrix()

    glPushMatrix()
    glViewport(dw1, dh1, 700, 700)

    glBegin(GL_QUADS) #deneme tahtası

    glColor3f(0, 0, 1)
    glVertex2f(0, 0.25)
    glVertex2f(-0.25, 0.25)
    glVertex2f(-0.25, 0)
    glVertex2f(0, 0)



    glEnd()

    glPopMatrix()

    glPushMatrix()
    glColor3f(0.0, 0.0, 0.0)
    glViewport(330, 80, 700, 700)
    glLineWidth(4)

    for x in range(-10, 10):
        for y in range(-10, 10):
            glBegin(GL_LINE_LOOP)

            glVertex2f(x, y)
            glVertex2f(x + 1, y)
            glVertex2f(x + 1, y + 1)
            glVertex2f(x, y + 1)
            glEnd()
    glPopMatrix()

    glPushMatrix()
    glViewport(1050, 80, 700, 700)
    glLineWidth(4)

    for y in range(-10, 10):
        for x in range(-10, 10):
            glBegin(GL_LINE_LOOP)

            glVertex2f(x, y)#*/-
            glVertex2f(x + 1, y)
            glVertex2f(x + 1, y + 1)
            glVertex2f(x, y + 1)
            glEnd()

    glPopMatrix()




#1111

def drawx(x,y):#kırmızı çarpıları çizdirir
    glDisable(GL_TEXTURE_2D)
    glPushMatrix()
    glColor3f(1, 0, 0)
    glViewport(x, y, 700, 700)
    glLineWidth(4)

    glBegin(GL_LINES)

    glVertex2f(0.5, 0.5)
    glVertex2f(-0.5, -0.5)
    glVertex2f(-0.5, 0.5)
    glVertex2f(0.5, -0.5)

    glEnd()

    glPopMatrix()

def drawy(x,y):#sarı çarpıları çizdirir

    glDisable(GL_TEXTURE_2D)
    glPushMatrix()
    glColor3f(1, 1, 0)
    glViewport(x, y, 700, 700)
    glLineWidth(4)

    glBegin(GL_LINES)

    glVertex2f(0.5, 0.5)
    glVertex2f(-0.5, -0.5)
    glVertex2f(-0.5, 0.5)
    glVertex2f(0.5, -0.5)

    glEnd()

    glPopMatrix()

def yapayzekadeneme():#rastgele kare işaretleyen fonksyion

    global listrx,listry,listrt,rx,ry,baslama

    rx = random.choice(listrx)
    ry = random.choice(listry)

    listrt.insert(0, [rx, ry])

    if(baslama == 1):

        for z in range(1,len(listrt),1):

            if(listrt[0] == listrt[z]):#daha önce işaretlenmemiş kare kontrolü

              yapayzekadeneme()

              break


    baslama = 1



def yapayzeka():#rastgele gemileri oluşturan fonkisyon

   global listyy,listyx,ax,ay,list2yy,list3yy

   ax = random.choice(listyx)
   ay = random.choice(listyy)

   listyt.append([ax,ay])
   listyt.append([ax,ay-1])
   listyx.remove(ax)

   ax = random.choice(listyx)
   ay = random.choice(list2yy)

   listyt.append([ax, ay])
   listyt.append([ax, ay - 1])
   listyt.append([ax, ay - 2])

   listyx.remove(ax)


   ax = random.choice(listyx)
   ay = random.choice(listyy)

   listyt.append([ax, ay])
   listyt.append([ax, ay - 1])

   listyx.remove(ax)

   ax = random.choice(listyx)
   ay = random.choice(list3yy)

   listyt.append([ax, ay])
   listyt.append([ax, ay - 1])
   listyt.append([ax, ay - 2])
   listyt.append([ax, ay - 3])

   listyx.remove(ax)


   ax = random.choice(listyx)
   ay = random.choice(list2yy)

   listyt.append([ax, ay])
   listyt.append([ax,ay - 1])
   listyt.append([ax,ay - 2])
   listyx.remove(ax)










def mouseMotion(x, y):#mouseun konumunu olusturan fonksiyon

    global mousex
    global mousey
    mousex = x
    mousey = y






def mousefunc(button,state,x,y):#gemilerin sınırlarına göre döndüren ve yerleştiren fonksiyon


    global w1,w2,w3,w4,w5
    global h1,h2,h3,h4,h5
    global tıkla1,oyna
    global angle1,angle2,angle3,angle4,angle5
    global yc1,yc2,yc3,yc4,yc5
    global yatay1,yatay2,yatay3,yatay4,yatay5

    if(tıkla1 == -1):

        if (state == GLUT_DOWN and button == GLUT_LEFT and mousey <= 830 and mousey >= 730 and mousex <= 870 and mousex >= 560):

            tıkla1 += 1
            oyna = 1


    elif (tıkla1 == 0):

        if (state == GLUT_DOWN and button == GLUT_RIGHT_BUTTON and mousey <= 330 and mousey >= 120 and mousex <= 120 and mousex >= 50):
            angle2 += 90
            yc2 += 1
            yatay2 = 1

        elif (state == GLUT_DOWN and button == GLUT_LEFT_BUTTON and mousey <= 330 and mousey >= 120 and mousex <= 120 and mousex >= 50):
                tıkla1 += 1
                w2 += 280


    elif(tıkla1==1):
        if (state == GLUT_DOWN and button == GLUT_RIGHT_BUTTON and mousey<=330 and mousey>=120 and mousex<=260 and mousex>=190):

            angle1 += 90
            yc1 +=1
            yatay1 = 1

        elif(state == GLUT_DOWN and button == GLUT_LEFT_BUTTON and mousey<=330 and mousey>=120 and mousex<=260 and mousex>=190):
                tıkla1 += 1
                w1 += 140

    elif(tıkla1==2):

        if (state == GLUT_DOWN and button == GLUT_RIGHT_BUTTON and mousey <= 540 and mousey >= 400 and mousex <= 120 and mousex >= 50):

            angle3 += 90
            yatay3 = 1

        if(yatay3==1):
            if (state == GLUT_DOWN and button == GLUT_LEFT_BUTTON and mousey <= 540 and mousey >= 400 and mousex <= 120 and mousex >= 50):

                tıkla1 += 1
                h3 += 350
                w3 += 280
        elif(yatay3==0):
            if (state == GLUT_DOWN and button == GLUT_LEFT_BUTTON and mousey <= 540 and mousey >= 400 and mousex <= 120 and mousex >= 50):

                tıkla1 += 1
                h3 += 280
                w3 += 280


    elif (tıkla1 == 3):

        if (state == GLUT_DOWN and button == GLUT_RIGHT_BUTTON and mousey <= 540 and mousey >= 400 and mousex <= 260 and mousex >= 190):
            angle4 += 90
            yatay4 = 1

        if (yatay4 == 0):


            if (state == GLUT_DOWN and button == GLUT_LEFT_BUTTON and mousey <= 540 and mousey >= 400 and mousex <= 260 and mousex >= 190):

                tıkla1 += 1
                w4 += 140
                h4 += 280

        elif (yatay4 == 1):

            if (state == GLUT_DOWN and button == GLUT_LEFT_BUTTON and mousey <= 540 and mousey >= 400 and mousex <= 260 and mousex >= 190):

                tıkla1 += 1
                w4 += 140
                h4 += 350

    elif (tıkla1 == 4):

        if (state == GLUT_DOWN and button == GLUT_RIGHT_BUTTON and mousey <= 890 and mousey >= 610 and mousex <= 120 and mousex >= 50):
            angle5 += 90
            yatay5 = 1

        if (yatay5 == 0):

            if (state == GLUT_DOWN and button == GLUT_LEFT_BUTTON and mousey <= 890 and mousey >= 610 and mousex <= 120 and mousex >= 50):
                tıkla1 += 1
                w5 += 280
                h5 += 490

        elif (yatay5 == 1):

            if (state == GLUT_DOWN and button == GLUT_LEFT_BUTTON and mousey <= 890 and mousey >= 610 and mousex <= 120 and mousex >= 50):
                tıkla1 += 1
                w5 += 280
                h5 += 560


    glutPostRedisplay()

def keyboardfunction(*args):#gemi hareket ettirme ve yerlestirme fonksiyonu

    global listx,listy,listt,xc1,yc1,xc2,yc2,w1,h1,w2,h2,w3,h3,w4,h4,yerlestirmesayisi1,yatay1,yatay2,gemi,w5,h5,oyuncu
    global dw1,dh1,oynandi
    if (yerlestirmesayisi1==1):

      if(yatay1==0):

        if (w1 <= 610):
              if args[0] == b"d":
                  w1 += 70
                  listx[0] += 1

        if (w1 >= 120):
              if args[0] == b"a":
                  w1 += -70
                  listx[0] -= 1
        if (h1 <= 340):
              if args[0] == b"w":
                  h1 += 70
                  listy[0] += 1
        if (h1 >= -120):
              if args[0] == b"s":
                  h1 += -70
                  listy[0] -= 1

        if args[0] == b"y":



            listt.insert(0,[listx[len(listx)-1],listy[len(listy)-1]])
            listt.insert(1,[listx[len(listx)-1],listy[len(listy)-1]-1])
            listt.insert(2,[listx[len(listx) - 1], listy[len(listy)-1]-2])

            listx.clear()
            listy.clear()
            listx.append(0)
            listy.append(0)
            yerlestirmesayisi1 += 1

      if (yatay1 == 1):


          if (w1 <= 480):
                  if args[0] == b"d":
                      w1 += 70
                      listx[0] += 1

          if (w1 >= 120):
                  if args[0] == b"a":
                      w1 += -70
                      listx[0] -= 1
          if (h1 <= 340):
                  if args[0] == b"w":
                      h1 += 70
                      listy[0] += 1
          if (h1 >= -260):
                  if args[0] == b"s":
                      h1 += -70
                      listy[0] -= 1
          if args[0] == b"y":



              listt.insert(0, [listx[len(listx) - 1], listy[len(listy) - 1]])
              listt.insert(1, [listx[len(listx) - 1]+1, listy[len(listy) - 1]])
              listt.insert(2, [listx[len(listx) - 1]+2, listy[len(listy) - 1]])

              listx.clear()
              listy.clear()
              listx.append(0)
              listy.append(0)
              yerlestirmesayisi1 += 1



    elif (yerlestirmesayisi1 == 0):

            if (yatay2 == 0):


                    if (w2 <= 610):
                        if args[0] == b"d":
                            w2 += 70
                            listx[0] += 1

                    if (w2 >= 120):
                        if args[0] == b"a":
                            w2 += -70
                            listx[0] -= 1
                    if (h2 <= 340):
                        if args[0] == b"w":
                            h2 += 70
                            listy[0] += 1
                    if (h2 >= -120):
                        if args[0] == b"s":
                            h2 += -70
                            listy[0] -= 1

                    if args[0] == b"y":


                        listt.insert(0, [listx[len(listx) - 1], listy[len(listy) - 1]])
                        listt.insert(1, [listx[len(listx) - 1], listy[len(listy) - 1] - 1])
                        listt.insert(2, [listx[len(listx) - 1], listy[len(listy) - 1] - 2])
                        listx.clear()
                        listy.clear()
                        listx.append(0)
                        listy.append(0)

                        yerlestirmesayisi1 += 1

            if (yatay2 == 1):


                    if (w2 <= 480):
                        if args[0] == b"d":
                            w2 += 70
                            listx[0] += 1

                    if (w2 >= 120):
                        if args[0] == b"a":
                            w2 += -70
                            listx[0] -= 1
                    if (h2 <= 340):
                        if args[0] == b"w":
                            h2 += 70
                            listy[0] += 1
                    if (h2 >= -260):
                        if args[0] == b"s":
                            h2 += -70
                            listy[0] -= 1

                    if args[0] == b"y":

                        listt.insert(0, [listx[len(listx) - 1], listy[len(listy) - 1]])
                        listt.insert(1, [listx[len(listx) - 1] + 1, listy[len(listy) - 1]])
                        listt.insert(2, [listx[len(listx) - 1] + 2, listy[len(listy) - 1]])
                        listx.clear()
                        listy.clear()
                        listx.append(0)
                        listy.append(0)

                        yerlestirmesayisi1 += 1

    elif (yerlestirmesayisi1 == 2):

            if (yatay3 == 0):


                    if (w3 <= 610):
                        if args[0] == b"d":
                            w3 += 70
                            listx[0] += 1

                    if (w3 >= 120):
                        if args[0] == b"a":
                            w3 += -70
                            listx[0] -= 1
                    if (h3 <= 340):
                        if args[0] == b"w":
                            h3 += 70
                            listy[0] += 1
                    if (h3 >= -190):
                        if args[0] == b"s":
                            h3 += -70
                            listy[0] -= 1

                    if args[0] == b"y":


                        listt.insert(0, [listx[len(listx) - 1], listy[len(listy) - 1]])
                        listt.insert(1, [listx[len(listx) - 1], listy[len(listy) - 1] - 1])

                        listx.clear()
                        listy.clear()
                        listx.append(0)
                        listy.append(0)

                        yerlestirmesayisi1 += 1

            if (yatay3 == 1):


                    if (w3 <= 560):
                        if args[0] == b"d":
                            w3 += 70
                            listx[0] += 1

                    if (w3 >= 120):
                        if args[0] == b"a":
                            w3 += -70
                            listx[0] -= 1
                    if (h3 <= 410):
                        if args[0] == b"w":
                            h3 += 70
                            listy[0] += 1
                    if (h3 >= -190):
                        if args[0] == b"s":
                            h3 += -70
                            listy[0] -= 1

                    if args[0] == b"y":


                        listt.insert(0, [listx[len(listx) - 1], listy[len(listy) - 1]])
                        listt.insert(1, [listx[len(listx) - 1] + 1, listy[len(listy) - 1]])

                        listx.clear()
                        listy.clear()
                        listx.append(0)
                        listy.append(0)

                        yerlestirmesayisi1 += 1

    elif(yerlestirmesayisi1 == 3):

            if (yatay4 == 0):

                if (w4 <= 610):
                    if args[0] == b"d":
                        w4 += 70
                        listx[0] += 1

                if (w4 >= 120):
                    if args[0] == b"a":
                        w4 += -70
                        listx[0] -= 1
                if (h4 <= 300):
                    if args[0] == b"w":
                        h4 += 70
                        listy[0] += 1
                if (h4 >= -190):
                    if args[0] == b"s":
                        h4 += -70
                        listy[0] -= 1

                if args[0] == b"y":


                    listt.insert(0, [listx[len(listx) - 1], listy[len(listy) - 1]])
                    listt.insert(1, [listx[len(listx) - 1], listy[len(listy) - 1] - 1])
                    listx.clear()
                    listy.clear()
                    listx.append(0)
                    listy.append(0)

                    yerlestirmesayisi1 += 1

            if (yatay4 == 1):

                if (w4 <= 550):
                    if args[0] == b"d":
                        w4 += 70
                        listx[0] += 1

                if (w4 >= 120):
                    if args[0] == b"a":
                        w4 += -70
                        listx[0] -= 1
                if (h4 <= 370):
                    if args[0] == b"w":
                        h4 += 70
                        listy[0] += 1
                if (h4 >= -190):
                    if args[0] == b"s":
                        h4 += -70
                        listy[0] -= 1

                if args[0] == b"y":


                    listt.insert(0, [listx[len(listx) - 1], listy[len(listy) - 1]])
                    listt.insert(1, [listx[len(listx) - 1] + 1, listy[len(listy) - 1]])
                    listx.clear()
                    listy.clear()
                    listx.append(0)
                    listy.append(0)

                    yerlestirmesayisi1 += 1


    elif (yerlestirmesayisi1 == 4):

        if (yatay5 == 0):

            if (w5 <= 610):
                if args[0] == b"d":
                    w5 += 70
                    listx[0] += 1

            if (w5 >= 120):
                if args[0] == b"a":
                    w5 += -70
                    listx[0] -= 1
            if (h5 <= 300):
                if args[0] == b"w":
                    h5 += 70
                    listy[0] += 1
            if (h5 >= -50):
                if args[0] == b"s":
                    h5 += -70
                    listy[0] -= 1

            if args[0] == b"y":



                listt.insert(0, [listx[len(listx) - 1], listy[len(listy) - 1]])
                listt.insert(1, [listx[len(listx) - 1], listy[len(listy) - 1] - 1])
                listt.insert(2, [listx[len(listx) - 1], listy[len(listy) - 1] - 2])
                listt.insert(3, [listx[len(listx) - 1], listy[len(listy) - 1] - 3])
                listx.clear()
                listy.clear()
                listx.append(0)
                listy.append(0)

                yerlestirmesayisi1 += 1

                for i in range(14):
                    listt.pop()
                yapayzeka()
        if (yatay5 == 1):

            if (w5 <= 410):
                if args[0] == b"d":
                    w5 += 70
                    listx[0] += 1

            if (w5 >= 120):
                if args[0] == b"a":
                    w5 += -70
                    listx[0] -= 1
            if (h5 <= 370):
                if args[0] == b"w":
                    h5 += 70
                    listy[0] += 1
            if (h5 >= -190):
                if args[0] == b"s":
                    h5 += -70
                    listy[0] -= 1

            if args[0] == b"y":


                listt.insert(0, [listx[len(listx) - 1], listy[len(listy) - 1]])
                listt.insert(1, [listx[len(listx) - 1] + 1, listy[len(listy) - 1]])
                listt.insert(2, [listx[len(listx) - 1] + 2, listy[len(listy) - 1]])
                listt.insert(3, [listx[len(listx) - 1] + 3, listy[len(listy) - 1]])
                listx.clear()
                listy.clear()
                listx.append(0)
                listy.append(0)
                yerlestirmesayisi1 += 1
                for i in range(13):

                    listt.pop()
                yapayzeka()
#deneme karesi
    elif(yerlestirmesayisi1 == 5):

        if (dw1 <= 1340):
            if args[0] == b"d":
                dw1 += 70
                listdx[0] += 1

        if (dw1 >= 800):
            if args[0] == b"a":
                dw1 += -70
                listdx[0] -= 1
        if (dh1 <= 384):
            if args[0] == b"w":
                dh1 += 70
                listdy[0] += 1
        if (dh1 >= -190):
            if args[0] == b"s":
                dh1 += -70
                listdy[0] -= 1

        if (args[0] == b"y"):



            listdt.insert(0, [listdx[len(listx) - 1], listdy[len(listy) - 1]])

            oynandi = 1
            listdt.pop()


    glutPostRedisplay()

def main():

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(1800,900)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b"Amiral Batti")
    glutDisplayFunc(drawfunc)
    glutMouseFunc(mousefunc)
    glutPassiveMotionFunc(mouseMotion)
    glutKeyboardFunc(keyboardfunction)
    InitGL()
    glutMainLoop()


main()
