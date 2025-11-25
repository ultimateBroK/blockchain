# Viết chương trình thực hiện mã hóa và giải mã chuỗi ký tự dùng XOR cipher (mỗi byte XOR với một khóa 
# đơn giản). 
# Input của chương trình: 
# - Dòng 1: 1 kí tự thể hiện chế độ làm việc, kí tự e là mã hóa (encrypt), kí tự d là giải mã (decrypt) 
# - Dòng 2: Một khóa là số nguyên dương 1 byte trong khoảng 1 đến 255 
# - Dòng 3: Chuỗi text 
# Outout của chương trình: Chuỗi kết quả
def xor_encrypt_decrypt(text, key):
    result = ""
    for char in text:
        c = ord(char)
        o = c ^ key
        new_c = chr(o)
        result += new_c
    return result

mode = input()
key = int(input())
text = input().rstrip('\n')

if mode == 'e' or mode == 'd':
    result = xor_encrypt_decrypt(text, key)
else: 
    result = "Chế độ không hợp lệ. Vui lòng nhập 'e' để mã hóa hoặc 'd' để giải mã."

print(result)