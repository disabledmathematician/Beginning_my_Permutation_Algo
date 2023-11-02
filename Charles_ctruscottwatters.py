def Charles():
	P = [1, 2, 3, 4, 5]
	x = 1
	y = 1
	x <<= len(P) - 1
	y <<= len(P) - 1
	c = len(P) - 1
	while c >= 0:
		print("{:05b}".format(x))
		print("{:05b}".format(y))
		print("Array element {} moved to {}".format(len(P) - 1, c))
		c2 = c
		y2 = y
		if c2 <= 4:
			while c2 <= (len(P) - 1):
				y2 <<= 1
				print("{:05b} to {:05b}".format(y, y2))
				print("Previous array element {} moved to {}".format(c, c2))
				c2 += 1
		y >>= 1
		c -= 1
	
if __name__ == """__main__""": Charles()