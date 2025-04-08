class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # Initialize the index and get the length of the input string
        index, length = 0, len(s)
        # This list will store the counts of consecutive '0's or '1's
        group_counts = []
      
        # Loop through the input string to create group counts
        while index < length:
            count = 1
            # If the next character is the same, increment the count
            while index + 1 < length and s[index + 1] == s[index]:
                count += 1
                index += 1
            # Append the count of the group to the list
            group_counts.append(count)
            index += 1
      
        # Initialize the answer variable to store the total count
        answer = 0
        # Iterate over the group counts and add the minimum count of
        # adjacent groups to the answer since they can form binary substrings
        for i in range(1, len(group_counts)):
            answer += min(group_counts[i - 1], group_counts[i])
      
        # Return the total count of binary substrings
        return answer
