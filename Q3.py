def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))

if __name__ == "__main__":
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 3, 3, 1]
    result = intersection(nums1, nums2)
    print("Intersection:", result)
