def cal(l,t):
    s=0
    if len(l)==1:
        for i in t:
            if i==l:
                s+=1
        return s
    else:
        print('firs parament is not a character')
        