def pear(s):
    box = []
    for i in range(0,len(s),2):
        if i + 1 < len(s):
            box.append(s[i:i+2])
        else:
            box.append(s[i]+'_')
    return box