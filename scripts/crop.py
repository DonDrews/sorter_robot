from PIL import Image
import cv2

im = Image.open('poopy.png')

width, height = im.size   # Get dimensions
print(width, height)

im_cropName = im.crop((717, 165, 990, 291))
im_cropName.save('cropCardName.png', quality=95)

#(left, top, right, bottom)
im_crop = im.crop((1818, 1152, 1920, 1269))
im_crop.save('cropCardSet.png', quality=95)

im2 = Image.open('cropCardSet.png')
im2_crop = im2.crop((5, 25, 84, 91))
im2_crop.save('cropCardSet.png', quality=95)

crop = cv2.imread('cropCardSet.png')
cv2.imshow("Cropped Set", crop)
cv2.waitKey(0)

1920, 1269