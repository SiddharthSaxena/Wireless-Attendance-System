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
