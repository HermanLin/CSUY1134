def two_sum(srt_lst, target):
    i, j = 0, len(srt_lst) - 1

    while i < j:
        total = srt_lst[i] + srt_lst[j]
        #print("Total: ", total)
        if total < target:
            i += 1
        elif total > target:
            j -= 1
        elif total == target:
            return (i, j)
        else:
            return None

def main():
    srt_lst = [-2,7,11,15,20,21]
    two_sum(srt_lst, 22)

#main()