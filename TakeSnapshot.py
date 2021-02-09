import cv2
def takesnapshot():
    videocapture = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = videocapture.read()
        cv2.imwrite("newpicture1.jpg", frame)
        result = False
    videocapture.release()
    cv2.destroyAllWindows()
takesnapshot()