def find_median_sorted_arrays(nums1, nums2):
    nums = sorted(nums1 + nums2)
    n = len(nums)
    if n % 2 == 0:
        return (nums[n // 2 - 1] + nums[n // 2]) / 2
    else:
        return nums[n // 2]

if __name__ == "__main__":
    nums1 = [1, 3]
    nums2 = [2]
    print("Median of two sorted arrays:", find_median_sorted_arrays(nums1, nums2))
