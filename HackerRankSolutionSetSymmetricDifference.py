# Enter your code here. Read input from STDIN. Print output to STDOUT
n1 = int(input())
E = list(map(int,input().strip().split()))[:n1]
n2 = int(input())
F = list(map(int,input().strip().split()))[:n2]
English = set(E)
French = set(F)
print(len(English.symmetric_difference(French)))
'''
Input:
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
Output:
8
'''
