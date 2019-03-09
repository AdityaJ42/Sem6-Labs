import time


def substitution_encrypt(pt, ok, ek):
	ct1 = ''
	for i in range(len(pt)):
		key = 0
		if i % 2 == 0:
			key = ok
		else:
			key = ek
		temp, up = (ord(pt[i]) - 65, 1) if pt[i].isupper() else (ord(pt[i]) - 97, 0)
		if up:
			ct1 += chr((temp + key) % 26 + 65)
		else:
			ct1 += chr((temp + key) % 26 + 97)
	return ct1


def transposition_encrypt(ct):
	ct2 = list(ct)
	l = len(ct)
	for i in range(l // 2):
		ct2[i], ct2[l - i - 1] = ct2[l - i - 1], ct2[i]
	return ''.join(ct2)


def substitution_decrypt(pt, ok, ek):
	ct1 = ''
	for i in range(len(pt)):
		key = 0
		if i % 2 == 0:
			key = ok
		else:
			key = ek
		temp, up = (ord(pt[i]) - 65, 1) if pt[i].isupper() else (ord(pt[i]) - 97, 0)
		if up:
			ct1 += chr((temp - key) % 26 + 65)
		else:
			ct1 += chr((temp - key) % 26 + 97)
	return ct1


def transposition_decrypt(ct):
	ct2 = list(ct)
	l = len(ct)
	for i in range(l // 2):
		ct2[i], ct2[l - i - 1] = ct2[l - i - 1], ct2[i]
	return ''.join(ct2)


def main():
	message = input('Enter the message to be encrypted: ')
	odd_key = int(input('Enter the odd key: '))
	even_key = int(input('Enter the even key: '))
	ct = ''.join(message.split())

	print('Encrypting.....')
	time.sleep(5)
	for j in range(10):
		ct = substitution_encrypt(ct, odd_key, even_key)
		ct = transposition_encrypt(ct)

	print('Encrypted Data: ', ct)

	time.sleep(2)
	print('\nDecrypting.....')
	time.sleep(5)
	for j in range(10):
		ct = transposition_decrypt(ct)
		ct = substitution_decrypt(ct, odd_key, even_key)

	print('Decrypted Data: ', ct)

if __name__ == '__main__':
	main()
