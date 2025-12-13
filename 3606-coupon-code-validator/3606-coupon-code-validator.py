class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        categories = {"electronics", "grocery", "restaurant", "pharmacy"}
        priority = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }
        ans = []
        n = len(code)
        
        def identifer_validator(c):
            if c == "":
                return False             
            for symbol in c:
                x = ord(symbol)
                if not ((65 <= x <= 90) or (97 <= x <= 122) or (48 <= x <= 57) or x == 95):
                    return False
            return True 
        for i in range(n):
            coupon_code = code[i]
            coupon_line = businessLine[i] 
            if not identifer_validator(coupon_code):
                continue
            if coupon_line not in categories:
                continue
            if not isActive[i]:
                continue
            
            ans.append((coupon_code, coupon_line))
        ans.sort(key=lambda x: (priority[x[1]], x[0]))
        
        result = [x[0] for x in ans]
        return result