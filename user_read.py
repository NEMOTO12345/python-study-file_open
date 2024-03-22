user = int(input())

with open("user.csv","r") as f:
    for line in f:
        i = line.strip().split(',')
        if int(i[2]) >= user:
            print(i[0],i[1])