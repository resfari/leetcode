
def recursion(s, len_s, new_s,ret, index, count):
    if count == 3 and index == len_s:
        ret.append(new_s)
    if count > 3:
        return
    
    i = index
    while i < len_s:
        part = s[index: i + 1]
        if len(part) == 0 or int(part) > 255 or int(part) < 0 or (part.startswith("0") and len(part) != 1):
            break
        
        new_slen = len(new_s)
        new_s += part
        
        if i + 1 != len_s:
            new_s += "."
            print(new_s)
            recursion(s, len_s, new_s, ret, i + 1, count + 1)
        else:
            recursion(s, len_s, new_s, ret, i + 1, count)
        i += 1
        new_s = new_s[:new_slen]

    


class Solution:
    def restoreIpAddresses(self, s: str) -> list:
        ret = []
        if len(s) > 12 or len(s) < 4:
            return ret
        if len(s) == 4:
            ret.append(".".join(s))
            return ret
        new_s = ""
        recursion(s, len(s), new_s, ret, 0, 0)
        return ret

s = Solution()

print(s.restoreIpAddresses("010010"))