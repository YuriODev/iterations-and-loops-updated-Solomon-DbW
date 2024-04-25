n = int(input())


for i in range(1, n+1):
    j = i
    is_Palindrome = False

    if j % 10 == 0:
        is_Palindrome = False
    
    elif j < 10:
        is_Palindrome = True
        
    elif j < 100 and j % 10 == j // 10:
            is_Palindrome = True
        
    elif j < 1000 and  j % 10 == j // 100:
            is_Palindrome = True
        
    elif j < 10000 and j % 10 == j // 1000 and j // 10 % 10 == j // 100 % 10 and j // 100 % 10 == j // 1000:
            is_Palindrome = True
        
    elif j < 100000 and j % 10 == j // 10000 and j // 10 % 10 == j // 100 % 10 and j // 100 % 10 == j // 1000 % 10 and j // 1000 % 10 == j // 10000:
            is_Palindrome = True
        
    if is_Palindrome:
        print(i, end=" ")