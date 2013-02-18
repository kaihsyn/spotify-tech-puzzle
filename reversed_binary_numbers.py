BASE = 2
bits = []

num = int(raw_input())

while True:
	if num == 0:
		break
	else:
		bits.append(str(num % 2))
		num /= BASE

print int(''.join(bits), base=BASE)
