from PIL import Image
import cv2

im = Image.open('cmdr.png')

width, height = im.size   # Get dimensions
print(width, height)

#im_cropName = im.crop((286, 820, 1293, 1001))
#im_cropName.save('cropCardName.png', quality=95)

#(left, top, right, bottom)
im_cropSet = im.crop((1777, 2178, 1953, 2327))
im_cropSet.save('cropCardSet.png', quality=95)

crop = cv2.imread('cropCardSet.png')
cv2.imshow("Cropped Set", crop)
cv2.waitKey(0)