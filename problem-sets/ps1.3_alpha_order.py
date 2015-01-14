# Paste your code into this box

s = 'azcbobobegghakl' # beggh
# s = 'abcbcd' # abc
# s = 'abcdefghijklmnopqrstuvwxyz' # abcdefghijklmnopqrstuvwxyz

longest_str = s[0]
max_length = 1

i = 1
anchor = i - 1
while i < len(s):
    if s[i - 1] <= s[i]:
        if i - anchor + 1 > len(longest_str):
            longest_str = s[anchor:i + 1]
    else:
        anchor = i
    
    # j = 2
    # current_str = s[i:(i + j)]
    # while current_str[-1] >= current_str[-2] and j <= len(s) - i:
        # j += 1
        # current_str = s[i:(i + j)]
    
    # if j > max_length:
        # max_length = j
        # longest_str = current_str[:j - 1]
        
    i += 1
        
print("Longest substring in alphabetical order is: %s" % longest_str)