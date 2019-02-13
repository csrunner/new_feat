# -*- coding:utf-8 -*-
__author__ = 'shichao'


import cv2

def display_from_file(path):

    cap = cv2.VideoCapture(path)
    while(1):
        # get a frame
        ret, frame = cap.read()
        # show a frame
        if ret:
            cv2.imshow("capture", frame)
            if cv2.waitKey(2) & 0xFF == ord('q'):
                break
        else:
            cap.release()
            cv2.destroyAllWindows()
            break

def display_from_camera():
    cap = cv2.VideoCapture(0)
    while (1):
        # get a frame
        ret, frame = cap.read()
        # show a frame
        if ret:
            cv2.imshow("capture", frame)
            if cv2.waitKey(2) & 0xFF == ord('q'):
                break
        else:
            cap.release()
            cv2.destroyAllWindows()
            break

def main():
    # path = r'C:\Users\cs_working\Downloads\ps1057.mp4'
    # display_from_file(path)
    display_from_camera()

if __name__ == '__main__':
    main()