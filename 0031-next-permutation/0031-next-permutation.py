class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        swapped = False
        specialCase = False
        while i >= 0 and not swapped:
            print(swapped)
            if nums[i] > nums[i - 1]:
                if i >= 1 and (i <= len(nums) - 1):
                    minIndex = i
                    for k in range(i + 1, len(nums)):
                        if nums[k] > nums[i - 1] and nums[k] < nums[minIndex]:
                            specialCase = True
                            minIndex = k

                if not specialCase:
                    swapped = True
                    nums[i - 1], nums[i] = nums[i], nums[i - 1]
                    print("inside this")
                    sortFrom = i
                else:
                    nums[minIndex], nums[i - 1] = nums[i - 1], nums[minIndex]

                    swapped = True
                    sortFrom = i
                    break
            i -= 1
            print(i)
            print("check")
        print("outside while")
        if not swapped:
            nums.sort()
        else:
            nums[sortFrom::] = sorted(nums[sortFrom::])
            pass
        print(nums)

    def temp(self, nums, l, r):
        print(nums)

    def quickSort(self, nums, l, r):
        while l < r:
            pivot = self.partition(nums, l, r)
            self.quickSort(nums, l, pivot - 1)
            self.quickSort(nums, pivot + 1, r)

    def partition(self, arr, l, r):
        i = l
        j = r
        pivot = arr[l]
        while i < j:
            while arr[i] <= pivot:
                i += 1
            while arr[j] >= pivot:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[l], arr[j] = arr[j], arr[l]
        return j
