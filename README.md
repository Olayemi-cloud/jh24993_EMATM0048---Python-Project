# jh24993_EMATM0048
Summative Assessment

## Question 1 - Fish Hatchery simulation program.

Developing a program that manages the activities of a hatchery using OOP – Object Oriented Programming

## Introduction

This project uses Object Oriented Programming to create a model that coordinates the running of a fish hatchery business. The model oversees activities like buying, selling and restocking of fish and the resources used in handling the fish (fertilizers, feed, salt). The model also manages the addition and removal of technicians that are in charge of the fish maintenance and sale. Another interesting part of the model is the fact that it shows the payment plan for technician. It also shows the list of Vendors and the availability of resources in the warehouse. Finally, it shows the cash flow of the hatchery business and indicates depreciation that occurs at every quarter including when the hatchery goes bankrupt.

Steps captured in the model
- Buying, selling, and restocking fish.
- Managing resources such as fertilizers, feed, and salt.
- Adding and removing technicians responsible for fish maintenance and sales.
- Tracking technician payment plans.
- Listing vendors and monitoring warehouse resource availability.
- Displaying cash flow and depreciation at every quarter, including identifying when the hatchery goes bankrupt.

## Technologies
The project is implemented using:
Python 3.12

## Program Setup
The program is modular and organized as follows:
Modules:The modules contains functions, classes that enhances the program's functionality.

fish.py - 
warehouse.py -
technician.py -
config.py -
hatchery.py -




































































































# Question 2 – Data Analytics

#3 Please note: The data changes if the webscrape code is clicked on repeatedly, kindly refer to the csv file for an accurate result.

Exploratory data analysis on data web scraped from the subreddit Health on the Reddit App

### Introduction
This project highlights the engagement patterns in Health subreddit on Reddit. Using the web-scrapped data, the scores, number of comments, post authors and trending health-related discussions was examined to know the community interaction style and popular topics. This analytics aims to explore the relationship between post scores, number of comments and other engagement factors while applying web scrapping, data preprocessing, and visualization techniques.

### Dataset Description
Website: Reddit (subreddit: r/Health)
Data Collection: Web scrapping using Python library Praw
Collection date: 10/18/2024 – 11/27/2024
Key data Columns: Post title, Author, Score, Number of Comments, Time posted.

### Data Analytics Pipeline
1.	Data Collection: To scrape data from the Reddit API, a reddit account was created, followed by registration for API credentials via Reddit's developer portal. After receiving a client_id, client_secret and user_agent, I proceeded to install ‘praw’ using "pip install praw" to enable scrapping from the Reddit website. Praw is a Python wrapper for the Reddit API, which makes authentication and JSON parsing easy. Then authenticated using client_id, client_secret, and user_agent. After that, reddit.subreddit('health') was used to fetch the health post data.
2.	Data Cleaning and Preprocessing: Removed irrelevant columns and renamed columns for consistency, handled inconsistent data.
3.	Exploratory Data Analysis: Statistics – mean, median, range & standard deviation. Visualise relationships using bar charts, health maps, sentimental analysis.
4.	Visualisation: Using libraries like Matplotlib, Seaborn, Plotly to create correlation heatmaps, word clouds, bar charts
5.	Summary and Conclusion: The analysis showed the trend of author engagement, sentiment changes over time and the connection between post scores and comments, highlighting the need for more accurate prediction models.

### Library used –
1.	Praw –  This library was used to access Reddit API to extract data. Installed by typing “pip install praw” on the anaconda prompt.
2.	Pandas – Used for data analysis and manipulations of the data set
3.	Seaborn – Used for statistical data visualization in collaboration with Matplotlib.
4.	Matplotlib.pyplot – For creating visuals, bar chart, histogram, doughnut charts etc
5.	Sklearn(scikit-learn) – Machine learning library used for regression.
6.	Arrow – Handled the date for more accurate precision, installed via "pip install arrow"


### Modules used:
1.	From collections – collections.Counter (for counting the frequency of an item on a list)
2.	From wordclod – wordcloud (for visual representation of words)
3.	From nltk – re  was used for regular expressions to remove special characters, nltk.corpus.stopwords removed stop words, nltk.tokenize.word_tokenize used to tokenize text, and nltk.stem.WordNetLemmatizer lemmatize words to clean and preprocess text/word data analysis.
4.	From sklearn - sklearn.feature_extraction.text, sklearn.model_selection, sklearn.linear_model, sklearn.decomposition.LatentDirichletAllocation (for vectorization, validation and regression models)

### How to run the code:
The code should be run using Jupyter notebook.




