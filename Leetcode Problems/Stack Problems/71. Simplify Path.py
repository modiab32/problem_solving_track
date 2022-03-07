class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = "" #store most recent file or dir bef4 a slash show up
        for c in path + "/":
            if c == "/":
                if cur =="..":
                    if stack:
                        stack.pop()
                elif cur != "" and cur!=".":
                    stack.append(cur)
                cur = ""
            else:
                cur += c
        return "/"+"/".join(stack)
