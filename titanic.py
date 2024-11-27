import pandas as pd

data = pd.read_csv('titanic.csv')

# print(data.info())
# print(data.groupby('Sex')['Survived'].mean())

data.drop(['PassengerId','Name','Ticket','Cabin','Embarked'], axis = 1, inplace = True)
print(data.info())

#первая часть очистки
def fill_age(row):
    if pd.isnull(row['Age']):
        if row['Pclass'] == 1:
            return data[data['Pclass'] == 1]['Age'].mean()
        if row['Pclass'] == 2:
            return data[data['Pclass'] == 2]['Age'].mean()
        if row['Pclass'] == 3:
            return data[data['Pclass'] == 3]['Age'].mean()
    return row['Age']

print(data['Pclass'].value_counts())

#Избавляемся от пустоты
data['Age'] = data.apply(fill_age, axis=1)
print(data.info())

def fill_gender(gender):
    if gender == 'male':
        return 1
    return 0

#превращаем в число
data['Sex'] = data['Sex'].apply(fill_gender)
print(data.info())

#вторая часть очистки
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

x = data.drop('Survived', axis=1)  #все данные x 
y = data['Survived']               #целевая аудитория y

x_train, x_test, y_train , y_test = train_test_split(x, y, test_size=0.3) #можно поменять на любое число
classifier.fit(x_train, y_train)

standart = StandardScaler()
x_train = standart.fit_transform(x_train)
x_test = standart.transform(x_test)

classifier = KNeighborsClassifier(n_neighbors=3) #можно поменять на любое число
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)
print('Процент правильных предсказаний:', accuracy_score(y_test, y_pred))
