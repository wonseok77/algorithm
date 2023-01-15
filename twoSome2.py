# Two sum
# 정수가 저장된 배열 nums이 주어졌을 때, nums의 원소중 두 숫자를 더해서
# target이 될 수 있으면 True 불가능하면 False를 반환하세요. 같은 원소를 두 번
# 사용할 수 없습니다.

# 제약조건
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9


# input : nums = {4, 1, 9, 7, 5, 3, 16}, target : 14
# output : True

# input : nums = {2, 1, 5, 7}, target : 4
# output : False

def twoSome2(nums, target):
    nums.sort() # O(nlogn)
    l, r = 0, len(nums)-1
    while l<r:
        if nums[l] + nums[r] > target:
            r -= 1
        elif nums[l] + nums[r] < target:
            l += 1
        elif nums[l] + nums[r] == target:
            return True
    return False

print(twoSome2(nums=[4, 1, 9, 7, 5, 3, 16], target=14))