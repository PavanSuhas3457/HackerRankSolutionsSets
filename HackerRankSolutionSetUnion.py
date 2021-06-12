'''
HackerRank: Set Union() Operation
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
N1 = int(input())
storage1 = set(input().split());
N2 = int(input())
storage2 = set(input().split());
storage3 = storage1.union(storage2)
print(len(storage3))
'''
Input:
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
Output:
13
'''
