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

def twoSum1(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] + nums[j] == target:
                return True
    
    return False

print(twoSum1(nums=[4,1,9,7,5,3,16], target = 14)) 
    