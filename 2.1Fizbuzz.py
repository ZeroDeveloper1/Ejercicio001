def fizzbuzz():
    for i in range(1, 101):
        result = ''
        if i % 3 == 0:
            result += 'Fizz'
        if i % 5 == 0:
            result += 'Buzz'
        print(result or i)

if __name__ == "__main__":
    fizzbuzz()