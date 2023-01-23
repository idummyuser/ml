# Prac 1a - Linear Regression Model

print("------------------------------------------------------")
import random
from sklearn.linear_model import LinearRegression

print("train the data")
print("------------------------------------------------------")
feature_set = []
target_set = []
no_of_rows = 200
limit = 2000
for i in range(0, no_of_rows):
    x = random.randint(0, limit)
    y = random.randint(0, limit)
    z = random.randint(0, limit)
    g = 10 * x + 2 * y + 3 * z
    print("x=", x, "\ty=", y, "\tz=", z, "\tg=", g)
    feature_set.append([x, y, z])
    target_set.append(g)

print("Here training the model begins")
model = LinearRegression()
model.fit(feature_set, target_set)
print("Here training the model ends")

print("testing the model begins")
test_data = [[1, 1, 3]]
print("testing data:", test_data)
prediction = model.predict(test_data)

print("prediction: ", prediction, "\tcoeffecient:", str(model.coef_))
