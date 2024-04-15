import unittest

def green_bottles():
    result = ''
    numbers = ['ten', 'nine', 'eight', 'seven', 'six', 'five', 'four', 'three', 'two', 'one', 'no']

    green_bottle = " green bottle"
    comma = ",\n"
    dot = "."
    hanging_on_the_wall = " hanging on the wall"
    and_if = "And if " 
    green_bottle_should_accidentally_fall = green_bottle + " should accidentally fall"
    threre_ll_be = "There'll be "
    if_that = "If that "

    for i in range(len(numbers) - 1):
        for _ in range(2):
            result += numbers[i].title() + green_bottle
            
            if (i != (len(numbers) - 2)):
                result += "s"
                
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

        if (i != len(numbers) - 1):
            result += "\n"

    return result

class GreenBottlesTest(unittest.TestCase):
    def test(self):
        ref = """Ten green bottles hanging on the wall,\n
Ten green bottles hanging on the wall,\n
And if one green bottle should accidentally fall,\n
There'll be nine green bottles hanging on the wall.\n
Nine green bottles hanging on the wall,\n
Nine green bottles hanging on the wall,\n
And if one green bottle should accidentally fall,\n
There'll be eight green bottles hanging on the wall.\n
Eight green bottles hanging on the wall,\n
Eight green bottles hanging on the wall,\n
And if one green bottle should accidentally fall,\n
There'll be seven green bottles hanging on the wall.\n
Seven green bottles hanging on the wall,\n
Seven green bottles hanging on the wall,\n
And if one green bottle should accidentally fall,\n
There'll be six green bottles hanging on the wall.\n
Six green bottles hanging on the wall,\n
Six green bottles hanging on the wall,\n
And if one green bottle should accidentally fall,\n
There'll be five green bottles hanging on the wall.\n
Five green bottles hanging on the wall,\n
Five green bottles hanging on the wall,\n
And if one green bottle should accidentally fall,\n
There'll be four green bottles hanging on the wall.\n
Four green bottles hanging on the wall,\n
Four green bottles hanging on the wall,\n
And if one green bottle should accidentally fall,\n
There'll be three green bottles hanging on the wall.\n
Three green bottles hanging on the wall,\n
Three green bottles hanging on the wall,\n
And if one green bottle should accidentally fall,\n
There'll be two green bottles hanging on the wall.\n
Two green bottles hanging on the wall,\n
Two green bottles hanging on the wall,\n
And if one green bottle should accidentally fall,\n
There'll be one green bottle hanging on the wall.\n
One green bottle hanging on the wall,\n
One green bottle hanging on the wall,\n
If that one green bottle should accidentally fall,\n
There'll be no green bottles hanging on the wall."""
        self.assertEqual(green_bottles(), ref)

if __name__ == "__main__":
    unittest.main()
print(green_bottles())