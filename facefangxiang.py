import sys
import shutil

import face_recognition
from PIL import Image, ImageDraw

parser = argparse.ArgumentParser()
parser.add_argument('filename', action="store", help=u'Ŀ¼')
parser.add_argument('--version', action='version',
                    version='%(prog)s 1.1 Rongzhong xu 2018 12 05')
options = parser.parse_args()

angles = {0:'up', 90:'right', 180:'down',270:'left'}
tmp_file = '/tmp/test.jpg'
for i in range(4):
    angle = 90 * i
    if angle > 0:
        img = Image.open(options.filename)
        img = img.rotate(angle, expand=True)
        img.save(tmp_file)     
        image = face_recognition.load_image_file(tmp_file)
    else:
        image = face_recognition.load_image_file(options.filename)
    face_locations = face_recognition.face_locations(image)
    if face_locations:
        print(angles[angle])
        sys.exit(0)

print("can not find face!")