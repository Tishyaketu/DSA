class Solution:
    def myAtoi(self, s: str) -> int:
        sign=True
        result=0
        index=0
        n=len(s)
        INT_MAX= pow(2,31)-1
        INT_MIN= -pow(2,31)
        while index<n and s[index]==' ':index+=1
        
        if index<n and s[index]=='-':
          sign=False
          index+=1
        
        elif index<n and s[index]=='+':index+=1
        
        while index<n and s[index].isdigit():
          d=int(s[index])
          if ((result>INT_MAX//10) or (result==INT_MAX//10 and d>INT_MAX%10)):
            return INT_MAX if sign else INT_MIN
          result=(result*10)+d
          index+=1
        
        return result if sign else (-1)*result