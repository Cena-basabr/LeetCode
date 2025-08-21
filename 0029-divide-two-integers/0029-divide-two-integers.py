class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if divisor == 0:
            raise ValueError("Division by zero is not allowed")

        sign = 1 if (dividend * divisor) >= 0 else -1

        dividend_abs = abs(dividend)
        divisor_abs = abs(divisor)

        result = dividend_abs // divisor_abs

        result *= sign

        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        else:
            return result
