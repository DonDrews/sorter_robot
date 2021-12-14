from PIL import Image
from PIL import ImageChops
from math import sqrt
import numpy as np
import cv2

def setUp(imageA, imageB, imageC):
	new = (400, 400) # This will have to be adjusted once we are on the real sorter

	# resize the images
	imageA = imageA.resize(new)
	imageB = imageB.resize(new)
	imageC = imageC.resize(new)

	imageA = imageA.convert('L')
	imageB = imageB.convert('L')
	imageC = imageC.convert('L')

	imageA = imageA.point(lambda v: v >= 128 and 255, "1")
	imageB = imageB.point(lambda v: v >= 128 and 255, "1")
	imageC = imageC.point(lambda v: v >= 128 and 255, "1")

	# save after resize
	imageA.save("temp.png")
	imageB.save("temp2.png")
	imageC.save("temp3.png")
 

def calcDiff(imageA, imageB):
    # calculate the root-mean-square difference between two images
    dif = ImageChops.difference(imageA, imageB)
    return [sqrt(np.mean(np.square(np.array(dif)))), np.mean(np.array(dif))]

def main():
	im = Image.open("cropCardSet.png")
	im2 = Image.open("mid-c.png")
	im3 = Image.open("theros.png") # the test comparison set

	setUp(im, im2, im3)
	
	im = Image.open("temp.png")
	im2 = Image.open("temp2.png")
	im3 = Image.open("temp3.png")

	compSame = calcDiff(im, im2)
	compDiff = calcDiff(im, im3)

	print("Same set symbol comp: ", compSame)
	print("Different set symbol comp: ", compDiff)
	
if __name__=="__main__":
    main()








