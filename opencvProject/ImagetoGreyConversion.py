import cv2
#Read image from the directory
img = cv2.imread("index.jpeg")
#print(img)
#print(cv2.COLOR_BAYER_RG2BGR)
#print(cv2.cvtColor(img,cv2.COLOR_BAYER_RG2GRAY))
#Convert an image from RGB TO GRAY Code
grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print("Gray Color values",grayImg)
#Inversion of image-> to negative image
invImg = 255 - grayImg
print("Inversion image values",invImg)

blurredImg = cv2.GaussianBlur(invImg,(21,21),0)
print("Blurred Image Values",blurredImg)
invBlurImg = 255 - blurredImg
print("Inversion Blurred Image Values",invBlurImg)
pensketch = cv2.divide(grayImg,invBlurImg,scale=256.0)

cv2.imshow("Original image of Lord Shiva",img)
cv2.imshow("Pencil sketch image of Lord Shiva",pensketch)
cv2.waitKey(0)
