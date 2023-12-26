# 라이브러리 추가
import warnings

from AI.connectdb import db_read

warnings.filterwarnings(action='ignore')
import re
import pandas as pd
import numpy as np
import urllib.request
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# 모듈 불러오기
pos_dict = joblib.load('AI/pos_dict.pkl')
neg_dict = joblib.load('AI/neg_dict.pkl')
plus_label = joblib.load('AI/plus_label.pkl')
tfidf = joblib.load('AI/tfidf.pkl')
SA_lr = joblib.load('AI/SA_lr.pkl')

# 하나의 내용에 대한 라벨(긍정/부정에 따른) 붙이는 함수
def labeling(i):
    tfidf_list = tfidf
    tfidf_module = tfidf_list[0]
    SA_module = SA_lr
    row = db_read(i)
    p_row = list(row)
    data = p_row[1]
    print(p_row[1])
        
    data = re.sub("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]", "", data)
    pn_tfidf = tfidf_module.transform([data])
    predict = SA_module.predict(pn_tfidf)
    if(predict[0] == 1):
        p_row[6] = '&#x1F60A'
        print(p_row[6])
        return p_row[6]
    else:
        p_row[6] = '&#x1F621'
        return p_row[6]
    

def label(i):
    
    tfidf_list = tfidf
    tfidf_module = tfidf_list[0]
    SA_module = SA_lr
    print(i)    
    data = re.sub("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]", "", i)
    pn_tfidf = tfidf_module.transform([data])
    predict = SA_module.predict(pn_tfidf)
    if(predict[0] == 1):
        result = '&#x1F60A'
        cont=i+":"+result
        print(cont)
        return result
    else:
        result = '&#x1F621'
        cont=i+":"+result
        print(cont)
        return result
    