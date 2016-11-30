
# coding: utf-8

# In[3]:

import pandas as pd
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split, cross_val_score


# To begin the machine learning process, a dataframe of players who retired prior to the 2000 season is split into two separate entities - the statistics (explanatory variables) and an array that details whether or not the player has been inducted. These two entities are used as the training data for the machine learning model.

# In[4]:

old_players_HOF_status = pd.read_csv('/data/kensportsfan/hofStatus.csv')
old_players_HOF_status = old_players_HOF_status.set_index('playerID')
assert len(old_players_HOF_status) == 7328
old_players_HOF_status.head()


# In[5]:

y = old_players_HOF_status['inducted']
X = old_players_HOF_status
del X['inducted']
print(X)
print(y)


# To identify a good model, cross validation of a logistic regression model is used to predict whether or not a randomly selected subset of players who are removed from the training data are predicted with high accuracy.

# In[6]:

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
model = LogisticRegression()
model.fit(X_train, y_train)
predicted = model.predict(X_test)
metrics.accuracy_score(y_test, predicted)


# In[7]:

cv_accuracy = cross_val_score(LogisticRegression(), X, y, scoring='accuracy', cv=5)
cv_accuracy


# Since the cross validated data is predicted with high accuracy, the logistic regression model is confirmed to be a good choice. It is now used to predict whether or not the testing data, players who retired between the years of 2000 and 2009, are in the Hall of Fame.

# In[8]:

players_retired_between_2000_2009_inclusive = pd.read_csv('/data/kensportsfan/2000to2009retirees.csv')
players_retired_between_2000_2009_inclusive = players_retired_between_2000_2009_inclusive.set_index('playerID')
hall_of_famers = pd.read_csv('/data/kensportsfan/halloffamers.csv')
hall_of_famers = hall_of_famers.set_index('playerID')


# In[9]:

players_retired_between_2000_2009_inclusive.head()


# In[10]:

hall_of_famers.head()


# In[11]:

eligible_new_players_HOF_status = pd.merge(left=players_retired_between_2000_2009_inclusive, right=hall_of_famers,
                                           left_index=True,right_index=True, how='left')
eligible_new_players_HOF_status = eligible_new_players_HOF_status.fillna('N')
eligible_new_players_HOF_status['inducted'] = eligible_new_players_HOF_status['inducted'].astype('category')
eligible_new_players_HOF_status.head()


# In[12]:

y2 = eligible_new_players_HOF_status['inducted']
X2 = eligible_new_players_HOF_status
del X2['inducted']
print(X2)
print(y2)


# The logistic regression model does quite well, as it predicts whether or not players who retired between the years of 2000 and 2009 are in the Hall of Fame with 97.5% accuracy.

# In[13]:

predicted2 = model.predict(X2)
metrics.accuracy_score(y2, predicted2)


# In[14]:

assert len(pd.Series(y2)) == len(pd.Series(predicted2))


# In[13]:

y2 = pd.Series(y2)
predicted2 = pd.Series(predicted2, index=y2.index)
check_results = pd.concat([y2,predicted2], axis=1)
check_results.columns = ['inducted', 'predicted']
check_results[check_results['inducted'] != check_results['predicted']]


# In[ ]:



