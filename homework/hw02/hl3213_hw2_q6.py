def two_sum(srt_lst, target):
    lstLen = len(srt_lst)
    addend1 = 0
    addend2 = lstLen - 1
    i = 0
    j = 0

    while addend1 < addend2 and addend2 != lstLen - 1:
        