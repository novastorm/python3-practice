def merge_sort(a_list):
    pass

def merge_sort_recursive_1(a_list):
    '''
    Split list in half recursively and merge resulting lists sorted.
    '''
    if len(a_list) <= 1:
        '''
        List of length 1 is sorted.
        '''
        return a_list

    mid = len(a_list) // 2
    A = merge_sort_recursive_1(a_list[0:mid])
    B = merge_sort_recursive_1(a_list[mid:])

    results = []
    while A or B:
        if A and not B:
            results.extend(A)
            break
        if B and not A:
            results.extend(B)
            break

        if A[0] < B[0]:
            results.append(A.pop(0))
        else:
            results.append(B.pop(0))

    return results

# def merge_sort(a_list):
#     if len(a_list) > 1:
#         mid = len(a_list) // 2
#         left_half = a_list[:mid]
#         right_half = a_list[mid:]
    
#         merge_sort(left_half)
#         merge_sort(right_half)
    
#         i = 0
#         j = 0
#         k = 0

#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 a_list[k] = left_half[i]
#                 i = i + 1
#             else:
#                 a_list[k] = right_half[j]
#                 j = j + 1
#             k = k + 1
        
#         while i < len(left_half):
#             a_list[k] = left_half[i]
#             i = i + 1
#             k = k + 1
#         while j < len(right_half):
#             a_list[k] = right_half[j]
#             j = j + 1
#             k = k + 1

#     return a_list
def merge_sort_in_place_recursive_top_down(a_list):
    if not a_list:
        return a_list

    def helper(a_list, lo, hi):
        if hi - lo == 1:
            return a_list

        mid = (hi + lo) // 2
        print("", lo, hi, "mid:", mid)
        print(a_list[lo:mid])
        print(a_list[mid:hi])
        helper(a_list, lo, mid)
        helper(a_list, mid, hi)

        i = lo
        j = mid
        while i < mid and j < hi:
            print("B:", a_list[lo:hi])
            print("i,j", (i,j))
            if not (i < mid) or not (j < hi):
                break

            if a_list[i] < a_list[j]:
                print("i += 1", )
                i += 1
            else:
                print("j += 1")
                a_list[i], a_list[j] = a_list[j], a_list[i]
                i += 1
            print("A:", a_list[lo:hi])

        return a_list

    return helper(a_list, 0, len(a_list))


def merge_sort_in_place_recursive_bottom_up(a_list):
    if not a_list:
        return a_list
    pass

def merge_sort_in_place_iterative(a_list):
    if not a_list:
        return a_list
    pass

###############################################################################

import unittest

class Test_merge_sort_recursive_1(unittest.TestCase):

    def setUp(self):
        pass

    def test_empty(self):
      i = []
      e = []
      self.assertEqual(merge_sort_recursive_1(i), e)

    def test_single(self):
      i = [2]
      e = [2]
      self.assertEqual(merge_sort_recursive_1(i), e)

    def test_od(self):
      i = [7,1,8,2,5]
      e = [1,2,5,7,8]
      self.assertEqual(merge_sort_recursive_1(i), e)

    def test_even(self):
      i = [2,7,5,9,8,9]
      e = [2,5,7,8,9,9]
      self.assertEqual(merge_sort_recursive_1(i), e)

    def test_negative_even(self):
      i = [-8,-2,-1,-9,-2,-4]
      e = [-9, -8, -4, -2, -2, -1]
      self.assertEqual(merge_sort_recursive_1(i), e)


# class Test_merge_sort_in_place(unittest.TestCase):

#     def setUp(self):
#         pass

#     def test_empty(self):
#       i = []
#       e = []
#       self.assertEqual(merge_sort_in_place_recursive_top_down(i), e)

#     def test_single(self):
#       i = [2]
#       e = [2]
#       self.assertEqual(merge_sort_in_place_recursive_top_down(i), e)

#     def test_odd(self):
#       i = [7,1,8,2,5]
#       e = [1,2,5,7,8]
#       self.assertEqual(merge_sort_in_place_recursive_top_down(i), e)

#     def test_even(self):
#       i = [2,7,5,9,8,9]
#       e = [2,5,7,8,9,9]
#       self.assertEqual(merge_sort_in_place_recursive_top_down(i), e)

#     def test_negative_even(self):
#       i = [-8,-2,-1,-9,-2,-4]
#       e = [-9, -8, -4, -2, -2, -1]
#       self.assertEqual(merge_sort_in_place_recursive_top_down(i), e)

if __name__ == '__main__':
    unittest.main()
    