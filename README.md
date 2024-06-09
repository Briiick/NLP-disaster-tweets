# NLP with Disaster Tweets

## Predict which Tweets are about real disasters and which ones are not.

#### Alexander Bricken

---

See articles here: 
- https://towardsdatascience.com/part-1-data-cleaning-does-bert-need-clean-data-6a50c9c6e9fd
- https://towardsdatascience.com/does-bert-need-clean-data-part-2-classification-d29adf9f745a

#### Submission Accuracy and Position on Leaderboard (at time of post): 84.063%, position #71 (although #52 if you subtract cheaters).

### Project structure:

```
├── README.md                     <- The top-level README for developers using this project.
├── data
│   ├── raw                       <- The raw data
│   ├── submissions               <- The final data to be submitted
│
│
├── requirements.txt              <- Requirements for this project.
│
├── utils.py                      <- Utility functions for project.
├── tweet-scraping.py             <- Tweet scraping for more data.
│
├── notebooks                     <- Jupyter notebooks for this project.
│   ├── nlp_disaster_tweets       <- The main Jupyter notebook
│
├── data-dictionary.txt <- Data dictionaries, manuals, and all other explanatory materials.
```

### Data

Raw data source: https://www.kaggle.com/c/nlp-getting-started/overview

### Using The Project

Check in the notebooks folder to see the associated exploratory analysis.

If you want to play with it, simply type `git clone https://github.com/Briiick/NLP-disaster-tweets.git` in your terminal.
### References

[Natural Language Processing with Disaster Tweets](https://www.kaggle.com/c/nlp-getting-started/overview)

[NLP with Disaster Tweets: EDA, cleaning and BERT](https://www.kaggle.com/gunesevitan/nlp-with-disaster-tweets-eda-cleaning-and-bert)

[Basics of using pre-trained GloVe Vectors](https://medium.com/analytics-vidhya/basics-of-using-pre-trained-glove-vectors-in-python-d38905f356db)

[Cleaning text data with Python](https://towardsdatascience.com/cleaning-text-data-with-python-b69b47b97b76)

[What is tokenization?](https://www.analyticsvidhya.com/blog/2020/05/what-is-tokenization-nlp/)

[BERT Text Classification using Keras](https://swatimeena989.medium.com/bert-text-classification-using-keras-903671e0207d)
