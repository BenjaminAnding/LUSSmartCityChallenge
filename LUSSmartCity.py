import urllib
import glob
import os
import cv2
import numpy as np
from PIL import Image, ImageFilter
from datetime import datetime

baseURL = 'http://www.lafayettela.gov/tcams/getTCamera.aspx?ptzid='
AmbCongURL = '151'
AmbCurrURL = '210'
AmbDullURL = '149'
AmbErasURL = '148'
AmbBousURL = '181'
AmbGuilURL = '150'
AmbI10RURL = '185'
AmbKaliURL = '113'
AmbRoblURL = '153'
AmbSettURL = '213'
AmbVertURL = '188'
AmbWillURL = '186'



i = 0
while i<100:
	i+=1
	time = str(datetime.now())
	urllib.urlretrieve(baseURL+AmbCongURL, "AmbCong"+time+".jpg")
	urllib.urlretrieve(baseURL+AmbCurrURL, "AmbCurr"+time+".jpg")
	urllib.urlretrieve(baseURL+AmbDullURL, "AmbDull"+time+".jpg")
	urllib.urlretrieve(baseURL+AmbErasURL, "AmbEras"+time+".jpg")
	urllib.urlretrieve(baseURL+AmbBousURL, "AmbBous"+time+".jpg")
	urllib.urlretrieve(baseURL+AmbGuilURL, "AmbGuil"+time+".jpg")
	urllib.urlretrieve(baseURL+AmbI10RURL, "AmbI10R"+time+".jpg")
	urllib.urlretrieve(baseURL+AmbKaliURL, "AmbKali"+time+".jpg")
	urllib.urlretrieve(baseURL+AmbRoblURL, "AmbRobl"+time+".jpg")
	urllib.urlretrieve(baseURL+AmbSettURL, "AmbSett"+time+".jpg")
#	urllib.urlretrieve(baseURL+AmbVertURL, "AmbVert"+time+".jpg")
	urllib.urlretrieve(baseURL+AmbWillURL, "AmbWill"+time+".jpg")

	
badImage = Image.open("JUNK.jpg")
badImage.show()
badImage_sharp = badImage.filter( ImageFilter.SHARPEN )
r,g,b = badImage_sharp.split()
print(r)
print(g)
print(b)


images = glob.glob('*.jpg')

for image in images:
	if image != "JUNK.jpg":
		testImage = Image.open(image)
	if testImage != badImage:
		testImage_sharp = testImage.filter( ImageFilter.SHARPEN )
		r2,g2,b2 = testImage_sharp.split()
		if r==r2 and g==g2 and b==b2:
			print("JANK")
			os.remove(image)
		else: 
			print("Gucci")
			img = cv2.imread(image)
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			gray = np.float32(gray)
			dst = cv2.cornerHarris(gray,2,3,0.04)
			dst = cv2.dilate(dst,None)
			img[dst>0.01*dst.max()]=[0,0,255]
			cv2.imshow('dst',img)
			if cv2.waitKey(0) & 0xff == 27:
			    cv2.destroyAllWindows()
	