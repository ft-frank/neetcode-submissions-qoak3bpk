class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            n = len(s)
            new =  str(n) + '#' + s
            encoded.append(new)
        return "".join(encoded)
    def decode(self, s: str) -> List[str]:
        output = []
        n = len(s)
        i = 0
        next_word = []
        num = []
        while i < n:
            
            if s[i].isdigit():
                num.append(s[i])
            elif s[i] == "#":
                length = "".join(num)
                length = int(length)

                for j in range(length):
                    i += 1
                    next_word.append(s[i])

                new_word = "".join(next_word)

                output.append(new_word)
                next_word = []
                num = []
                



            i += 1
        return output

