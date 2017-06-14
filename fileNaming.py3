def fileNaming(names):
    ans = []
    ans.append(names[0])
    for i in range(1,len(names)):
        name = names[i]
        n = ans.count(name)
        if n > 0:
            while True:
                s = name + '(' + str(n) + ')'
                if s not in ans:
                    ans.append(s)
                    break
                else:
                    n += 1
        else:
            ans.append(name)
            
    return ans
