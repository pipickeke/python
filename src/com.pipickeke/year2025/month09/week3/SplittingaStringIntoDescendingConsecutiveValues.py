"""


"""


class Solution:
    def splitString(self, s:str)->bool:
        n = len(s)
        for i in range(1,n):
            first_str = s[:i]
            v = int(first_str)
            v -= 1
            t = s[i:]
            while t:
                while len(t) > 1 and t[0] == '0':
                    t = t[1:]

                target = str(v)
                if not t.startswith(target):
                    break

                t = t[len(target):]
                v -= 1

            else:
                return True
        return False



    def splitString_2(self, s: str) -> bool:
        n = len(s)
        for i in range(1,n):
            first_str = s[:i]
            v = int(first_str)
            v -= 1

            t = s[i:]
            while t:
                while len(t) > 1 and t[0] == '0':
                    t = t[1:]

                target = str(v)
                if not t.startswith(target):
                    break

                t = t[len(target):]
                v -= 1

            else:
                return True
        return False




    def splitString_3(self, s: str) -> bool:
        n = len(s)
        for i in range(1,n):
            first_str = s[:i]
            v = int(first_str)
            v -= 1
            t = s[i:]

            while t:
                while len(t) > 1 and t[0] == '0':
                    t = t[1:]

                target = str(v)
                if not t.startswith(target):
                    break

                t = t[len(target):]
                v -= 1

            else:
                return True
        return False









