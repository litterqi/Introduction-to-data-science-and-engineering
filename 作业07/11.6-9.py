import numpy as np
from sklearn import linear_model,metrics
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from sklearn.datasets import load_iris

iris_dataset=load_iris()
X=iris_dataset['data']
Y=iris_dataset['target']
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.7,random_state=20,shuffle=True)

logistic_rg=linear_model.LogisticRegression()
logistic_rg.fit(x_train,y_train)
pred=logistic_rg.predict(x_test)
print('accuracy for logistic regression:',metrics.accuracy_score(y_test,pred))

target0=X[:50]
target1=X[50:100]
target2=X[100:]
center0=np.mean(target0[:,0:4],axis=0)
center1=np.mean(target1[:,0:4],axis=0)
center2=np.mean(target2[:,0:4],axis=0)
print('中心点依次是：',center0,center1,center2)

distance0=[]
distance1=[]
distance2=[]
print("target=0到中心点的距离:")
for vec in target0:
    distance0.append(np.sqrt(np.sum(np.square(vec-center0))))
print(distance0)
print("target=1到中心点的距离:")
for vec in target1:
    distance1.append(np.sqrt(np.sum(np.square(vec-center1))))
print(distance1)
print("target=2到中心点的距离:")
for vec in target2:
    distance2.append(np.sqrt(np.sum(np.square(vec-center2))))
print(distance2)

from sklearn.cluster import KMeans
kmeans=KMeans(n_clusters=3,random_state=1)
kmeans.fit(x_train,y_train)
pred=kmeans.predict(x_test)
print(kmeans.cluster_centers_)
print('accuracy for kmeans',metrics.accuracy_score(pred,y_test))   