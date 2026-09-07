class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0 # The best window size found so far
        l = 0 # Left edge of the window.
        counts = [0] * 26 # A list of 26 zeros, one slot per letter of the alphabet

        for r in range(len(s)): # Right edge moves forward one character at a time
            counts[ord(s[r]) - 65] += 1 # Add the new letter to the tally.

# ord() gives a character's number code. ord('A') is 65, ord('B') is 66, up to ord('Z') = 90.

            while (r-l+1) - max(counts) > k: # legality check
                counts[ord(s[l]) - 65] -= 1 #Shrinking from the left means the leftmost letter leaves the window, so remove it from the tally.

                l += 1 # Move the left edge right. Window is one narrower, the while re-checks.
            longest = max(longest, (r-l+1)) # measure it and keep the record if it's bigger.

        return longest

        # Time: O(n)