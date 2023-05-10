
isbn = input()

k = 0

while k < len(isbn):
	if k == 3 or k == 4 or k == 6 or k == 12 :
		print('-', end='')
	
	print(isbn[k], end='')
	k += 1