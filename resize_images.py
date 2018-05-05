from PIL import Image
from resizeimage import resizeimage
import os
path = os.path.join(os.getcwd(),'images')
files = os.listdir(path)
for image in files:
	fd_img = open(os.path.join(path,image), 'rb')
	img = Image.open(fd_img)
	img = resizeimage.resize_width(img,500)
	print('Resized Image: {}'.format(image))
	img.save(os.path.join(path,image), img.format)
	fd_img.close()
