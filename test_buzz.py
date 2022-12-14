from buzz import FizzBuzz

fizzer = FizzBuzz()

values = list(fizzer.generate(19))

desired_output = [1,
        2,
        'Fizz',
        4,
        'Buzz',
        'Fizz',
        7,
        8,
        'Fizz',
        'Buzz',
        11,
        'Fizz',
        13,
        14,
        'FizzBuzz',
        16,
        17,
        'Fizz']

assert values == desired_output
