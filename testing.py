def test(function, expected, *input):
    result = function(*input)
    print(f'{"Pass" if result == expected else "Fail"} | Input: {input} | Output: {result} | Expected: {expected}')
