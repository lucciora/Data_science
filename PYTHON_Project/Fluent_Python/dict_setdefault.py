import re
WORD_RE=re.compile('\w+')
texts='''Thank you for applying for the AWS Educate program. 
Unfortunately, after careful review, your application was
 not approved for the following reason(s)'''
index={}

for line_no, line in enumerate(texts,1):
    for match in WORD_RE.finditer(line):
        print(line)
        print(line_no)
        word = match.group()
        print(word)
        print("---")
            
 