def kbig(nums,k):
    set_nums = set(nums)
    while k>0:
        del_num=max(set_nums)
        set_nums.remove(del_num)
        k-=1
    print(del_num)




