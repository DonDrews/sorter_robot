from PIL import Image
from PIL import ImageChops
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
import os, os.path


def importSets():
	imgs = []
	valid_images = [".jpg",".gif",".png",".tga"]
	path = '/home/alex/Desktop/sorter_robot/set_symbols'
	
	for f in os.listdir(path):
		ext = os.path.splitext(f)[1]
		if ext.lower() not in valid_images:
			continue

		imgs.append(Image.open(os.path.join(path,f)))
	
	return imgs

def setUp(imageA, fileName):
	new = (400, 400) # This will have to be adjusted once we are on the real sorter
	fileType = '.png'

	# resize the images
	imageA = imageA.resize(new)

	# grey scale
	imageA = imageA.convert('L')

	# threshold scale
	imageA = imageA.point(lambda x: x >= 128 and 255, "1")

	# save after resize
	imageA.save(str(fileName)+fileType)

def setUpTest(imageA):
	new = (400, 400) # This will have to be adjusted once we are on the real sorter
	fileType = '.png'

	# resize the images
	imageA = imageA.resize(new)

	# grey scale
	imageA = imageA.convert('L')

	# threshold scale
	imageA = imageA.point(lambda x: x >= 128 and 255, "1")

	# save after resize
	imageA.save('cropCardSet.png')

 
def calcDiff(imageA, imageB):
    # calculate the root-mean-square difference between two images
    dif = ImageChops.difference(imageA, imageB)
    return [sqrt(np.mean(np.square(np.array(dif)))), np.mean(np.array(dif))]

def main():
	im = Image.open("cropCardSet.png")
	compList = list()
	
	setList = importSets()

	for i, value in enumerate(setList):
		setUp(value, i)

	setUpTest(im)
	im = Image.open("cropCardSet.png")

	for i in range(len(setList)):
		try:
			tempIm = Image.open(str(i)+'.png')
		except:
			break

		compList.append(calcDiff(im, tempIm))

	print(compList)

	plt.plot(compList)
	plt.ylabel('Card Match (Lower is better)')
	plt.xticks([0,1,2,3,4], ['Card 0', 'Card 1', 'Card 2', 'Card 3', 'Card 4'], rotation ='horizontal')
	plt.xlabel('Card Number')
	plt.show()

if __name__=="__main__":
    main()








