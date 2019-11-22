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


