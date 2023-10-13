import cv2
# import HandTrackingModule as htm
from cvzone.HandTrackingModule import HandDetector


# ----------------------------------------------------------------------------
camW, camH = 1280, 720

cap = cv2.VideoCapture(0)
cap.set(3, camW)
cap.set(4, camH)

# detector = htm.handDetector(detectionCon=0.8)
detector = HandDetector(detectionCon=0.8)
keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]]

def drawAll(img, buttonList):
    for button in buttonList:
    # Drawing and positioning
        x, y = button.pos
        w, h = button.size
        cv2.rectangle(img, button.pos, (x + w, y + h), (255, 0, 255), cv2.FILLED)
        cv2.putText(img, button.text, (x + 20, y + 65),
                cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
    return img

# Button Class
class Button():
    def __init__(self, pos, text, size=(85,85)):
        self.pos = pos
        self.size =size
        self.text =text

buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([100 * j + 50, 100 * i + 50], key))




while True:
    success, img = cap.read()
    # To find hands
    img = detector.findHands(img)
    # LandMark Points
    # lmList = detector.findPosition(img)
    print(lmList)
    lmList = detector.findPosition(img)
    bboxInfo = detector.findHands(img)
    #  Drawing all Buttons
    img = drawAll(img, buttonList)


    if lmList:
        for button in buttonList:
            x, y = button.pos
            w, h = button.size

            if x < lmList[8][0] < x+w:
                cv2.rectangle(img, button.pos, (x + w, y + h), (0, 225, 0), cv2.FILLED)
                cv2.putText(img, button.text, (x + 20, y + 65),
                            cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)


    cv2.imshow("Image", img)
    cv2.waitKey(1)