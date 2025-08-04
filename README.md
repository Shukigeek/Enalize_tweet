analyze data project


* the project take a path of a csv file and have 2 main pitchers 

** the first one is analyze the data to get 5 conclusion from the data 
1. average len of tweet 
2. number of antisemitic tweet and non antisemitic tweet
3. longest 3 tweet per category
4. number of uppercase word in tweet total
5. 10 must common words in all tweets

** the second pitcher is to cleaning the data
1. by saving only the 2 important columns
2. deleting comma sign
3. replacing all words to lower case
4. deleting all the tweets that not biased

to use the project just need to run the main.py script


the file system is as follows

project/
|--- README.me
|---data/
|------tweet_dataset.csv
|---results/
|------results.json
|------tweet_dataset_cleaned.csv
|---src/
|------analyze_manager.py
|------clean_data.py
|------clean_manager.py
|------data_analyze.py
|------load_data.py
|---main.py
