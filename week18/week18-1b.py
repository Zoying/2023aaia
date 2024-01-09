a = int(input())
if a <= 2000:
	print(100)
else:
	print((a-2000+499) // 500 * 5 + 100)