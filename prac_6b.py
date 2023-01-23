from sklearn.cluster import KMeans
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score

datasets = datasets.load_iris()
X = datasets.data
Y = datasets.target

print(X,Y)

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
# print(x_train, x_test, y_train, y_test)

for i in range(1,11):
    model = KMeans(n_clusters=4)
    model.fit(x_train, y_train)

p = model.predict(x_test)
print(p)

print(confusion_matrix(y_test, p))
print(accuracy_score(y_test, p) * 100)
