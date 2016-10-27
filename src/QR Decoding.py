from PIL import Image
import cv2
import zbarlight

cap = cv2.VideoCapture(0)


def qr(image):
    try:
        code = zbarlight.scan_codes('qrcode', image)
        return code
    except AssertionError:
        return

while True:
    # Capture frame-by-frame.
    ret, frame = cap.read()

    # Convert incoming frames into gray scale.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Convert image frames into numpy array.
    image = Image.fromarray(gray)
    decoded = qr(image)
    print(decoded)

# Display the resulting frame.
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture.
cap.release()
cv2.destroyAllWindows()
