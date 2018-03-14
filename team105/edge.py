import cv2
image = cv2.imread('C:\Users\HP\Desktop\team105\dataSet\image2.png')
image2 = cv2.imread('C:\Users\HP\Desktop\team105\dataSet\imgtest_image2.png')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(gray_image, (7, 7), 0)

gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
blurred_image2 = cv2.GaussianBlur(gray_image2, (7, 7), 0)

#canny = cv2.Canny(blurred_image, 10, 30)
#canny2 = cv2.Canny(blurred_image2, 10, 30)

image3 = gray_image - gray_image2
#canny = cv2.Canny(image3, 10, 30)


cv2.imshow("image1", image)
cv2.imshow("image2", image2)

cv2.imshow("Canny with low thresholds", image3)
#cv2.imshow("Canny with high thresholds", canny2)
# cv2.imshow('Test image',image)


cv2.waitKey(0)
cv2.destroyAllWindows()

