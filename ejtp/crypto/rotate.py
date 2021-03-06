'''
This file is part of the Python EJTP library.

The Python EJTP library is free software: you can redistribute it 
and/or modify it under the terms of the GNU Lesser Public License as
published by the Free Software Foundation, either version 3 of the 
License, or (at your option) any later version.

the Python EJTP library is distributed in the hope that it will be 
useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser Public License for more details.

You should have received a copy of the GNU Lesser Public License
along with the Python EJTP library.  If not, see 
<http://www.gnu.org/licenses/>.
'''


import encryptor

class RotateEncryptor(encryptor.Encryptor):
    def __init__(self, offset):
        self.offset = offset

    def encrypt(self, source):
        return self.rotate(source, self.offset)

    def decrypt(self, source):
        return self.rotate(source, -self.offset)

    def rotate(self, source, offset):
        result = ""
        for i in source:
            result += chr((ord(i)+offset) % 256)
        return result

    def proto(self):
        return ['rotate', self.offset]
