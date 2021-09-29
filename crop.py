from PIL import Image
import cv2

im = Image.open('card.png')

im_cropName = im.crop((60, 30, 950, 200))
im_cropName.save('cropCardName.png', quality=95)

width, height = im.size   # Get dimensions
#print(width, height)

#(left, top, right, bottom)
#im_cropSet = im.crop((996, 1131, 942, 1046))
im_cropSet = im.crop((1000, 945, 1128, 1044))
im_cropSet.save('cropCardSet.png', quality=95)

crop = cv2.imread('cropCardSet.png')
cv2.imshow("Cropped Set", crop)
cv2.waitKey(0)