# Approaching data in a numerical way

# Importing necessary packages
import numpy as np
import pandas as pd

# Reading CSV file
train = pd.read_csv('train.csv')

# Cleaning not numeric relevant data
train_filt = train.drop(columns=['PassengerId', 'Name', 'Ticket', 'Cabin', 'Embarked'])

# First approach

print('Columns: ')
print(train_filt.columns)

print('Describe: ')
print(train_filt.describe())

print('-------------------------------------')
# Only survivors
print('Only Survivors: ')
train_surv = train_filt.query('Survived == 1')

print('Describe: ')
print(train_surv.describe())

print('-------------------------------------')
# Only NOT survivors
print('Only NOT Survivors: ')
train_notsurv = train_filt.query('Survived == 0')

print('Describe: ')
print(train_notsurv.describe())

# Conclusion at this point (about Survivors / Not Surv):
#   Age (apparently) is not a factor. Similar distribution in both cases
#   SibSp in Survivors is more 'compact' than in Not_Surv
#   Parch is similar in both cases, with a little difference in the mean


print('-------------------      ***       ------------------')
train_filt_fem = train_filt.query('Sex == "female"')
print('Female: ')
print(train_filt_fem.describe())

train_filt_male = train_filt.query('Sex == "male"')
print('\n Male: ')
print(train_filt_male.describe())

# Sex is a relevant factor: almost 75% of women survived, but only 19% of men did.

