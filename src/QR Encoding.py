import pyqrcode

encode = pyqrcode.create('Wireless Attendance System', error='Q', version=4, mode='binary')

# Generate PNG image of QR codes.

encode.png('code.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
encode.show()
