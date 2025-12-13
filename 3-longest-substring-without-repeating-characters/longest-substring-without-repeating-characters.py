class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0 # actual answer
        mp={} # hasmap to keep track of every occured character's next index
        i=0 # starting point of sliding window
        n=len(s)
        for j in range(n): # ending point of sliding window
          if s[j] in mp: # checking if last chara of sliding window is already present in hashmap
            i=max(i,mp[s[j]]) #if yes setting the start point to the last char's next index
          ans=max(ans,j-i+1) # calculating ans based on curr sliding window len & max len
          mp[s[j]]=j+1 # creating / updating sliding window's last char's next index
        return ans