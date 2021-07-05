# def getGcd(a, b):
#     return a if b == 0 else getGcd(b, a % b)

# def solution(arr):
#     if len(arr) == 1:
#         return arr[0]
#     answer = 1
#     firstVal = arr[0]
#     secondVal = arr[1]
#     gcd = getGcd(firstVal, secondVal)
    
#     for i in range(2, len(arr)):
#         gcd = getGcd(gcd, arr[i])
        
#     for n in arr:
#         answer *= n // gcd
        
#     return answer * gcd

def solution(arr):
    n = 1 
    while True:
        maxVal = max(arr) # 제일 큰수를 1씩 증가시켜가면서 곱해본다
        maxVal *=  n
        for num in arr:
            if maxVal % num != 0: # 모든 원소가 다 나누어 떨어지면 답
                n += 1
                break
        else:
            return maxVal
        
        
    