import cv2
from cvzone.PoseModule import PoseDetector

cap = cv2.VideoCapture('Video.mp4')

detector = PoseDetector()
posList = []

while True:
    success, img = cap.read()

    if not success:
        break  # Exit the loop if there are no more frames

    img = detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img)

    if bboxInfo and lmList:  # Check if both bboxInfo and lmList are not empty
        lmString = ''
        for lm in lmList:
            lmString += f'{lm[1]},{img.shape[0] - lm[2]},{lm[3]},'
        posList.append(lmString)

    print(len(posList))

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('s'):
        with open("AnimationFile.txt", 'w') as f:
            f.writelines(["%s\n" % item for item in posList])

cap.release()
cv2.destroyAllWindows()
