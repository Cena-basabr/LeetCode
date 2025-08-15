class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()

        a, b, c = nums[0], nums[1], nums[2]

        if a + b <= c:
            return "none"
        if a == b and b == c:
            return "equilateral"
        if a == b or b == c:
            return "isosceles"

        return "scalene"