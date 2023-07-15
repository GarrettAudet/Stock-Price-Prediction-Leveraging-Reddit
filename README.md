# Abstract 
The increasing attraction of high-risk investments for retail investors has fuelled speculation across social media platforms on stocks with a perceived likelihood for disproportionate returns. The code present within this repo investigates the viability of leveraging online equity speculation to inform investor purchase behavior based on the historic accuracy of individuals predicting market movements. 

# Data Collection
- Webscrape.ipynb: Collect the Reddit data using PRAW and Pushshift APIs

# Prepocessing Folder
- Filtering of submission and comment Reddit data
- Text cleaning
- Ticker extraction
- Collection of financial data
- Sentiment score
- Trustworthiness calculation

# Code
The code located in this folder represents different models with varying sliding windows. The rationale is - relative to our dataset of user trustworthy scores and historic equity movements - is to see how timely information must be to be relevant and which models perform best in this time-series prediction.

# Graphs
The graphs folder has the results from the code run in the Models folder.

