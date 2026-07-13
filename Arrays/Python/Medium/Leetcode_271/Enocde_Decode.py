class Solution:  # Container class for the encode and decode string methods
    def encode(self, strs: list[str]) -> str:  # Encodes a list of strings to a single string
        result = ""  # Initialize an empty string to accumulate the encoded output
        for s in strs:  # Iterate over each string in the input list
            # For each string, append its length, a separator '#', and the string itself
            # Example for "abc": append "3#abc" so decoding can recover length and content
            result += str(len(s)) + "#" + s
        return result  # Return the fully concatenated encoded string


    def decode(self, s: str) -> list[str]:  # Decodes a single string back into a list of strings
        result = []  # Initialize the list that will hold decoded strings
        i = 0  # Pointer to traverse the encoded string
        while i < len(s):  # Continue until we've processed the entire encoded string
            j = i  # Start a secondary pointer at the current position to find the separator
            while s[j] != "#":  # Move j forward until we reach the '#' separator
                j += 1
            # The substring s[i:j] represents the length of the next original string
            length = int(s[i:j])  # Convert the length substring to an integer
            # Extract the string content that follows the '#' using the parsed length
            result.append(s[j + 1:j + 1 + length])
            # Move the main pointer i past the current length, separator, and the extracted string
            i = j + 1 + length
        return result  # Return the list of decoded strings

if __name__ == "__main__":
    # Simple test harness to verify encode/decode round-trip behavior
    sol = Solution()

    test_cases = [
        ["hello", "world"],           # normal strings
        ["", ""],                     # empty strings in list
        [],                               # empty list
        ["#", "##", "a#b"],         # strings containing the separator character
        ["こんにちは", "emoji👍"]      # unicode / multi-byte characters
    ]

    for idx, case in enumerate(test_cases, start=1):
        encoded = sol.encode(case)
        decoded = sol.decode(encoded)
        print(f"Test {idx}: original={case} encoded={encoded!r} decoded={decoded}")
        assert decoded == case, f"Round-trip mismatch on test {idx}: got {decoded}"

    print("All encode/decode tests passed.")
