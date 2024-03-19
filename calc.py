import string

def add(n, m) -> int:
	return n + m

def sub(n, m) -> int:
	return n - m

def mul(n, m) -> int:
	return n * m

def div(n, m) -> float:
	return n / m

def main():
	s = input("enter expr op expr format eg. 2+2 : ")
	
	idx = 0

	for i in range(len(s)):
		if s[i] not in string.digits:
			idx = i
			break
	
	num1 = int(s[:idx])
	num2 = int(s[idx+1:])
	op = s[idx]

	dc = {
		"+" : add,
		"-" : sub,
		"*" : mul,
		"/" : div
	}

	print(dc[op](num1, num2))

if __name__ == '__main__':
	main()