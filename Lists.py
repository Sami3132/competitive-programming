if __name__ == '__main__':
    N = int(input())
    
    output = []
    
    for _ in range(N):
        command = input()
        comm_segments = command.split()
                
        if "insert" in command:
            output.insert(int(comm_segments[1]), int(comm_segments[2]))
            
        elif "print" in command:
            print(output)
            
        elif "remove" in command:
            output.remove(int(comm_segments[1]))
            
        elif "append" in command:
            output.append(int(comm_segments[1]))
            
        elif "sort" in command:
            output.sort()
            
        elif "pop" in command:
            output.pop()
            
        else:
            output.reverse()
