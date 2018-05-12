input = input("입력해주세요! : ")

if input == '안녕':
    print('안녕하세요~!')
elif input == '사랑해':
    print('저도요~~')
elif input == '반복더하기':
    repeat = int(input('1부터 어디까지를 더한 합이죠? : '))
    for i in range(1, repeat + 1):
        sum += i
    print('1부터 ' + repeat + '까지를 더한 합은 ' + sum + '입니다.')
else:
    print('반가워요~')
