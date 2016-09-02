#정확도
def accuracy(tp, fp, fn, tn):
    correct = tp + tn
    total = tp + fp + fn + tn
    return correct / total


accuracy_ = accuracy(10, 20, 30, 40)
print(accuracy_)

#정밀도
def precision(tp, fp, tn, fn):
    return tp/(tp+fp)

def recall(tp, fp, fn, tn):
    return tp / (tp + fn)

def harmonic_mean(tp, fp, fn, tn):
    p = precision(tp, fp, tn, fn)
    r = recall(tp, fp, fn, tn)
    return 2 * p * r / (p + r)