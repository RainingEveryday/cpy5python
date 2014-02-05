#"Lucky" Students <3
#http://www.classtools.net/random-name-picker/

from random import randint #Imports random integers from the fabric of space and time.

names = [
"ang.cunrong.kleon@dhs.sg",
"ang.junming@dhs.sg",
"ang.sweechow@dhs.sg",
"au.jiaying@dhs.sg",
"chin.yongchen@dhs.sg",
"chong.jiale.nicholas@dhs.sg",
"chong.jiamin.desirae@dhs.sg",
"chua.yiqi@dhs.sg",
"foo.lexian.felicia@dhs.sg",
"gn.jingwen.bellerie@dhs.sg",
"goh.jiaying1@dhs.sg",
"kou.yongkang@dhs.sg",
"lee.wenhao.damien@dhs.sg",
"li.jinjie@dhs.sg",
"lim.kaixin.sheena@dhs.sg",
"lim.mingmin.michelle@dhs.sg",
"lim.tjionghann@dhs.sg",
"loi.xinyi.audrey@dhs.sg",
"ng.cheryl@dhs.sg",
"ng.xingyu@dhs.sg",
"ng.xingyu@dhs.sg",
"ng.xingyu@dhs.sg",
"ng.xingyu@dhs.sg",
"quek.jiaqi@dhs.sg",
"shi.changxiao@dhs.sg",
"tan.chuan@dhs.sg",
"tan.meizi.sherene@dhs.sg",
"tan.meizi.sherene@dhs.sg",
"wong.jieyu.jade@dhs.sg",
"yan.hongyao.alvin@dhs.sg",
"zeng.jin@dhs.sg",
"zeng.jin@dhs.sg",
"zhu.siyi@dhs.sg"]

#1 for males, 2 for females. Another large step towards true gender equality.
gender = [
1,
1,
1,
2,
1,
1,
2,
2,
2,
2,
2,
1,
1,
2,
2,
2,
2,
2,
2,
1,
1,
1,
1,
2,
2,
1,
2,
2,
2,
1,
2,
2,
2]

#Infocomm, 0 = Not in infocomm (Double chances), 1 = In infocomm (No double chance) Hooray. Cheer and be merry.
infocomm = [
0,
0,
0,
0,
0,
0,
0,
0,
1,
0,
1,
1,
2, #Damien gets a double chance for mocha. Yay, chocolate.
0,
0,
0,
0,
0,
1,
0,
0,
0,
0,
0,
0,
1,
0,
0,
0,
1,
0,
0,
0]

chancelist = []

for name in names:
    while names.count(name) >= 2: #Code runs until one name remains, aka keeps deleting. Death awaits.
        namenumber = names.index(name) #Returns the index (number) of the first encounter with the name in the list.
        del names[namenumber] #Pew pew remove.
        del gender[namenumber]
        del infocomm[namenumber]

#Appends the chances a name is entered into a list for randomization.
for i in range(len(names)):
    if gender[i] == 2 or infocomm[i] == 0 or infocomm[i] == 2:
        n = 0
        while n <= 1:
            chancelist.append(names[i])
            n = n + 1
    elif gender[i] == 1 or infocomm[i] == 1:
        g = 0
        while g <= 0:
            chancelist.append(names[i])
            g = g + 1
    else:
        pass

winners = []

chosen = 0
while chosen <= 2:
    randomize = randint(0, int(len(chancelist)))
    winners.append(chancelist[randomize])
    chosen = chosen + 1
    if winners.count(chancelist[randomize]) >= 2:
        chosen = chosen - 1
        winners.remove(chancelist[randomize])
    else:
        pass

print(winners)
