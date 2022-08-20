import base64

enc_flag = '==QVAH{==wd3lc==AMm3_==Ad0_b==QMu3s==wX5up==wMr_s==wMcr3==wN_c1==Qdb}'
copy_flag = enc_flag

for i,j in enumerate(enc_flag):
    if i % 7 == 0:
        part = enc_flag[i:i+4]
        based = base64.b64decode(part[::-1] + '===').decode()
        copy_flag = copy_flag.replace(part,based)

print(copy_flag)
