import cv2
import math


img = cv2.imread("7.jpg")
img=cv2.resize(img,(0,0),fx=0.5,fy=0.5,interpolation=cv2.INTER_NEAREST)  #修改图片的尺寸
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Canny边缘检测
edges = cv2.Canny(img, 180,220)

# 二值化后找边缘
ret ,thresh=cv2.threshold(gray,0,255,cv2.THRESH_OTSU)
# ret, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
print(ret)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# contours,hierarchy=cv2.findContours(edges,1,2)


# print(len(contours))
# print(hierarchy)
# imag = cv2.drawContours(img,contours=contours,contourIdx=-1,color=(0,0,255),3)
imag = cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
# print(contours)

#椭圆
for cnt in contours:
    try:
        ellip = cv2.fitEllipse(cnt)
        print(ellip)
        #(x,y),(MA,ma),angle
        imag = cv2.ellipse(imag,ellip,(0,255,0),2)
        #画长宽
        res_ellipse = ellip
        ell_center_x = int(res_ellipse[0][0])
        ell_center_y = int(res_ellipse[0][1])

        ell_h_point1_x = int(ell_center_x - 0.5 * res_ellipse[1][0] * math.cos(res_ellipse[2] / 180 * math.pi))
        ell_h_point1_y = int(ell_center_y - 0.5 * res_ellipse[1][0] * math.sin(res_ellipse[2] / 180 * math.pi))
        ell_h_point2_x = int(ell_center_x + 0.5 * res_ellipse[1][0] * math.cos(res_ellipse[2] / 180 * math.pi))
        ell_h_point2_y = int(ell_center_y + 0.5 * res_ellipse[1][0] * math.sin(res_ellipse[2] / 180 * math.pi))

        ell_w_point1_x = int(ell_center_x - 0.5 * res_ellipse[1][1] * math.sin(res_ellipse[2] / 180 * math.pi))
        ell_w_point1_y = int(ell_center_y + 0.5 * res_ellipse[1][1] * math.cos(res_ellipse[2] / 180 * math.pi))
        ell_w_point2_x = int(ell_center_x + 0.5 * res_ellipse[1][1] * math.sin(res_ellipse[2] / 180 * math.pi))
        ell_w_point2_y = int(ell_center_y - 0.5 * res_ellipse[1][1] * math.cos(res_ellipse[2] / 180 * math.pi))

        cv2.line(imag, (ell_h_point1_x, ell_h_point1_y), (ell_h_point2_x, ell_h_point2_y), (0, 255, 255), thickness=2)
        cv2.line(imag, (ell_w_point1_x, ell_w_point1_y), (ell_w_point2_x, ell_w_point2_y), (0, 255, 255), thickness=2)

    except BaseException as e:
        print("null")

# 显示
# cv2.namedWindow("imag",cv2.WINDOW_NORMAL)
# cv2.imshow("thresh", thresh)
# cv2.imshow("edges", edges)
cv2.imshow("imag", imag)
# cv2.imshow('imeg', imeg)
# cv2.imshow('edges', edges)
cv2.waitKey(0)
# cv2.destroyAllWindows()
