import matplotlib.pyplot as plt
import matplotlib
import matplotlib.font_manager as fm
import seaborn as sns
import numpy as np
import pandas as pd
from gensim.models import KeyedVectors

import crawler
import nlp

sns.set()
sns.set_context('talk')

try:
    font_location = "HANDotum.ttf"
    font_name = fm.FontProperties(fname = font_location).get_name()
    matplotlib.rc('font', family=font_name)
except:
    print("폰트 임포트 에러")

from sklearn import neighbors

rv1 = pd.read_csv("Data/review1_pre.csv", index_col=[0])
rv1 = rv1.drop_duplicates(['Author', 'BookCode'], keep='first')
rv1 = rv1[~pd.isna(rv1["Author"])]

rv_book_pivot = rv1.pivot(index='Author', columns='BookCode', values='SumRate')
rv_book_pivot = rv_book_pivot.fillna(0)
us_list = rv_book_pivot.index
book_list = rv_book_pivot.columns
book_rv_pivot = rv_book_pivot.T

nn_model = neighbors.NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=10)
nn_model.fit(book_rv_pivot)
sim, idx = nn_model.kneighbors_graph(book_rv_pivot, mode='distance')