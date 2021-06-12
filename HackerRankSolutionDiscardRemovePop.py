'''
HackerRank Problem: Set Discard() Remove() and Pop()
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
set1 = set(map(int,input().split()))
for i in range(int(input())):
    samp = input().split()
    if samp[0] == 'remove':
        set1.remove(int(samp[1]))
    elif samp[0] == 'discard':
        set1.discard(int(samp[1]))
    else:
        set1.pop()
print(sum(list(set1)))
'''
Input:
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop
discard 6
remove 5
pop
discard 5
Output:
4
'''
