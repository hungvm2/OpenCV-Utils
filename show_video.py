import cv2

vidcap = cv2.VideoCapture('http://127.0.0.1:8081')
# vidcap = cv2.VideoCapture('rtsp://test:abcd1234@10.84.130.40/h265/ch8/main/av_stream')
vidcap.set(3,640) #set frame width
vidcap.set(4,480) #set frame height
# vidcap = cv2.VideoCapture(args.get('video'))
while True:
    _,frame = vidcap.read()
    # frame = cv2.resize(frame, (640, 480))
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
vidcap.release()
cv2.destroyAllWindows()
