print(''.isspace())
print('Wn'.isspace())
print('  '.isspace())

while True:
    passward=input('새로운 패스워드를 선택하시오(문자와 숫자만 가능)')
    if password.isalnum():
        print("(정상)")
    else:
        print('문자와 숫자만을 이용하여 패스워드를 선택하시오.')
