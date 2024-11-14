# # fruits = ['apple', 'banana', 'mango']
# # for index, fruit in enumerate(fruits, start=1):
# #     print(index, fruit)
# from typing import List

# class Solution:
#     def findPeakElement(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n == 1:
#             return 0
#         low, high = 0, n - 1
        
#         while low <= high:
#             mid = (low + high) // 2
            
#             # Check if mid is a peak element
#             if (mid == 0 or nums[mid] > nums[mid - 1]) and (mid == n - 1 or nums[mid] > nums[mid + 1]):
#                 return mid
#             # If the element on the left is greater, then move towards the left side
#             elif mid > 0 and nums[mid - 1] > nums[mid]:
#                 high = mid - 1
#             # If the element on the right is greater, then move towards the right side
#             else:
#                 low = mid + 1
        
#         return -1  # This should never be reached if the input is valid

# if __name__ == "__main__":
#     ps = Solution()
#     num = [1, 2, 1, 3, 5, 6, 4]
#     print(f"Here is the index: {ps.findPeakElement(num)}")
# class solution:
#     def squrt(self, n):
#         ans = 1
#         for i in range(n):
#             if i*i <= n:
#                 ans = i
#             else:
#                 break
# if __name__ == "__main__":
#     pio = solution()
#     ni = 2
#     print(f"here is the answwer: {pio(ni)}")
# class Solution:
#     def power(self, mid, n, m):
#         ans = 1
#         for i in range(n):
#             ans = ans*mid
#             if ans>m:
#                 return 2
#         if ans == m:
#             return 1
#         return 0
#     def NthRoot(self, n, m):
# 		# Code here
#           low = 1
#           high = m
# 		while low<= high:
# 		    mid = (low+high)//2
# 		    midn = power(mid, n, m)
# 		    if midn == 1:
# 		        return mid
# 		    elif midn == 0:
# 		        low = mid+1
# 		    else:
# 		        high = mid-1
# n = int(input())
# for i in range(n):
#     for j in range(n-1-i):
#         print(" ",end="")
#     for j in range(2*i+1):
#         print("*",end="")
#     print()
# def minimize_max_distance(arr, k):
#     n = len(arr)
#     how_many = [0] * (n - 1)

#     for gas_stations in range(1, k):
#         max_section = -1
#         max_ind = -1
        
#         # Find the largest section to split
#         for i in range(n - 1):
#             diff = arr[i + 1] - arr[i]
#             section_length = diff / (how_many[i] + 1)  # Note: how_many[i] + 1 because we are splitting this section
            
#             if section_length > max_section:
#                 max_section = section_length
#                 max_ind = i
        
#         # Increment the count of gas stations in the chosen section
#         how_many[max_ind] += 1

#     # Calculate the maximum distance after placing all gas stations
#     max_ans = -1
#     for i in range(n - 1):
#         diff = arr[i + 1] - arr[i]
#         section_length = diff / (how_many[i] + 1)  # Final length after all splits
#         max_ans = max(max_ans, section_length)

#     return max_ans

# # Example usage
# arr = [0, 10, 20, 30]
# k = 2
# result = minimize_max_distance(arr, k)
# print(f"The minimized maximum distance is: {result}")
# n = int(input())
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(i):
#         print("*",end="")
#     for j in range(i-1):
#         print("*",end="")
#     for j in range((n-1)-i+1):
#         print(" ",end= "")
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end="")
#     for j in range(n-i-1):
#         print("*",end="")
#     for j in range((n-i)-2):
#         print("*",end="")
#     for j in range(i+1):
#         print(" ",end= "")
#     print()
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(i+1):
#         print(j+1,end="")
#     for j in range(i):
#         print((j)-i+(n-1),end="")
#     print()
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         # Split the string into words
#         words = s.split()
#         # Reverse the list of words
#         words.reverse()
#         # Join the words back into a string
#         return ' '.join(words)

# if __name__ == "__main__":
#     sd = Solution()
#     n = "my name is chik chik chik slim shady"
#     result = sd.reverseWords(n)
#     print(f"Reversed: {result}")
# Solution: Bubble Sort
# Solution: Palindrome Check
# def bubblesort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(n-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#     return arr
# print(bubblesort([5,6,7,12,89,53,65]))
# def pallindrom(s):
#     s = ''.join(e for e in s if e.isalnum()).lower()
#     return s ==  s[::-1]
# print(pallindrom("HelleH"))
# def fibbonaci(n):
#     fib = [0,1]
#     for i in range(2,n):
#         fib.append(fib[i-1]+fib[i-2])
#     return fib[:n]
# print(fibbonaci(10))
# def multi_mat(A,B):
#     row_A = len(A)
#     col_A = len(A[0])
#     row_B = len(B)
#     col_B = len(B[0])
#     if col_A!=row_B:
#         return "Can't Multiply this matrix"
#     result = [[0 for _ in range(col_B)]for _ in range(row_A)]
#     for i in range(row_A):
#         for j in range(col_B):
#             for k in range(col_A):
#                 result[i][j]+= A[i][k]*B[k][j]
#     return result
# A = [[1, 2], [3, 4]]
# B = [[5, 6], [7, 8]]
# print(multi_mat(A,B))
# def hcf(a,b):
#     while b:
#         a,b = b,a%b
#     return a
# num_1 = 80
# num_2 = 2
# result = hcf(num_1,num_2)
# print(f"HCF of {num_1} by {num_2} is {result}")
# def reverse_no(s):
#     word = s.split()
#     word.reverse()
#     return ' '.join(word)
# print(reverse_no("mera naam junjun"))
# def check_prime(n):
#     for i in range(1,9):
#         if n%i == 0:
#          return False
#         else:
#            return True
# print(check_prime(7))
n = 101
dp = [0]*(n)
dp[0]=0
dp[1]=1
for i in range(2,n):
    dp[n]=dp[n-1]+dp[n-2]
print(dp[7])