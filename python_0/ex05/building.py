import sys


def calculate(strvar: str):
    upper=0
    lower =0
    spaces =0
    num =0
    mark =0
    for i in strvar:
        if i.islower() :
            lower +=1
        elif i.isupper():
            upper +=1
        elif i.isspace():
            spaces+=1
        elif i.isdigit():
            num+=1
        else:
            mark+=1
    total = len(strvar)
    print("The text contains",total,"characters: ")
    print(upper," upper letters")
    print(lower," lower letters")
    print(mark," punctuation marks")
    print(spaces," spaces")
    print(num," digits")

def main():
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        elif len(sys.argv) == 2:
            calculate(sys.argv[1])
        elif len(sys.argv) == 1:
            v = input("What is the text to count?") 
            calculate(v)
    except EOFError:
        return
    except AssertionError as e:
        print("AssertionError: ",e)


if __name__ == "__main__":
    main()