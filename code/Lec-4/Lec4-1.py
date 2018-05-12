def gugudan(num):
    for i in range(1, 10):
        print(str(num) + ' * ' + str(i) + ' = ' + str(num * i))
    
input = int(input('보고 싶은 구구단 수를 입력하세요. : '))
gugudan(input)