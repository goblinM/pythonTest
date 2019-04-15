def increase_num(nums):
    if not nums:
        return 0
    max_num = max(nums)
    min_num = min(nums)
    total_nums = [i for i in range(min_num,max_num+1)]
    diff_nums = list(set(total_nums).difference(set(nums)))
    if not diff_nums:
        print(len(nums)-1)
        return len(nums)-1
    else:
        res = 0
        print(diff_nums)
        print(max_num-(max(diff_nums)+1)-1)

if __name__ == "__main__":
    nums = [1,3,4,5,6,9,10,11,12,13]
    # nums = [998,999,1000]
    increase_num(nums)