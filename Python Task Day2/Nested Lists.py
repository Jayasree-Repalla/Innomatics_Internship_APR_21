nestedlist = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    nestedlist.append([name,score])

lowestscore = min(b for a,b in nestedlist)
for a,b in nestedlist:
    nestedlist.sort()
    for a,b in nestedlist:
        if (b == lowestscore): 
            nestedlist.remove([a,b])

secondlowest = min(b for a,b in nestedlist)
for a,b in nestedlist:
    if b == secondlowest:
        print(a)