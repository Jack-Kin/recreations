def find_kth(a, b, k):
    if len(a) > len(b):
        a, b = b, a

    # 2 boundary conditions
    if len(a) == 0:
        return b[k]
    if k < 3:
        c = a[0:min([k+1, len(a)])] + b[0:min([k+1, len(b)])]
        return sorted(c)[k]

    # induction, find cutpoint
    # cutpoint: a[n - 1] and b[l - 1]
    n = min((len(a) + 1) / 2, k - 1)
    l = min(k - n, len(b))

    if a[n - 1] <= b[l - 1]:
        return find_kth(a[n:], b, k - n)
    return find_kth(a, b[l:], k - l)

class Solution(object):
    def findMedianSortedArrays(self, s1, s2):
        """
        :type s1: List[int]
        :type s2: List[int]
        :rtype: float
        """
        l = len(s1) + len(s2)
        if l % 2 == 1:
            return find_kth(s1, s2, l/2)
        return (find_kth(s1, s2, (l - 1)/2) + find_kth(s1, s2, (l + 1)/2)) / 2.0