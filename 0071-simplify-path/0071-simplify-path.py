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
            else:
                stack.append(name)
        return "/" + "/".join(stack)
    
            