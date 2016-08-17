import sys, re

# data의 in, out 포맷

print(sys.stdin)
print(sys.stdout)

regex = sys.argv
print(regex)

for line in sys.stdin:
    if re.search(regex, line):
       print(sys.stdout.write(line))
