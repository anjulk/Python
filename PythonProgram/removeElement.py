import argparse

def removeElement(nums, elementToRemove):
    emptyList = []
    l1 = len(nums)
    counter = 0 
    for i in range(l1):
        if elementToRemove == nums[i]:
            pass
        else:
            emptyList.append(nums[i])
            counter += 1
    if counter <= l1-1:
        while counter < l1:
            emptyList.append('_')
            counter += 1
    print(l1)
    print(counter)
    return emptyList


def main(nums, number):
    if number in nums:
        return(removeElement(nums, number))
    else:
        return 'Number not present in List therefore, nothing to remove'


if __name__ == '__main__':
    # Initialize arguments parser
    parser = argparse.ArgumentParser()
    # Add elements and get element to remove from the list as a user input from command line
    parser.add_argument('elementToRemove', help="elementToRemove", type=int)
    
    args = parser.parse_args()
    print(args.elementToRemove)
    print(main([1,2,3,5,3,1,3,], args.elementToRemove))