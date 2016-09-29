from sklearn.tree import export_graphviz
import io 
import pydot
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

def draw_dicision_tree(classifier):
    dot_buf = io.StringIO()
    export_graphviz(classifier, out_file=dot_buf, max_depth=5)
    graph = pydot.graph_from_dot_data(dot_buf.getvalue())[0]
    image = graph.create_png()
    image_buf = io.StringIO()
    image_buf.write(image)
    return image(image_buf.getvalue())

def plot_decision_regions(X, y, classifier, title):
    resolution = 0.01
    markers = ('s', '^', 'o', '^', 'v')
    colors = ('red', 'blue', 'green', 'grey', 'cyan')
    cmap = matplotlib.colors.ListedColormap(colors[:len(np.unique(y))])
    
    x1_min, x1_max = X[:, 0].min() - 1, X[:,0].max() + 1
    x2_min, x2_max = X[:, 0].min() - 1, X[:,0].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([]))
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1], alpha=0.8, c=cmap(idx), marker=markers[idx], s=80, label=cl)

    plt.xlabel('petal length [cm]')
    plt.ylabel('petal width [cm]')
    plt.legend(loc='upper left')
    plt.title(title)
    plt.show()
    
