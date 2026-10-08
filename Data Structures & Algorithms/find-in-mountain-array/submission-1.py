class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        cache = {}

        def get(i):
            if i not in cache:
                cache[i] = mountainArr.get(i)
            return cache[i]
        
        l, r = 0, length-1
        while l < r:
            m = (l+r)//2
            if get(m) < get(m+1):
                l = m + 1
            else:
                r = m
        peak = l

        def bin_search(l, r, asc):
            while l < r:
                m = (l + r) // 2
                val = get(m)
                if val == target:
                    return m
                if asc == (val < target):
                    l = m + 1
                else:
                    r = m
            return -1
        
        res = bin_search(0, peak + 1, True)
        if res != -1:
            return res
        return bin_search(peak+1, length, False)

            
            