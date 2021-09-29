from PIL import Image
import cv2

im = Image.open('card.png')

width, height = im.size   # Get dimensions
print(width, height)

im_cropName = im.crop((60, 30, 950, 200))
im_cropName.save('cropCardName.png', quality=95)

#(left, top, right, bottom)
im_cropSet = im.crop((1000, 945, 1128, 1044))
im_cropSet.save('cropCardSet.png', quality=95)

crop = cv2.imread('cropCardName.png')
cv2.imshow("Cropped Set", crop)
cv2.waitKey(0)