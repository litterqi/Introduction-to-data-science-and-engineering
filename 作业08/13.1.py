import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import pandas as pd
iris = load_iris()
def mirror(x):
    return iris.target_names[int(x)]
iris.target=list(map(mirror,iris.target))
data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
data['target'] = iris.target
sns.set(style="ticks")
sns.pairplot(data, hue="target")
plt.show()
