import pyqrcode
import sys


def version():
    major = int(sys.version.strip().split('.')[0])
    return major


def encode(data):
    encoded = pyqrcode.create(data, error='Q', version=4, mode='binary')
    encoded.png('code.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
    return encoded

if version() == 2:
    code = raw_input('Enter the data to be converted into QR code: ')
    encode(code)
elif version() == 3:
    code = input('Enter the data to be converted into QR code: ')
    encode(code)
else:
    print('Unknown python version {}'.format(version()))
