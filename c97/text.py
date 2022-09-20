def text():
    file=input('enter file name: ')
    count = 0
    fileOpener=open(file,"r")
    for i in fileOpener:
        words= i.split()
        count=count+len(words)
    print(count)
    

text()
    