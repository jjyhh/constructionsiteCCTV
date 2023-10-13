import cv2
 
# 이미지 읽기
img = cv2.imread('test.jpg', 1)
 
# 이미지 화면에 표시
cv2.imshow('Test Image', img)
cv2.waitKey(0)
# 이미지 윈도우 삭제
cv2.destroyAllWindows()
 
# 이미지 다른 파일로 저장
cv2.imwrite('test2.png', img)