from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
#[height, weight, shoe size]
X= [[182,80,44], [177, 70, 43], [160, 60,38], [154, 54, 37],
    [166,65,40], [190,90,47], [175,64,39], [177,70,40], [159,55,36],
    [171,75,42], [181,85,43]]


Y= ['male','female', 'female', 'female','male','male',
    'male', 'female', 'male', 'female', 'male']

# Can choose three different classifiers
clf = KNeighborsClassifier()

clf = clf.fit(X,Y)
prediction = clf.predict([[180,88,44]])

print prediction


