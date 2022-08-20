
import base64

enc_flag = '==QVAH{==wd3lc==AMm3_==Ad0_b==QMu3s==wX5up==wMr_s==wMcr3==wN_c1==Qdb}'

password = input('Please enter the super secret password: ')

enc_password = ""

for i,p in enumerate(password):
    if i % 4 == 0:
        enc_password += base64.b64encode(p.encode('utf-8')).decode()[::-1]
    else:
        enc_password += p

if enc_password == enc_flag:
    print("Welcome to Blue's super secret club")
else:
    print("Who are you?")
