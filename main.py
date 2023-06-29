class Solution:
	def isDivisible(self, s):
		# code here
		if int(s,2)%3==0:
		    return 1
		return 0

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution()
		ans = ob.isDivisible(s)
		print(ans)
