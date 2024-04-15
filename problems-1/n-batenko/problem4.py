import unittest

def green_bottles():
    result = ''
    numbers = ['ten', 'nine', 'eight', 'seven', 'six', 'five', 'four', 'three', 'two', 'one', 'no']

    green_bottle = " green bottle"
    comma = ",\n"
    dot = "."
    hanging_on_the_wall = ' hanging on the wall'
    and_if = "And if " 
    green_bottle_should_accidentally_fall = green_bottle + " should accidentally fall"
    threre_ll_be = "There'll be "
    if_that = "If that "

    for i in range(len(numbers) - 1):
        for _ in range(2):
            result += numbers[i].title() + green_bottle
            
            if (i != (len(numbers) - 2)):
                result += 's'
                
            result += hanging_on_the_wall + comma

        if (i == (len(numbers) - 2)):
            result += if_that
        else:    
            result += and_if

        result += numbers[-2] + green_bottle_should_accidentally_fall

        result += comma

        result += threre_ll_be + numbers[i + 1] + green_bottle
        if (i != (len(numbers) - 3)):
            result += 's'
        result += hanging_on_the_wall + dot

        if (i != len(numbers) - 2):
            result += '\n'

    return result

class GreenBottlesTest(unittest.TestCase):
    def test(self):
        self.maxDiff = None
        ref = """Ten green bottles hanging on the wall,
Ten green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There'll be nine green bottles hanging on the wall.
Nine green bottles hanging on the wall,
Nine green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There'll be eight green bottles hanging on the wall.
Eight green bottles hanging on the wall,
Eight green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There'll be seven green bottles hanging on the wall.
Seven green bottles hanging on the wall,
Seven green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There'll be six green bottles hanging on the wall.
Six green bottles hanging on the wall,
Six green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There'll be five green bottles hanging on the wall.
Five green bottles hanging on the wall,
Five green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There'll be four green bottles hanging on the wall.
Four green bottles hanging on the wall,
Four green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There'll be three green bottles hanging on the wall.
Three green bottles hanging on the wall,
Three green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There'll be two green bottles hanging on the wall.
Two green bottles hanging on the wall,
Two green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There'll be one green bottle hanging on the wall.
One green bottle hanging on the wall,
One green bottle hanging on the wall,
If that one green bottle should accidentally fall,
There'll be no green bottles hanging on the wall."""
        self.assertEqual(green_bottles(), ref)

if __name__ == "__main__":
    unittest.main()