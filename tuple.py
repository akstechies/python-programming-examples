
# TODO: Given two tuples called tuple1 and tuple2, perform the operations described in comments in the editor.

# * change value at index 0 of both tuple to string "number"

def main():
    tuple1 = tuple(("one", "two", "three"))
    tuple2 = tuple(("1", "2", "3"))
    
    # change value at index 0 of both tuple to string "number"
    listTuple1 = list(tuple1)
    listTuple1[0] = "number"
    tuple1 = (tuple(listTuple1))
    
    listTuple2 = list(tuple2)
    listTuple2[0] = "number"
    tuple2 = (tuple(listTuple2))
    
    print(tuple1)
    print(tuple2)
    
    return 0

if __name__ == '__main__':
    main()