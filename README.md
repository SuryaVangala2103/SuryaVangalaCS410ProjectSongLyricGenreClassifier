# SuryaVangalaCS410ProjectSongLyricGenreClassifier
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
4) In terminal, CD into the directory and enter: python3 api.py
5) You will receive a link in terminal. Copy paste this link into the search bar and include /predict at the end
6) Enter censored text into the text box (for all curse words change all characters except the first one to "*")
7) Click enter
8) Observe Result

Code recevied 0.39 on test data via sklearn score. I consider this to be decent considering that lyrics are only one small dimension which differentiate genres. Many songs from different genres can be lyrically identical. 
