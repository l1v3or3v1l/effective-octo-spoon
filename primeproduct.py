def isPrime(n: int) -> bool:
	c = 0;
	if n > 1:
		for i in range(2, n//2+1):
			if (n % i == 0):
				return False;
		return True;
	return False;

def primeproduct(m: int) -> bool:
	for i in range(1, m//2+1):
		if (m % i == 0 and isPrime(i) and isPrime(m//i) and m//i*i == m):
			return True;
	return False;

def delchar(s: str, c: chr) -> str:
	if (len(c) > 1): return s;
	idx = s.find(c);
	while (idx >= 0):
		tmp = "";
		tmp += s[:idx] + s[idx+1:];
		s = tmp;
		idx = s.find(c);
	return s;

def shuffle(l1: list, l2: list) -> list:
	l3 = [];
	for i in range(0, min(len(l1), len(l2))):
		l3.append(l1[i]);
		l3.append(l2[i]);
	if len(l1) > len(l2):
		l3.extend(l1[min(len(l1), len(l2)):]);
	elif len(l2) > len(l1):
		l3.extend(l2[min(len(l1), len(l2)):]);
	return l3;

print(primeproduct(6));
print(primeproduct(188));
print(primeproduct(202));

print(delchar("banana","b"));
print(delchar("banana","a"));
print(delchar("banana","n"));
print(delchar("banana","an"));

print(shuffle([0,2,4],[1,3,5]));
print(shuffle([0,2,4],[1]));
print(shuffle([0],[1,3,5]));
