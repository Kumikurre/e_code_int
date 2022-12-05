from typing import Generator, Union

class FizzBuzz():
    def generate(self, length: int) -> Generator[Union[int, str], None, None]:
        """
        :param length: The integer number of entries to generate
        :returns: A generator which holds the output values, either str or int
        :raises ValueError: A string or an int less than 1 is not supported
        :raises TypeError: A float is not a supported input
        """
        val = int(length)
        if val < 1:
            raise ValueError('Can not generate fizzbuzz for a range less than 1.')

        # use generator to increase performance for big inputs
        for val in range(1, length):
            output = ''
            if val % 3 == 0:
                output = output + 'Fizz'
            if val % 5 == 0:
                output = output + 'Buzz'
            if output == '':
                output = val

            yield output
