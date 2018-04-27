import urllib
import glob
import os
import cv2
import time
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

intersections = {'AmbCong':'Ambassador @ Congress', 'AmbCurr':'Ambassador @ Curran', 'AmbDull':'Ambassador @ Dulles', 'AmbEras':'Ambassador @ Eraste Landry', 'AmbBous':'Ambassador @ Boustany', 'AmbGuil':'Ambassador @ Guilbeau', 'AmbI10R':'Ambassador @ I10 Ramp', 'AmbKali':'Ambassador @ Kaliste Saloom', 'AmbRobl':'Ambassador @ Robley', 'AmbSett':'Ambassador @ Settlers Trace', 'AmbWill':'Ambassador @ Willow'} 

badImage = Image.open("JUNK.jpg")
badImage_sharp = badImage.filter( ImageFilter.SHARPEN )
r,g,b = badImage_sharp.split()
print(r)
print(g)
print(b)


for key in intersections:
	if not os.path.exists(key):
		os.makedirs(key)
i = 0
while i<5:
	i+=1
	dtime = str(datetime.now())
	urllib.urlretrieve(baseURL+AmbCongURL, "AmbCong/AmbCong"+dtime+".jpg")
	urllib.urlretrieve(baseURL+AmbCurrURL, "AmbCurr/AmbCurr"+dtime+".jpg")
	urllib.urlretrieve(baseURL+AmbDullURL, "AmbDull/AmbDull"+dtime+".jpg")
	urllib.urlretrieve(baseURL+AmbErasURL, "AmbEras/AmbEras"+dtime+".jpg")
	urllib.urlretrieve(baseURL+AmbBousURL, "AmbBous/AmbBrous"+dtime+".jpg")
	urllib.urlretrieve(baseURL+AmbGuilURL, "AmbGuil/AmbGuil"+dtime+".jpg")
	urllib.urlretrieve(baseURL+AmbI10RURL, "AmbI10R/AmbI10R"+dtime+".jpg")
	urllib.urlretrieve(baseURL+AmbKaliURL, "AmbKali/AmbKali"+dtime+".jpg")
	urllib.urlretrieve(baseURL+AmbRoblURL, "AmbRobl/AmbRobl"+dtime+".jpg")
	urllib.urlretrieve(baseURL+AmbSettURL, "AmbSett/AmbSett"+dtime+".jpg")
#	urllib.urlretrieve(baseURL+AmbVertURL, "AmbVert/AmbVert"+dtime+".jpg")
	urllib.urlretrieve(baseURL+AmbWillURL, "AmbWill/AmbWill"+dtime+".jpg")

for key in intersections:
	images = glob.glob(key+'/*.jpg')
	imagelist = []
	for image in images:
		imagelist.append(image)
	imagelist.sort()
	for image in imagelist:
		if image != "JUNK.jpg":
			testImage = Image.open(image)
			if testImage != badImage:
				testImage_sharp = testImage.filter( ImageFilter.SHARPEN )
				r2,g2,b2 = testImage_sharp.split()
				if r==r2 and g==g2 and b==b2:
					print("JANK")
					os.remove(image)
				else: 
					print(image)
					img = cv2.imread(image)
					gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
					gray = np.float32(gray)
					dst = cv2.cornerHarris(gray,2,3,0.04)
					dst = cv2.dilate(dst,None)
					img[dst>0.01*dst.max()]=[0,0,255]
					cv2.imshow('dst',img)
				if cv2.waitKey(100) & 0xff == 27: 
					time.sleep(0.8)
					cv2.destroyAllWindows()