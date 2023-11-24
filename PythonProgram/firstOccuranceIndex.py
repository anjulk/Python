# Find first occurance of a string inside another string and return Index
# This function returns -1 if the string is not found
def firstOccuranceIndex( ):
    inputString = input('Input your string  ')
    firstOccurance = input('Input string to be found ')
    print(inputString , firstOccurance)
    l1 = len(inputString)
    l2 = len(firstOccurance)
    
    if l2 == 0:
        return -1
    elif l2 > l1:
        return -1
    else:
        counter = 0
        position = -1
        for i in range(l1):
            if firstOccurance[counter] == inputString[i]:
                counter += 1
            else:
                counter = 0
            if counter == 1:
                position = i
            
            if counter == l2:
                return position
        return -1


def main():
    print('Index of String is at %d' % (firstOccuranceIndex()))

if __name__ == '__main__':
    main()