#!/usr/bin/python3
import pyqrcode

code = input('Enter the data to be converted into QR code: ')
encode = pyqrcode.create(code, error='Q', version=4, mode='binary')

# Generate PNG image of QR codes.
encode.png('code.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
