testcases = int(input())
for i in range(1,testcases+1):
    n_cards = int(input())
    x = []
    x_sorted = []
    count = 0
    for _ in range(n_cards):
        card = input()
        x.append(card)
        x_sorted.append(card)
        x_sorted.sort()
        if(x_sorted != x):
            count += 1
        x.sort()
    
    print(f"Case #{i}: {count}")


               

        
