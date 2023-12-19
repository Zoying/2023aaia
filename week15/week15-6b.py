a, b = list(map(int, input().split()))

ans = a // b

if a % b > 0:
	ans = ans + 1
	
print(ans, end = '')