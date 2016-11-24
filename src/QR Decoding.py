#
#     Copyright (C) 2016  Siddharth Saxena
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
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
