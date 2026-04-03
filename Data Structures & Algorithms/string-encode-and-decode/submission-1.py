class Solution:

    def encode(self, strs: List[str]) -> str:
        algorithm = []
        for s in strs:
            n = len(s)
            code = str(n) + "#" + s
            algorithm.append(code) # But I have to include this algorithm within the string, as it passes stirng onto decode.
        return "".join(algorithm) # 5#Hello5#World
        

    def decode(self, s: str) -> List[str]:
        output = []
        n = len(s)
        i = 0
        num = []
        while i < n:
            if s[i].isdigit():
                num.append(s[i])
                i += 1
            if s[i] == "#":
                if len(num) > 1:
                    number = int("".join(num))
                else: number = int(num[0])
                word = []
                for p in range(number):
                    i += 1
                    word.append(s[i])
                i += 1
                num = []
                output.append("".join(word))
        return output










        