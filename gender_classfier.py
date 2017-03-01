from sklearn import tree

#array for body size
X = [[185, 58, 22], [152, 65, 23], [190, 78, 31], [155, 70, 35], [176, 61, 22],
     [160, 61, 24], [156, 55, 24], [189, 61, 22], [154, 59, 31], [180, 74, 31],
     [183, 55, 22]]

#array for male or female
Y = ['female', 'female', 'male', 'male', 'female', 'female', 'female', 'female',
     'female', 'male', 'female']


clf = tree.DecisionTreeClassifier()

clf = clf.fit(X, Y)

prediction = clf.predict([180, 72, 32])

print prediction