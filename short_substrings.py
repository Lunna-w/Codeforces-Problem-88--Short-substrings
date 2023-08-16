t = int(input())

for i in range(t):
    b = input().strip()
    
    if len(b) == 2:
        print(b)
    else:
        a = [b[i] for i in range(0, len(b), 2)]
        a.append(b[-1])
        print(''.join(a))