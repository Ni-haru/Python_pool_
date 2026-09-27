import sys

def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError(" the arguments are bad")
        s = sys.argv[1]
        n = sys.argv[2]
        if s.replace(" ","").isalpha() & n.isdigit():
            n = int(n)
            lst = s.split(" ")
            re =[word for word in lst if(lambda x :len(x) > n)(word)]
            print(re)
        else:
            raise AssertionError(" the arguments are bad")
    except AssertionError as e:
        print("AssertionError :",e)

if __name__ =="__main__":
    main()