import cv2
import time
import HandTrackingModule as htm

#                 U2FuYWV2ZWdpZGluY2V5YXpkZW1pc3RpbS4=
pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmlist = detector.findPosition(img)
    if len(lmlist) != 0:
        print(str(lmlist[4]) + "Napim?")

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(31)), (10, 70),
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("sen aglion", img)
    cv2.waitKey(1)
