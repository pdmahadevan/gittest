def bubble(l):

    li = 0;
    size = len(l);
    
    while (li < size): 
        tmp = li;
        minn = tmp;
        while (tmp < size - 1):
            tmp = tmp + 1;
            if l[tmp] < l[minn]:
                minn = tmp; 
        tmp = l[li];
        l[li] = l[minn];
        l[minn] = tmp;
        li = li + 1;

    return l;
        

