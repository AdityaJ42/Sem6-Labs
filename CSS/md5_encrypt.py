import hashlib

letter = 'C'
line = 'This is an example line.'
paragraph = "In writing, the words point and purpose are almost synonymous. Your point is your purpose, and how you decide to make your point clear to your reader is also your purpose."

print('Letter: {}'.format(letter))
print('Line: {}'.format(line))
print('Paragraph: {}'.format(paragraph))
# md5
enc1_md5 = hashlib.md5(letter.encode())
enc2_md5 = hashlib.md5(line.encode())
enc3_md5 = hashlib.md5(paragraph.encode())
print('\nMD5')
print('Character Encryption: {}'.format(enc1_md5.hexdigest()))
print('Line Encryption: {}'.format(enc2_md5.hexdigest()))
print('Paragraph Encryption: {}'.format(enc3_md5.hexdigest()))
# sha1
enc1_sha1 = hashlib.sha1(letter.encode())
enc2_sha1 = hashlib.sha1(line.encode())
enc3_sha1 = hashlib.sha1(paragraph.encode())
print('\nSHA1')
print('Character Encryption: {}'.format(enc1_sha1.hexdigest()))
print('Line Encryption: {}'.format(enc2_sha1.hexdigest()))
print('Paragraph Encryption: {}'.format(enc3_sha1.hexdigest()))
