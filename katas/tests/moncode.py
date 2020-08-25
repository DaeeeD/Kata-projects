


def FizzBuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0 :
        return 'Buzz'
    return number

for number in range(1, 100):
    print(FizzBuzz(number))