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
'''
