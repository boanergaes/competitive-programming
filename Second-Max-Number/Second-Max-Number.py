if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr);
    max_ = float('-inf')
    s_max = float('-inf')
    
    for i in arr:
        if i > max_:
            s_max = max_
            max_ = i 
        elif i > s_max and i < max_:
            s_max = i
                        
    print(s_max)