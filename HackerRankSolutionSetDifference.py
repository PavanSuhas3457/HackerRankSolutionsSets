'''
HackerRank Problem: Set Difference()
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
num1 = int(input())
set1 = set(input().split())
num2 = int(input())
set2 = set(input().split())
print(len(set1.difference(set2)))
'''
Input:
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
Output:
4
'''
