
# coding: utf-8

# In[1]:

import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# The first step is to get a pandas dataframe of all of the batters who have ever played in Major League Baseball history. Next, the statistics that were not recorded during the early part of baseball history are removed and the statistics will be grouped by player such that each record are a single player's career statistics. The non-counting statistics such as team are removed as well.

# In[2]:

batters = pd.read_csv('/data/kensportsfan/Batting.csv')
batters.head()


# Another pandas dataframe is made for the pitchers, which enables the following set difference to be performed:
# 
# $$ Batters - Pitchers $$
# 
# This removes all pitchers from analysis, which is ideal because many pitchers are in the Hall of Fame for their pitching accomplishments despite mediocre hitting statistics.

# In[3]:

pitchers = pd.read_csv('/data/kensportsfan/Pitching.csv')
batters_only = set(batters.playerID).difference(pitchers.playerID)
batters_by_season = batters[batters.index.isin(batters_only)]


# In[4]:

batters_only = set(batters.playerID).difference(pitchers.playerID)
batters_by_season = batters[batters.playerID.isin(batters_only)]


# In[5]:

del batters_by_season['stint']
del batters_by_season['teamID']
del batters_by_season['lgID']
del batters_by_season['IBB']
del batters_by_season['HBP']
del batters_by_season['SH']
del batters_by_season['SF']
del batters_by_season['GIDP']
del batters_by_season['CS']
del batters_by_season['SO']
batters_by_season.head()


# In[6]:

batters_by_career = batters_by_season.groupby('playerID').sum()
assert len(batters_by_career) == 9429
batters_by_career = batters_by_career.dropna()
assert len(batters_by_career) == 9245
batters_by_career.head()


# In[7]:

assert 'aaronha01' in batters_by_career.index #Hank Aaron
assert 'bondsba01' in batters_by_career.index #Barry Bonds
assert batters_by_career.loc['aaronha01','HR'] == 755 #Hank Aaron hit 755 Career HR
assert batters_by_career.loc['mayswi01','HR'] == 660 #Willie Mays hit 660 Career HR
assert batters_by_career.loc['henderi01','SB'] == 1406 #Rickey Henderson had 1406 Career SB


# The goal is to break the players into three distinct dataframes:
# * Players who retired before the year 2000
# * Players who have played since the year 2000 but retired before the 2010 season
# * Players who have played since the year 2010
# 
# This first group will be joined with the Hall of Fame dataframe, which has information on which players are in the Hall of Fame. Then this group will be used as the training data for building a model that predict whether or not a player in the second group has been inducted into the Hall of Fame based on their hitting statistics. The third group is removed from analysis since they are not yet eligible to be elected into the Hall of Fame.

# In[8]:

batters_before_2000 = batters_by_season[batters_by_season['yearID'] < 2000]
assert len(batters_before_2000) == 42669
batters_before_2000 = batters_before_2000.dropna()
assert len(batters_before_2000) == 41764
batters_since_2000 = batters_by_season[batters_by_season['yearID'] >= 2000]
assert len(batters_since_2000) == 9460
batters_since_2010 = batters_by_season[batters_by_season['yearID'] >= 2010]
assert len(batters_since_2010) == 3129
batters_since_2010.head()


# The three dataframes are each grouped by playerID so that each player only appears once and has the sum of their statistics (career statistics) during that time frame shown.

# In[9]:

career_stats_before_2000 = batters_before_2000.groupby('playerID').sum()
del career_stats_before_2000['yearID']
career_stats_before_2000.head()


# In[10]:

career_stats_since_2000 = batters_since_2000.groupby('playerID').sum()
del career_stats_since_2000['yearID']
career_stats_since_2000.head()


# In[11]:

career_stats_since_2010 = batters_since_2010.groupby('playerID').sum()
del career_stats_since_2010['yearID']
career_stats_since_2010.head()


# In[12]:

old_player_list = set(batters_by_career.index).difference(career_stats_since_2000.index)
players_retired_before_2000 = career_stats_before_2000[career_stats_before_2000.index.isin(old_player_list)]

new_player_list = set(batters_by_career.index).difference(players_retired_before_2000.index)
players_retired_since_2000 = batters_by_career[batters_by_career.index.isin(new_player_list)]

