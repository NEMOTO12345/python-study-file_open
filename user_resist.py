sei = input('苗字')
mei = input('名前')
age = input('年齢')
i = sei + ',' + mei + ',' + age +'\n'

# e = open('user.csv','w')
# e.write(i)
# e.close()

with open("user.csv","a", encoding="Shift_JIS") as f:
    f.write(i)

