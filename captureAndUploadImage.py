import cv2
import dropbox
import time
import random
starttime = time.time()
def takesnapshot():
    number = random.randint(0, 100)
    videocaptureobject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = videocaptureobject.read()
        image_name = "img"+str(number)+".png"
        cv2.imwrite(image_name, frame)
        starttime = time.time
        result = False
    return image_name
    print("Snapshot Taken")
    videocaptureobject.release()
    cv2.destroyAllWindows()
def upload_file(image_name):
    access_token = "7yXZ3kKioywAAAAAAAAAAayQi0eQZFm_J5XHqNa4V0OkV-KG-JZUZaoI-6BxBwJW"
    file = image_name
    file_from = file
    file_to = "/testFolder"+ (image_name)
    dbx = dropbox.Dropbox(access_token)
    with open (file_from, "rb")as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print("File Uploaded")
def main():
    while(True):
        if((time.time()-starttime)>=5):
            name = takesnapshot()
            upload_file(name)
main()