eligible_new_player_list = set(players_retired_since_2000.index).difference(career_stats_since_2010.index)
players_retired_between_2000_2009_inclusive = players_retired_since_2000[players_retired_since_2000.index.isin(eligible_new_player_list)]
del players_retired_between_2000_2009_inclusive['yearID']
players_retired_between_2000_2009_inclusive.to_csv(path_or_buf='/data/kensportsfan/2000to2009retirees.csv')

assert 'aaronha01' in players_retired_before_2000.index #Hank Aaron
assert 'bondsba01' in players_retired_between_2000_2009_inclusive.index #Barry Bonds


# A Hall of Fame dataframe is created with players who have been elected.

# In[13]:

hall_of_fame_voting = pd.read_csv('/data/kensportsfan/HallOfFame.csv')
hall_of_famers = hall_of_fame_voting[hall_of_fame_voting['inducted'] == 'Y']
hall_of_famers = hall_of_famers[['playerID','inducted']]
hall_of_famers = hall_of_famers.set_index('playerID')
hall_of_famers.to_csv(path_or_buf='/data/kensportsfan/halloffamers.csv')

assert 'gwynnto01' in hall_of_famers.index #Tony Gwynn
assert 'biggicr01' in hall_of_famers.index #Craig Biggio


# The dataframe of players who retired prior to the 2000 season is left joined with the Hall of Fame dataframe. Players who are in the Hall of Fame have a 'Y' in the inducted column, while players not in the Hall of Fame dataframe have a NaN in the inducted column. These NaN values are replaced with 'N'.

# In[14]:

old_players_HOF_status = pd.merge(left=players_retired_before_2000, right=hall_of_famers, left_index=True, right_index=True, how='left')
old_players_HOF_status = old_players_HOF_status.fillna('N')
assert len(old_players_HOF_status) == 7328
old_players_HOF_status['inducted'] = old_players_HOF_status['inducted'].astype('category')
old_players_HOF_status.to_csv(path_or_buf='/data/kensportsfan/hofStatus.csv')
old_players_HOF_status.head()


# Now that all null values have been replaced, the players are grouped by whether or not they are inducted into the Hall of Fame. The players in the Hall of Fame average many more of each statistic than the players not in the Hall of Fame.

# In[15]:

old_players_HOF_status_gb = old_players_HOF_status.groupby('inducted').mean()
old_players_HOF_status_gb


# Comparing the quantities of players with different levels of each statistic, the majority of players not in the Hall of Fame fall into the lowest interval, while very few Hall of Famers fall into the lowest interval. Subsequent intervals see a sharp decrease in number of non Hall of Famers while also seeing a slight increase in the number of Hall of Famers. Each player is assigned to the bin closest to their respective quantity. For example:
# * A player with 20 G will be assigned to the 0 G bin
# * A player with 600 G will be assigned to the 1000 G bin
# * A player with 1400 G will be assigned to the 1000 G bin
# * A player with 2200 G will be assigned to the 2000 G bin

# In[16]:

old_players_HOF_status_rounded = old_players_HOF_status.round({'G': -3, 'AB': -4, 'H': -3, 'HR': -3, 'SB': -3, 'BB': -3})
pd.crosstab(old_players_HOF_status_rounded.G, old_players_HOF_status_rounded.inducted).plot(kind='bar')
plt.ylabel('Number of Players');


# In[17]:

pd.crosstab(old_players_HOF_status_rounded.AB, old_players_HOF_status_rounded.inducted).plot(kind='bar')
plt.ylabel('Number of Players');


# In[18]:

pd.crosstab(old_players_HOF_status_rounded.H, old_players_HOF_status_rounded.inducted).plot(kind='bar')
plt.ylabel('Number of Players');


# In[19]:

pd.crosstab(old_players_HOF_status_rounded.HR, old_players_HOF_status_rounded.inducted).plot(kind='bar')
plt.ylabel('Number of Players');


# In[20]:

pd.crosstab(old_players_HOF_status_rounded.SB, old_players_HOF_status_rounded.inducted).plot(kind='bar')
plt.ylabel('Number of Players');


# In[21]:

pd.crosstab(old_players_HOF_status_rounded.BB, old_players_HOF_status_rounded.inducted).plot(kind='bar')
plt.ylabel('Number of Players');

