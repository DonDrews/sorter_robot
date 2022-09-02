from PIL import Image, ImageChops
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
import os, os.path

def importSets():
	imgs = dict()
	valid_format = [".png"]
	path = 'set_symbols' # Swap once on the PI
	
	for f in os.listdir(path):
		ext = os.path.splitext(f)[1]
		if ext.lower() not in valid_format:
			continue

		imgs[f] = Image.open(os.path.join(path,f))
	
	return imgs

def setUp(imageName, image): # Set up for the comparison image
	new = (400, 400) # This will have to be adjusted once the PI

	# Resize the images
	image = image.resize(new)

	# Grey scale
	image = image.convert('L')

	# Threshold scale
	image = image.point(lambda x: x >= 128 and 255, "1")

	path = "edited_images/" + imageName

	# Save after resize
	image.save(path, "png")
 
def calcDiff(imageA, imageB):
    # Calculate the root-mean-square difference between two images
    dif = ImageChops.difference(imageA, imageB)
    return [sqrt(np.mean(np.square(np.array(dif)))), np.mean(np.array(dif))]

def main():
	compList = list()
	graphAxis = list()
	counterList = list()
	counter = -1 # Zero based indexing
	sep = '.'
	im = Image.open("cropCardSet.png")

	setUp("cropCardSet.png", im)
	im = Image.open("cropCardSet.png")

	setList = importSets()

	for i in setList:
		setUp(i, setList[i]) # i is card name, setList[i] is the image

		try:
			tempIm = Image.open("edited_images/"+i)
		except:
			break

		counter += 1
		counterList.append(counter)
		graphAxis.append(str(i).split(sep, 1)[0])
		compList.append(calcDiff(im, tempIm))

	plt.plot(compList)
	plt.ylabel('Card Match (Lower is better)')
	plt.xticks(counterList, graphAxis, rotation ='horizontal')
	plt.xlabel('Set')
	plt.show()

if __name__=="__main__":
    main()