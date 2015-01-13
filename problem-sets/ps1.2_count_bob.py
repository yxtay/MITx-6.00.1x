# Paste your code into this box 

s = 'azcbobobegghakl' # 2
# s = 'bobobob' # 3

sScan = 'bob'
count = 0
for idx in range(len(s) - len(sScan) + 1):
    if s[idx:(idx + len(sScan))] == sScan:
        count += 1

print("Number of times bob occurs is: %d" % count)