class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        temp = path.split("/")

        stack = []
        for name in temp:
            if not name or name == ".":   
                continue
            if name == "..":
                if stack:
                    stack.pop()
                continue
            else:
                stack.append(name)
        ans = "/"
        do_flash = False
        for name in stack:
            if do_flash:
                ans += (f"/{name}")
            else:
                ans += (f"{name}")
                do_flash = True
        return ans
            