from pickletools import uint8
import cv2
import numpy as np

watermark_file = input("give the watermark path .. ")
image_file = input("give the image path .. ")

watermark = cv2.imread(watermark_file)

imag = cv2.imread(image_file)

#imag = cv2.resize(imag,(900,700),cv2.INTER_CUBIC)


gray_watermak = cv2.cvtColor(watermark,cv2.COLOR_BGR2GRAY)
gray_watermak= cv2.adaptiveThreshold(gray_watermak,255,cv2.THRESH_BINARY,cv2.ADAPTIVE_THRESH_MEAN_C,11,2)
invert = cv2.bitwise_not(gray_watermak)
print(np.quantile(invert,0.5))

img_h ,img_w ,_ = imag.shape


resized = cv2.resize(invert,(img_w,img_h),cv2.INTER_CUBIC)



#bordered = cv2.copyMakeBorder(resized,top+1,buttom,left+1,right,cv2.BORDER_CONSTANT,value=[0,0,0])
bordered = resized/255.0

imag[0:img_h,0:img_w,0] = np.abs(imag[0:img_h,0:img_w,0] -bordered*20)
imag[0:img_h,0:img_w,1] =np.abs(imag[0:img_h,0:img_w,1] - bordered*20)
imag[0:img_h,0:img_w,2] = np.abs(imag[0:img_h,0:img_w,2] - bordered*20)




cv2.imwrite("result2.png",imag)

cv2.imshow("file",resized)
cv2.imshow("",imag)
cv2.waitKey(0)



