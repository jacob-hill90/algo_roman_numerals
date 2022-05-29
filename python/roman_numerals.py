def to_roman(num):
    answer = ""
    dictionary = {
        "M": 1000,
        "CMXLIV": 900,
        "D": 500,
        "C": 100,
        "L": 50,
        "XLIV": 44,
        "XIV": 14,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }
    for Key in dictionary:
        while num >= dictionary[Key]:
            answer += Key
            num -= dictionary[Key]
    return answer
    