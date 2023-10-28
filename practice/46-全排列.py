def permute(nums):
    res = []
    def dfs(path):
        if len(path) == len(nums):
            res.append([nums[i] for i in path])
            return
        for i,v in enumerate(nums):
            if i not in path:
                dfs(path + [i])

    dfs([])
    return res

print(permute([1,2,3]))
print(permute([1,2,3,4]))

