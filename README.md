# QR Encoder/Decoder
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg?maxAge=3600&&style=flat)](https://github.com/SiddharthSaxena/Wireless-Attendance-System)&nbsp;&nbsp;[![Github Release](https://img.shields.io/badge/version-v1.0-red.svg?maxAge=3600&&style=flat)](https;//github.com/SiddharthSaxena/Wireless-Attendance-System/releases/tag/v1.0)&nbsp;&nbsp;[![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg?maxAge=3600&&style=flat)](https://github.com/SiddharthSaxena/Wireless-Attendance-System/blob/master/LICENSE)

Minor/Major Project.

---

* [Requirements](#requirements)
* [Usage](#usage)
* [License](#license)
* [Preview](#preview)

---

### Requirements

* **Python 2 or 3**.

* Python 2 package **zbar**. `sudo pip install zbar`

* Python3 packages **zbarlight**, **numpy**, **pyqrcode**, **pypng**. `sudo pip3 install zbarlight numpy pyqrcode pypng`

* **OpenCV 2 or 3**.

#### For Linux users:

* Install **zbar** developmental headers. `sudo apt-get install libzbar0 libzbar-dev`

#### For Windows users:

* Install **zbar** developmental headers from [here](https://sourceforge.net/projects/zbarw/).

#### For Mac users:

* Install **zbar** developmental headers. `brew install zbar`

---

### Usage

#### QR Encoding

* From Terminal, run `python QR\ Encoding.py` (for Python 2) or `python3 QR\ Encoding.py` (for Python3).

* Enter data to be converted to QR code.

* The default error control value for creating QR codes is 'Q'. You can change this value if you want higher error control capacity. 

#### QR Decoding

* From Terminal, run `python QR\ Decoding.py` (for Python 2) or `python3 QR\ Decoding.py` (for Python3). 

* A camera window will pop up. Bring the QR code to be decoded near the camera.

* The decoded output will be shown in the terminal window.

* Press 'Q' to quit when you are done.

---

### License

GNU General Public License v3 (GPLv3). See the [LICENSE](https://github.com/SiddharthSaxena/PyCurrency-Converter/blob/master/LICENSE) file for full details.

---

### Preview

<img src="http://www.siddharthsaxena.weebly.com/files/theme/QRED.png" id="preview">
