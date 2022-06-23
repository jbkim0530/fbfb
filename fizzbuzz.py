FizzBuzz Game

# 3의 배수 : 'fizz' (Done)
# 5의 배수 : 'buzz'(Done)
# 15의 배수 : 'fizzbuzz'(Done)
# 나머지 : 숫자(1-45) (Done)


for i in range(1, 46):
    
    if i % 15 == 0:
        print('FizzBuzz')

    elif i % 3 == 0:
        print('fizz')

    elif i % 5 == 0:
        print('buzz')
    
    else:
        print(i)


