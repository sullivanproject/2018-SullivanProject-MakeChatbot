def hello():
    print('안녕하세요~!')

def metoo():
    print('저도요~~')

def repeatsum(repeat):
    sum = 0
    for i in range(1, repeat + 1):
        sum += i
    return sum
    
def nicetomeetyou():
    print('반가워요~')

input = input("입력해주세요! : ")

if input == '안녕':
    hello()
elif input == '사랑해':
    metoo()
elif input == '반복더하기':
    num = int(input('1부터 어디까지를 더한 합이죠? : '))
    print('1부터 ' + num + '까지를 더한 합은 ' + repeatsum(num) + '입니다.')
else:
    nicetomeetyou()
