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
