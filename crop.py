from PIL import Image
import cv2

im = Image.open('card.png')

im_cropName = im.crop((60, 30, 950, 200))
im_cropName.save('cropCardName.png', quality=95)

width, height = im.size   # Get dimensions
left = 2 * width/4
top = 2 * height/3
right = 3 * width/4
bottom = 3 * height/4

im_cropSet = im.crop((left, top, right, bottom))
im_cropSet.save('cropCardSet.png', quality=95)

crop_name = cv2.imread('cropCardSet.png')
cv2.imshow("Cropped Set", crop_name)
cv2.waitKey(0)