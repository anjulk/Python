import argparse

def lastWorldLength(lastWorldLengthString):
    if len(lastWorldLengthString) == 0 or lastWorldLengthString[0] == '':
        return -1
    
    if lastWorldLengthString[-1] == '':
        return len(lastWorldLengthString[-2])

def main(inputString):
    convertList =  inputString.split(' ')
    print(lastWorldLength(convertList))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument("inputString", help="input string", type=str)
    args = parser.parse_args()
    main(args.inputString)
    