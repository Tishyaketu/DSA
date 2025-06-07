class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = []
        pq = [(-count,char) for char,count in Counter(s).items()]
        heapify(pq)
        while pq:
          first_count, first_char = heappop(pq)
          if not ans or first_char!=ans[-1]:
            ans.append(first_char)
            if first_count+1!=0:
              heappush(pq,(first_count+1,first_char))
          else:
            if not pq: return ''
            second_count, second_char = heappop(pq)
            ans.append(second_char)
            if second_count+1!=0:
              heappush(pq,(second_count+1,second_char))
            heappush(pq,(first_count,first_char))
        return ''.join(ans)