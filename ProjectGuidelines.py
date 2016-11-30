
# coding: utf-8

# # Project Guidelines

# ## Overview

# This document describes the final projects that you will do for this course. These projects will build on your existing knowledge and take you to the next level with your skills in coding, software engineering, visualization, debugging, algorithmic thinking, etc.
# 
# What is the difference between this project and the previous homework you have done?
# 
# * The project will be **more work** than a single homework.
# * The project will be a much more accurate representation of what it is like to do data science "in the wild".
# * The project is **open ended**. For most of your homework, there has been a very clear result you are aiming for, and I pick the target. With the project, I will give you general guidance, but you will have significant freedom to create and explore questions. Because of this you won't know the right answer and neither will I.
# * The end result of your project will be a **computational narrative**, i.e. a *story*, that uses code, data and visualizations to communicate something of significance. You will tell this story to me in the form of notebooks and to the class in your final presentation.
# * The project is a **capstone experience** that will tie together everything you have learned and likely require you to learn a lot of new things we haven't covered in class.
# * Most importantly, the project will be a lot of **fun** and provide you with something significant you can use as the start of a data science portfolio.

# ## Selecting a dataset

# Use the following guidelines for picking a dataset:
# 
# * Your dataset should not be larger than 20-30GB unless you get special permission.
# * Be aware that you have about 2GB of RAM. If your dataset is larger than that, you will have to resort to special libraries (such as dask) for working with larger data.
# * Your dataset needs to be sufficiently large and complex to explore interesting questions:
#   - Tabular data
#     - Should contain at least 2 tables with relationships between tables.
#     - After you have grouped by all categorical columns, the resulting groups should have at least 100s of rows.
#     - Should have numerous columns with different data types (categorical, geographical, date/time, quantitative).
#   - Textual data
#     - Should be large enough that there are many files.
#     - Should have some sort of metadata along with it to allow you to answer more interesting questions.
# * The aquisition or usage of the dataset should not be illegal or unethical in any way. It can however be controversial.
# * If you scrape your dataset from web pages or an HTTP API, you need to includes the code used to get the data with your project.
# * If must provide citations and links to where you got the data from.
# * If you have questions about a particular dataset, please ask me as early as possible.

# ## Final presentation

# To get credit for the project, you **must** present your project to the class during the official final time for the class. You will use the notebook to do your presentation.
# 
# * Your presentation should be a narative that describes your data science process, and the questions you explored.
# * You should do live demonstrations and a summary of the code, but you shouldn't get too technical about the details of the code.
# * Remember, most of the class won't know anything about the dataset, topics or questions you are presenting about.
# * If you have code that takes a while to run, you should run the code before the presentation, save the results to a file, load the results from disk and perform final analysis and visualizations.
# * Your presentation notebook should be a separate notebook from the main notebook that contains the full data science process and its description.
# * You will have 5-7 minutes total for your presentation.
# 
# **Students and faculty outside the class will be invited to attend the final presentations.**

# ## Rubric

# You will be graded on the following categories:
# 
# ### Data
# 
# * Your dataset should be complex and large enough to explore interesting questions, but not soo big that it is difficult to work with (see above).
# * Your dataset should be stored under a folder with your GitHub username in the `/data` folder of the server. Do not put your data in your project folder.
# 
# ### Code
# 
# * Code is well organized into relatively small functions (10-20 lines) that do one thing.
# * Functions have docstrings describing what they do.
# * Appropriate variable names are used.
# * PEP 8 is approximately followed for code style.
# * Code is tested using assert statements.
# * Code that is used in multiple notebooks is put into standalone `.py` files and imported.
# * Code is modular to easily allow the exploration of different questions.
# * Code is written with fast performance in mind and does not have any significant performance problems.
# * Your code should not use more than 2GB of RAM at any point in time.
# * Appropriate data structures and algorithms are used.
# * All of your notebooks should run from scratch in a reasonable amount of time. Please make a note about code that takes a long (more than a few minutes) to run.
# 
# ### Narrative
# 
# * Narrative text is provided to describe the dataset, code, results, visualizations, modeling, etc.
# * When appropriate, equations are included (LaTeX).
# * You identify the core questions you will study.
# * The narrative tells a compelling *story* that addresses the questions.
# * A one paragraph abstract is provided.
# 
# ### Presentation
# 
# * Well dressed, looks professional.
# * Relaxed, confident and enthusiastic.
# * Speaks clearly at all times, with good volume, good pace, and smooth delivery.
# * All demos work.
# 
# ### Organization
# 
# * The project is organized into multiple notebooks with clear titles and ordering. Something like this:
#   - `01-Introduction.ipynb`
#   - `02-DataCleaning.ipynb`
#   - `03-Exploration.ipynb`
#   - `04-Modeling.ipynb`
#   - `05-MachineLearning.ipynb`
#   - `06-Presentation.ipynb`
# * An introduction notebook is provided with the following sections:
#   - Abstract
#   - Description of the dataset.
#   - Index of other notebooks with a short description
#   - Citations
# * Each notebook has well organized Markdown sections.
# 
# ### Aquisition and cleaning
# 
# * Dataset is stored on disk in an appropriate format.
# * Dataset is cleaned and transformed into the tidy-data standard (read Hadley's paper!)
# * Tests are provided to verify the data is properly cleaned and transformed.
# * See [odo](http://odo.readthedocs.org/en/latest/) for transforming between formats.
# 
# ### Exploratory data analysis
# 
# * The dataset is explored thoroughly through transformations (groupby, merge, etc) and visualization.
# * Data exploration is tied to the questions you are exploring and this relationship is made explicit.
# * Visualizations adhere to the theory and practice of effective visualizations.
# * Interesting relationships in different parts of the dataset are explored.
# * Interactive widgets are used to explore the dataset interactively.
# * Appropriate visualizations are used.
# 
# ### Statistical modeling
# 
# * Bootstrap resampling is used to create distributions and confidence intervals of any estimated statistics.
# * Appropriate statistical models (regression, maximum likelihood, Markov chain) are built to aid in exploring relationships and extracting insight from the data.
# 
# ### Machine learning
# 
# * Perform supervised or unsupervised machine learning on your dataset to predict, cluster, etc. your data.
# * Appropriate machine learning practices are used (cross validation, hyperparameter tuning, etc.).
# * Multiple algorithms/models are compared where appropriate.
# 
# ### Challenge area
# 
# * Your project should contain at least one challenge area that involves your learning a new Python library, statistical technique, etc.
# * Examples
#   - Network/graphs using [NetworkX}(https://networkx.github.io/)
#   - Larger than memory data using [dask](http://dask.pydata.org/en/latest/).
#   - Topic modeling of text documents using Latent Dirichlet Allocation (LDA).
#   - A new supervised/unsupervised learning algorithm.
#   - A new data storage format, such as HDF5.
#   - A dataset involving time series and date/times (such as financial assets over time).
