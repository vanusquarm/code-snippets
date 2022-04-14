from sklearn.linear_model import RidgeClassifier
features = [[5, 3.4, 6], [1, 9.4, 10], [2, 0.1, 1]]
target = [0, 1, 1]

# Used alpha parameter in model creation
clf = RidgeClassifier(alpha=3.0).fit(
features, target
)

# Score model with features and target
print(clf.score(features, target))

# Predict new values based on features
print(clf.predict(features))

# output 
1.0
[0 1 1]
