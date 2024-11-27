# jh24993_EMATM0048
Summative Assessment













































































## Question 2 – Data Analytics

# Please note: The data changes if the webscrape code is clicked on repeatedly, kindly refer to the csv file for an accurate result.

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

### Modules used:
1.	From collections – collections.Counter (for counting the frequency of an item on a list)
2.	From wordclod – wordcloud (for visual representation of words)
3.	From nltk – re  was used for regular expressions to remove special characters, nltk.corpus.stopwords removed stop words, nltk.tokenize.word_tokenize` used to tokenize text, and nltk.stem.WordNetLemmatizer lemmatize words to clean and preprocess text/word data analysis.
4.	From sklearn - sklearn.feature_extraction.text, sklearn.model_selection, sklearn.linear_model, sklearn.decomposition.LatentDirichletAllocation (for vectorization, validation and regression models)

### How to run the code:
The code should be run using Jupyter notebook.




