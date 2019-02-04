def fibs(n):
    curr, prev, stor = 1, 0, 0
    ret = []
    if n >= 1:
        ret.append(1)
        for i in range(n - 1):
            ret.append(curr + prev)
            stor = curr
            curr += prev       
            prev = stor 
    else:
        return ret
    return ret