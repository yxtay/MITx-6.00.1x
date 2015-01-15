# Paste your code into this box

# s = 'azcbobobegghakl' # beggh
s = 'abcbcd' # abc
# s = 'abcdefghijklmnopqrstuvwxyz' # abcdefghijklmnopqrstuvwxyz

longest_str = s[0]

i = 1
anchor = i - 1
while i < len(s):
    if s[i - 1] <= s[i]:
        if i - anchor + 1 > len(longest_str):
            longest_str = s[anchor:i + 1]
    else:
        anchor = i
        if len(s) - anchor <= len(longest_str):
            break
        
    i += 1
print("Longest substring in alphabetical order is: %s" % longest_str)