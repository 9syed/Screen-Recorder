import cv2
import pyautogui
import numpy as np

width, height = pyautogui.size()
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
output = cv2.VideoWriter('output.mkv', fourcc, 30.0, (width, height))

while True:
    image = pyautogui.screenshot()
    frame = np.array(image)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    output.write(frame)
    cv2.imshow('Screen Recorder', frame)

    if cv2.waitKey(1) == ord('q'):
        break

output.release()
cv2.destroyAllWindows()