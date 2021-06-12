'''
HackerRank Problem: Set.add()
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
countries = set()
for i in range(N):
    countries.add(input())
print(len(countries))
'''
Input:
7
UK
China
USA
France
New Zealand
UK
France
Output:
5
'''
