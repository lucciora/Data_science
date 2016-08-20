import sys
from collections import Counter
import codecs



try:
    with codecs.open('typing.txt', 'r', encoding="utf-8") as f:
        print("file opend")
        counter = Counter(word.lower()
                  for line in f.readlines() for word in line.strip().split()
                  if word)
        print(counter)
except:
    print("usage:most_common_words")
    sys.exit(1) # non-zeor exit code indicates error!
    

