class ADL_Array:

    @staticmethod
    def bisect(a, x, isLeft=False, lo=0, hi=None):
        if lo < 0:
            raise ValueError("Out of Bounds")
        if hi is None:
            hi = len(a)

        def bisect_right_compare(a, b):
            return a < b

        def bisect_left_compare(a, b):
            return a <= b

        if isLeft:
            compare = bisect_left_compare
        else:
            compare = bisect_right_compare


        while lo < hi:
            mid = (lo + hi) // 2
            if compare(x, a[mid]):
                hi = mid
            else:
                lo = mid + 1

        return lo
