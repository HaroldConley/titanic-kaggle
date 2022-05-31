# Plotting info to get a general idea of the data available

# Importing necessary packages

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()

# Reading csv file
train = pd.read_csv('train.csv')


print(train.columns)

# Survivor and No Survivors ages by gender
g=sns.boxplot(x='Survived', y='Age', data=train, hue='Sex')
g.set_title('Ages Distribution')
plt.show()
plt.close()

# How much people survived by Class?
sns.set_palette(['grey', 'silver'])
g1=sns.countplot(x='Pclass', data=train, hue='Survived')
g1.set_title('Survivors by Class')
plt.show()
plt.close()

# Survivors Ages distribution by Class and Sex
sns.set_theme(style="darkgrid")
sns.displot(
    data=train, x='Age', col='Pclass', row='Sex', hue='Survived',
    binwidth=3, height=3, facet_kws=dict(margin_titles=True),
)
plt.show()
plt.close()

print('The End')
