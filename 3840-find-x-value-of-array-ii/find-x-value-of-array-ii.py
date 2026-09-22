class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        tree = [None] * (4 * n)

        def merge(left, right):
            p1, c1 = left
            p2, c2 = right
            prod = (p1 * p2) % k
            cnt = list(c1)
            for r in range(k):
                cnt[(p1 * r) % k] += c2[r]
            return (prod, cnt)

        def build(node, l, r):
            if l == r:
                rem = nums[l] % k
                c = [0] * k
                c[rem] = 1
                tree[node] = (rem, c)
                return
            mid = (l + r) // 2
            build(2 * node + 1, l, mid)
            build(2 * node + 2, mid + 1, r)
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2])

        def update(node, l, r, idx, val):
            if l == r:
                rem = val % k
                c = [0] * k
                c[rem] = 1
                tree[node] = (rem, c)
                return
            mid = (l + r) // 2
            if idx <= mid:
                update(2 * node + 1, l, mid, idx, val)
            else:
                update(2 * node + 2, mid + 1, r, idx, val)
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2])

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree[node]
            mid = (l + r) // 2
            if qr <= mid:
                return query(2 * node + 1, l, mid, ql, qr)
            if ql > mid:
                return query(2 * node + 2, mid + 1, r, ql, qr)
            return merge(query(2 * node + 1, l, mid, ql, qr), 
                         query(2 * node + 2, mid + 1, r, ql, qr))

        build(0, 0, n - 1)
        res = []
        for idx, val, start, target_x in queries:
            update(0, 0, n - 1, idx, val)
            _, cnt = query(0, 0, n - 1, start, n - 1)
            res.append(cnt[target_x])
            
        return res
        