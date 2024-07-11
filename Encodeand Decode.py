class Solution:
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s):
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res

# Create an instance of the Solution class
solution = Solution()

# List of strings to encode
strs = ["neet", "code", "love", "you"]

# Encode the list of strings
encoded_str = solution.encode(strs)
print(f"Encoded: {encoded_str}")

# Decode the encoded string
decoded_list = solution.decode(encoded_str)
print(f"Decoded: {decoded_list}")
