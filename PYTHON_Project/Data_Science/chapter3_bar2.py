from random import randint
from collections import Counter
from matplotlib import pyplot
grades = [randint(1,100) for _ in range(100)]
print(grades)
decile = lambda grade: grade//10*10
histogram = Counter(decile(grade) for grade in grades)
pyplot.bar([x-4 for x in histogram.keys()], histogram.values(), 10)
pyplot.axis([-5, 105, 0, max(histogram.values())+1])
pyplot.xticks([10*i for i in range(11)])
pyplot.xlabel("Decile")
pyplot.ylabel("# of Students")
pyplot.title("Distribution of Exam 1 Grades")
pyplot.show()