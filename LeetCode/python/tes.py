class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # res = []
        # candidates.sort()

        # def dfs(idx, path, cur):
        #     if cur == target:
        #         res.append(path.copy())
        #         return
        #     for i in range(idx, len(candidates)):
        #         if i > idx and candidates[i] == candidates[i - 1]:
        #             continue
        #         if cur + candidates[i] > target:
        #             break

        #         # path.append(candidates[i])
        #         dfs(i + 1, path + [candidates[i]], cur + candidates[i])
        #         # path.pop()

        # dfs(0, [], 0)
        # return res

        candidates.sort()
        print(candidates)
        res = []
        def dfs(cur, total, i):
            # if i >= len(candidates):
            #     return
            if total == target:
                res.append(cur.copy())
            # print(candidates[i])

            for j in range(i, len(candidates)):
                if total + candidates[j] > target:
                    continue
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                # cr
                dfs(cur + [candidates[j]], total + candidates[j], j)

        dfs([], 0, 0)
        print(res)

        return res