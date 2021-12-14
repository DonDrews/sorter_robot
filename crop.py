from PIL import Image
import cv2

im = Image.open('MID.png')

width, height = im.size   # Get dimensions
print(width, height)

#im_cropName = im.crop((286, 820, 1293, 1001))
#im_cropName.save('cropCardName.png', quality=95)

#(left, top, right, bottom)
im_crop = im.crop((1810, 2145, 1997, 2316))
im_crop.save('cropCardSet.png', quality=95)

im2 = Image.open('cropCardSet.png')
im2_crop = im2.crop((34, 17, 173, 145))
im2_crop.save('cropCardSet.png', quality=95)

crop = cv2.imread('cropCardSet.png')
cv2.imshow("Cropped Set", crop)
cv2.waitKey(0)