from PIL import Image
import cv2
import zbarlight
import numpy


cap = cv2.VideoCapture(0)


def qrCheck(arg):
    # Check an image for a QR code, return as string.
    # file_path = '/home/siddharth/Desktop/code.png'
    # with open(file_path, 'rb') as image_file:
    #     image = Image.open(image_file)
    #     image.load()
    image_string = arg.tostring()
    try:
        code = zbarlight.scan_codes('qrcode', image_string)
        return code
    except AssertionError:
        return

while True:
    # Capture frame-by-frame.
    ret, frame = cap.read()

    # Our operations on the frame come here.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    decoded = qrCheck(gray)
    print(decoded)

# Display the resulting frame.
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture.
cap.release()
cv2.destroyAllWindows()
