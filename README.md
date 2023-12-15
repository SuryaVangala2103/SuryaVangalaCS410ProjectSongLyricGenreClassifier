# SuryaVangalaCS410ProjectSongLyricGenreClassifier

Free topic documentation requirements: Source Code, Demo, Self Evaluatiom 

Dependencies: 
1) nltk 
2) os
3) sklearn
4) pickle
5) flask

I used Python 3.7. I don't know if other versions of python work or not.
The webpage runs on localhost. 

Demo: https://www.youtube.com/watch?v=jrwLvbrXyCY

How to set up and use (Documentation):
1) Clone repo to local
2) pip install dependencies listed above
3) Ensure your localhost is set up to run webpages
4) In terminal, CD into the directory and enter:
```console
python3 api.py
```
5) You will receive a link in the terminal. Copy and paste this link into a search engine and include /predict at the end. For example: on my machine the link is  http://127.0.0.1:5000, so I type  http://127.0.0.1:5000/predict into the search bar 
6) Enter censored text into the text box (for all curse words change all characters except the first one to "*") 
7) Click enter
8) Observe Result

Self Evaluation:
My code received a 0.39473684210526316 on sklearn's score metric, which is an R^2 value. This is quite low, however considering the size of the dataset I was able to feasibly gather as well as the fact that song genres are more separated by non-text information than lyrical content, I am satisfied with my performance. Through anecdotal experience, my code seems to have an easier time with hip-hop, pop, and rock songs than country. I don't know why this is. It seems to me that pop, country, and rock can have very similar lyrical content to each other at times, making classification hard. 
