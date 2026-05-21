n,m = list(map(int,input().split()))
my_array = list(map(int,input().split()))
sA = list(map(int,input().split()))
sB = list(map(int,input().split()))

happiness = 0
for num in my_array:
    if num in sA:
        happiness += 1
    elif num in sB:
        happiness -= 1
        
print(happiness)