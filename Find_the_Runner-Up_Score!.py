if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = list(arr)
    
    winner = arr[0]
    runner_up = float('-inf')

    for score in arr:
        if score > winner:
            runner_up = winner
            winner = score
        elif score > runner_up and score != winner:
            runner_up = score

    print(runner_up)
