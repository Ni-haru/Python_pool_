import sys

NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. "
}

def main():
    try:
        if len(sys.argv) == 2:
            for i in sys.argv[1]:
                if i.upper() not in NESTED_MORSE:
                    raise AssertionError("the arguments are bad")
            result=""
            for i in sys.argv[1]:
                result += NESTED_MORSE[i.upper()]
            print(result.rstrip())
        else:
            raise AssertionError("the arguments are bad")
    except AssertionError as e:
        print("AssertionError: ",e)
    
if __name__ =="__main__":
    main()