import re

file = open("2.txt")
text = file.readline()

num = r"(?:0|[1-9A-E][0-9A-E]*)"
pattern = re.compile(fr"{num}(?:[+*]{num})*")

exprs = re.findall(pattern, text)
best = max(exprs, key=len)
print(best)

ops = [x for x in best if x in '+*']
nums = best.replace('+', '*').split('*')
nums = [str(int(x, 15)) for x in nums]
expr = ''
for i in range(len(ops)):
    expr += nums[i] + ops[i]
expr += nums[-1]
print(sum(map(int, str(eval(expr)))))