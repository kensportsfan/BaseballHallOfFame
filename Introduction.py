
# coding: utf-8

# # Abstract

# No American sport cherishes its history quite like Major League Baseball. Known as the participants of America's pastime, Major League Baseball legends play an important role not just in American sports but also in American society. Baseball statisticians have relentlessly documented data from games, and after hundreds of years of such documentation, many records have been set, broken and broken again. Perhaps held in even a higher esteem than these records, however, is the accomplishment of making it into the Baseball Hall of Fame. Each year, the baseball world engages in a passionate discussion regarding which players will and won't make the cut to earn baseball's greatest honor. This project involves building a predictive model to determine which hitters will make the Hall of Fame based on their career statistics.

# # Description of the dataset

# The original data consists of three csv file datasets:
# * Batting.csv
# * HallOfFame.csv
# * Pitching.csv
# 
# The core file is the Batting dataset, as it contains all hitting information for each player since 1871, grouped by season. The pitching dataset is used to remove pitchers from the analysis, since their Hall of Fame candidacy will not be based on their (often mediocre) hitting statistics. A Hall of Fame pitcher could likely have very poor hitting statistics, so including them in the model would throw off the model's ability to properly assess Hall of Fame quality hitting. After removing the pitchers from the analysis, the remaining players are joined with the HallOfFame dataset to identify each player as a Hall of Famer or a non Hall of Famer.

# # Index

# Notebooks:
# * _Introduction.ipynb_ - Gives background and details about the analysis and data being used
# * _DataCleaning&Analysis.ipynb_ - Takes data from the original three datasets (Batting, HallOfFame, Pitching) and cleans it in preparation for machine learning
# * _MachineLearning.ipynb_ - Runs logistic regression to predict whether or not players who retired from 2000-2009 are in the Hall of Fame based on training data of players who retired prior to the 2000 season
# * _Presentation.ipynb_ - Displays model results/conclusions, describes what went well and what could have been done differently

# In[ ]:



