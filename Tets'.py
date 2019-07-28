from collections import defaultdict
def lcs(xstr, ystr):
    lcs = ['']
    lcslen = 0
    location = defaultdict(list)
    #print(location)
    i = 0
    for k in ystr:
        location[k].append(i)
        i += 1
    #print(i)
    #print(location)
    for i in xrange(len(xstr)):
        cs = ''
        index = -1
        reached_index = defaultdict(int)
        for item in xstr[i:]:
            for new_index in location[item][reached_index[item]:]:
                reached_index[item] += 1
                if index < new_index:
                    cs += item
                    index = new_index
                    break
            if index == len(ystr) - 1:
                break
        if len(cs) > lcslen:
            lcs, lcslen = [cs], len(cs)
        elif len(cs) == lcslen:
            lcs.append(cs)
    return set(lcs)


print(lcs("AAAABCC","AAAACCB"))