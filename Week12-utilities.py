#https://github.com/npmiller3/Week12-Assignments
#Nathan Miller
#CSCI102-Section A
#Week12-utilities

def PrintOutput(a):
    print('OUTPUT', a)

def LoadFile(filename):
    filename = open(filename, 'r+')
    astring = filename.read()
    alist = astring.splitlines()
    return alist

def UpdateString(a, b, c):
    new_list = []
    for i in a:
        new_list.append(i)
    new_list[c] = b
    new_str = ''
    for i in new_list:
        new_str += i
    PrintOutput(new_str)

def FindWordCount(alist, astring):
    count = 0
    for i in alist:
        if i == astring:
            count += 1
    PrintOutput(count)

def ScoreFinder(players, scores, name):
    name = name.lower()
    for i in range(len(players)):
        players[i] = players[i].lower()
    for i in range(0, len(players)):
        if players[i] == name:
            return ('OUTPUT', players[i], 'got a score of', scores[i])
    return ('player not found')

def Union(list1, list2):
    list3 = list1 + list2
    list4 = []
    for i in range(len(list3)):
        if list4.count(list3[i]) == 0:
            list4.append(list3[i])
    return list4







