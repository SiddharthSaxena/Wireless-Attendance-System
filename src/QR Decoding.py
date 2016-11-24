from PIL import Image
import cv2
import zbarlight

cap = cv2.VideoCapture(0)


# noinspection PyPep8Naming
def qrCheck(image):
    try:
        code = zbarlight.scan_codes('qrcode', image)
        return code
    except AssertionError:
        return


def output(string):
    if string:
        string = str(string)
        string = string.split("'")
        print(string[1])
        return

while True:
    # Capture frame-by-frame.
    ret, frame = cap.read()

    # Convert incoming frames into gray scale.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Convert image frames into numpy array.
    image = Image.fromarray(gray)
    decoded = qrCheck(image)
    output(decoded)

# Display the resulting frame.
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture.
cap.release()
cv2.destroyAllWindows()
