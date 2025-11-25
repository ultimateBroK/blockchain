def xor_encrypt_decrypt(text, key):
    result = ""
    for char in text:
        c = ord(char)
        o = c ^ key
        new_c = chr(o)
        result += new_c
    return result

mode = input().strip()
key = int(input().strip())
text = input().rstrip('\n')

if mode == 'e' or mode == 'd':
    result = xor_encrypt_decrypt(text, key)
else: 
    result = "Chế độ không hợp lệ. Vui lòng nhập 'e' để mã hóa hoặc 'd' để giải mã."

print(result)