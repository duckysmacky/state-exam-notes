file = open('24.txt')
text = file.readline()

def count(s):
    cnt = 0
    for l in 'AEIOUY':
        cnt += s.count(l)
    return cnt

max_substr = ''
strs = text.split('.')
for str_ in strs:
    i, j = 0, 0
    while len(str_) >= j >= i:
        substr = str_[i:j + 1]
        if count(substr) <= 7:
            max_substr = max(max_substr, substr, key=len)
            j += 1
        else:
            i += 1
print(max_substr)
print(len(max_substr), count(max_substr))