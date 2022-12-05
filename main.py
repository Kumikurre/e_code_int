from buzz import FizzBuzz

if __name__ == '__main__':
    fizzer = FizzBuzz()

    for val in fizzer.generate(100):
        print(val)



"""
"Write a program that prints the numbers from 1 to 100.
But for multiples of three print “Fizz” instead of the number
and for the multiples of five print “Buzz”.

For numbers which are multiples of both three and five print “FizzBuzz”."
"""