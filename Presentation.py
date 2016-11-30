
# coding: utf-8

# # Predicting Major League Baseball Hall of Famers

# In[1]:

import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split, cross_val_score


# ### Career Statisctics by Player

# Players who retired before the 2000 season are used as training data to build the model.

# In[2]:

old_players_HOF_status = pd.read_csv('/data/kensportsfan/hofStatus.csv')
old_players_HOF_status.head()


# ### Hall of Fame Players vs. non Hall of Fame Players

# In[3]:

old_players_HOF_status_gb = old_players_HOF_status.groupby('inducted').mean()
old_players_HOF_status_gb


# In[4]:

old_players_HOF_status_rounded = old_players_HOF_status.round({'G': -3, 'AB': -4, 'H': -3, 'HR': -3, 'SB': -3, 'BB': -3})


# In[5]:

pd.crosstab(old_players_HOF_status_rounded.G, old_players_HOF_status_rounded.inducted).plot(kind='bar')
plt.ylabel('Number of Players');


# In[6]:

pd.crosstab(old_players_HOF_status_rounded.AB, old_players_HOF_status_rounded.inducted).plot(kind='bar')
plt.ylabel('Number of Players');


# In[7]:

pd.crosstab(old_players_HOF_status_rounded.H, old_players_HOF_status_rounded.inducted).plot(kind='bar')
plt.ylabel('Number of Players');


# In[8]:

pd.crosstab(old_players_HOF_status_rounded.HR, old_players_HOF_status_rounded.inducted).plot(kind='bar')
plt.ylabel('Number of Players');


# In[9]:

pd.crosstab(old_players_HOF_status_rounded.SB, old_players_HOF_status_rounded.inducted).plot(kind='bar')
plt.ylabel('Number of Players');


# In[10]:

pd.crosstab(old_players_HOF_status_rounded.BB, old_players_HOF_status_rounded.inducted).plot(kind='bar')
plt.ylabel('Number of Players');


# ### Machine Learning

# In[11]:

old_players_HOF_status = pd.read_csv('/data/kensportsfan/hofStatus.csv')
old_players_HOF_status = old_players_HOF_status.set_index('playerID')
old_players_HOF_status.head()


# In[12]:

y = old_players_HOF_status['inducted']
X = old_players_HOF_status
del X['inducted']
print(X)
print(y)


# To identify a good model, cross validation of a logistic regression model is used to predict whether or not a randomly selected subset of players who are removed from the training data are predicted with high accuracy.

# In[13]:

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
model = LogisticRegression()
model.fit(X_train, y_train)
predicted = model.predict(X_test)
metrics.accuracy_score(y_test, predicted)


# In[14]:

cv_accuracy = cross_val_score(LogisticRegression(), X, y, scoring='accuracy', cv=5)
cv_accuracy


# Since the cross validated data is predicted with high accuracy, the logistic regression model is confirmed to be a good choice. It is now used to predict whether or not the testing data, players who retired between the years of 2000 and 2009, are in the Hall of Fame.

# In[15]:

players_retired_between_2000_2009_inclusive = pd.read_csv('/data/kensportsfan/2000to2009retirees.csv')
players_retired_between_2000_2009_inclusive = players_retired_between_2000_2009_inclusive.set_index('playerID')
hall_of_famers = pd.read_csv('/data/kensportsfan/halloffamers.csv')
hall_of_famers = hall_of_famers.set_index('playerID')


# In[16]:

eligible_new_players_HOF_status = pd.merge(left=players_retired_between_2000_2009_inclusive, right=hall_of_famers,
                                           left_index=True,right_index=True, how='left')
eligible_new_players_HOF_status = eligible_new_players_HOF_status.fillna('N')
eligible_new_players_HOF_status['inducted'] = eligible_new_players_HOF_status['inducted'].astype('category')
eligible_new_players_HOF_status.head()


# In[17]:

y2 = eligible_new_players_HOF_status['inducted']
X2 = eligible_new_players_HOF_status
del X2['inducted']
print(X2)
print(y2)


# The logistic regression model does quite well, as it predicts whether or not players who retired between the years of 2000 and 2009 are in the Hall of Fame with 97.5% accuracy.

# In[18]:

predicted2 = model.predict(X2)
metrics.accuracy_score(y2, predicted2)


# In[19]:

probs = model.predict_proba(X2)
hof_prob = []
for item in probs:
    hof_prob.append(item[1])


# ### Relationship between individual statistics and Hall of Fame likelihood

# In[20]:

plt.scatter(x=eligible_new_players_HOF_status.G,y=hof_prob);


# In[21]:

plt.scatter(x=eligible_new_players_HOF_status.AB,y=hof_prob);


# In[22]:

plt.scatter(x=eligible_new_players_HOF_status.H,y=hof_prob);


# In[23]:

plt.scatter(x=eligible_new_players_HOF_status.HR,y=hof_prob);


# In[24]:

plt.scatter(x=eligible_new_players_HOF_status.SB,y=hof_prob);


# In[25]:

plt.scatter(x=eligible_new_players_HOF_status.BB,y=hof_prob);


# ### Recap: Areas for Improvement
# * False positives for Hall of Fame are largely suspected steroid users
# * False negatives for Hall of Fame are players who played 'premium' positions that tended to have lower statistics

# In[26]:

y2 = pd.Series(y2)
predicted2 = pd.Series(predicted2, index=y2.index)
check_results = pd.concat([y2,predicted2], axis=1)
check_results.columns = ['inducted', 'predicted']
check_results[check_results['inducted'] != check_results['predicted']]


# In[ ]:



