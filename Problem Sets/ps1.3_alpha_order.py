# Paste your code into this box

s = 'azcbobobegghakl'

longest_str = s[0]
max_length = len(longest_str)

i = 0
while i < len(s) - max_length:
    j = 2
    current_str = s[i:(i + j)]
    while current_str[-1] >= current_str[-2] and j <= len(s) - i:
        j += 1
        current_str = s[i:(i + j)]
    
    if j > max_length:
        max_length = j
        longest_str = current_str[:j - 1]
        
    i += 1
        
print("Longest substring in alphabetical order is: %s" % longest_str)