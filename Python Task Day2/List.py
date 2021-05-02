if __name__ == '__main__':
    N = int(input())
    Output = [];
    for i in range(0,N):
        list = input().split();
        if list[0] == "print":
            print(Output)
        elif list[0] == "insert":
            Output.insert(int(list[1]),int(list[2]))
        elif list[0] == "remove":
            Output.remove(int(list[1]))
        elif list[0] == "pop":
            Output.pop();
        elif list[0] == "append":
            Output.append(int(list[1]))
        elif list[0] == "sort":
            Output.sort();
        else:
            Output.reverse();
