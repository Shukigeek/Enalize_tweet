analize data project


* the project take a path of a csv file and have 2 main phichers 

** the first one is analyze the data to get 5 conclotion from the data 
1. average len of tweet 
2. number of antisemic tweet and non antisemic tweet
3. longest 3 tweet per catgory
4. number of uppercase word in tweet total
5. 10 must common words in all tweets

** the secound picher is to cleanig the data
1. by saving only the 2 importent columns
2. deleting comma sign
3. replecing all words to lowwer case
4. deleteing all the tweets that not biased

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
