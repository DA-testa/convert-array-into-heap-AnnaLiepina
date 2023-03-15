# python3

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

    for i in range(len(data)):
        j = len(data)-1 - i
        while j > 0:
            if data[j] < data[(j-1) // 2]:
                swaps.append(((j-1) // 2, j))
                data[j], data[(j-1) // 2] = data[(j-1) // 2], data[j]
                j = (j-1)//2
            else:
                j-=1
    return swaps

def main():

    # input to choose what input method to use
    command = input()

    # input from keyboard
    if command[0] == 'I':
        n = int(input())
        data = list(map(int, input().split()))

        # checks if lenght of data is the same as the said lenght
        assert len(data) == n

        # calls function to assess the data 
        # and give back all swaps
        
        swaps = build_heap(data)

        # TODO: output how many swaps were made, 
        # this number should be less than 4n (less than 4*len(data))

        # output all swaps
        print(len(swaps))
        for i, j in swaps:
            print(i, j)
            
    # input from file
    elif command[0] == 'F':
        file_name = input()

        file = open('./tests/' + file_name, 'r')

        n = int(file.readline())

        data = list(map(int, file.readline().split()))

        assert len(data) == n
        swaps = build_heap(data)

        # TODO: output how many swaps were made, 
        # this number should be less than 4n (less than 4*len(data))

        print(len(swaps))
        for i, j in swaps:
            print(i, j)

if __name__ == "__main__":
    main()
