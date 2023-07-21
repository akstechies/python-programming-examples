
#TODO: You are given an empty list named names, you have to insert “Robin”, “Aman”, “Rahul” at the end of list one after other.

def main():
    names = []
    # YOUR CODE GOES HERE
    theNames = [ "Robin", "Aman", "Rahul" ]
    for x in theNames:
        names.append(x)
    print(names)
    return 0

if __name__ == '__main__':
    main()