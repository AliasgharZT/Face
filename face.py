from matplotlib import pyplot 
import cv2 

img=cv2.imread('az.jpg') 
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) 
model=cv2.CascadeClassifier('model.xml')

face=model.detectMultiScale(img) 

x=face[0][0]
y=face[0][1]
a=face[0][2]
b=face[0][3]

img=cv2.rectangle(img,(x,y),(x+a,y+b),(157,200,91),2)

pyplot.imshow(img) 
