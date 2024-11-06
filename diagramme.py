import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('GoogleApps.csv')

# Гистограмма
size_info = data['Size']
size_info.plot(kind='hist')
# Ящик с усами 
#paid = data[data['Type'] == 'Free']['Rating']
#paid.plot(kind='box')
# Диаграма Рассеяния
#data.plot(x = 'Installs', y = 'Size', kind='scatter')
# Круговая диаграма
#category = data['Category'].value_counts()
#content = data['Content Rating'].value_counts()
#category.plot(kind='pie')
# Столбчатая диаграмма
#category.plot(kind='barh')
table = data.pivot_table(
    index='Content Rating',
    columns='Type',
    values='Rating',
    aggfunc='mean'
)
table.plot(kind='barh', subplots= True)


plt.show()
