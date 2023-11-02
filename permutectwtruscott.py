from PIL import Image, ImageDraw
from itertools import permutations
def Charles():
	width = 600
	height = 600
	image = Image.new(mode='L', size=(height, width), color=255)
	y_start = 0
	y_end = image.height
	draw = ImageDraw.Draw(image)
	L = ["#b6b6b6b6", "#8a8a8a8a", "#ffffffff", "#00000000"]
	x = permutations(L)
	c = 0
	for p in x:
		print(p)
		draw.rectangle(((0, 0), (0 + image.height / 2, 0 + image.width / 2)), fill=p[0])
		draw.rectangle(((image.height / 2, image.width / 2), (image.height, image.width)), fill=p[1])
		draw.rectangle(((0, image.height), (image.height / 2, image.width / 2)), fill=p[2])
		draw.rectangle(((0 + image.width, 0), (image.width / 2, image.height / 2)), fill=p[3])
#	draw.rectangle(((image.height / 2, image.width / 2), (0, image.width)), fill=144)
#	draw.rectangle(((image.height / 2, image.width / 2), image.height, image.width), fill=0)
#	draw.rectangle(((image.height / 2, image.height / 2), image.height, image.width), fill=0)
#	for x in range(0, image.width, image.width // 2):
#		line = ((x, y_start), (x, y_end))
#		draw.rectangle((0, 0), (0))
#		draw.line(line, fill=128)
#	x_start = 0
#	x_end = image.width
#	for y in range(0, image.height, image.height // 2):
#		line = ((x_start, y), (x_end, y))
#		draw.line(line, fill=128)
		
		image.save('{}_ctruscottwatters.png'.format(c))
		c += 1
Charles()