import utils

def test_formatter(util, testValues, results):
    
    index = 0

    for value in testValues:
        print("-----------------------------------")
        print(f"INPUT: {value}")
        print(f"EXPECTED: {results[index]} | RECEIVED: {util.formatter(value)}")

        if (util.formatter(value) == results[index]):
            print("TEST PASSED")

        else:
            print("TEST FAILED")

        index += 1

def test_reversed(util, testValues, results):
    
    index = 0

    for value in testValues:
        print("-----------------------------------")
        print(f"INPUT: {value}")
        print(f"EXPECTED: {results[index]} | RECEIVED: {util.reversed(value)}")

        if (util.reversed(value) == results[index]):
            print("TEST PASSED")

        else:
            print("TEST FAILED")

        index += 1

#Call the tests from here
if __name__ == "__main__":
    
    #Initialize object
    u = utils.utils()

    #Initialize test cases
    values = ["string", "hello", 2.1, 5.5,21, 561, 1278]
    results = [None, None, None, None, 12, 165, 8721]

    #Test the function reversed
    print("TESTING REVERSED")
    print("-----------------------------------")
    test_reversed(u, values, results)

    #Initialize new test cases
    values = ["string", "hello", 2.1, 5.5,2, 21, 5]
    results = [None, None, None, None, ('0b10', '0o2'), ('0b10101', '0o25'), ('0b101', '0o5')]

    #Test the formatter function
    print("TESTING FORMATTER")
    print("-----------------------------------")
    test_formatter(u, values, results)

