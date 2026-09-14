import cv2
import numpy as np
image=cv2.imread('image.png')
if image is None:
    print("Image is not found")
    exit()

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
print("Choose an option:")
print("1. apply Guassian Blur")
print("2.Apply medain blow")
print("3. Canny Edge detection")
print("4.Sobel Edge detection")
print("5. Laplacian Edge detction")
print("6.Exit")

while True:
    choice=int(input("Enter a choice"))
    if choice==1:
        blur=cv2.GaussianBlur(gray,(5,5),0)
        cv2.imshow("Guassian Blur",blur)

    elif choice==2:
        median=cv2.medianBlur(gray,5)
        cv2.imshow("Median Blur",median)

    elif choice==3:
        edges=cv2.Canny(gray,100,200)
        cv2.imshow("Canny Edge Detection",edges)

    elif choice==4:
        sobelx=cv2.Sobel(gray,cv2.CV_16F,1,0,ksize=5)
        sobely=cv2.Sobel(gray,cv2.CV_16F,0,1,ksize=5)
        sobel=cv2.magnitude(sobelx,sobely)
        cv2.imshow("Sobel Edge detection",sobel)

    elif choice==5:
        laplacian =cv2.Laplacian(gray,cv2.CV_16F)
        cv2.imshow("LAplacian Edge Detectiion",laplacian)

    elif choice==6:
        break
    else:
        print("Invalid option try again")
cv2.destroyAllWindows()