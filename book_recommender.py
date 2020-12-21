import numpy as np
import pandas as pd
from pathlib import Path
import scipy.sparse
import soynlp.hangle as soyh

class BookRecommender:
    def __init__(self):
         DATA = Path('.').resolve() / "Data"

         self.book_table = pd.read_csv(DATA / "book1.csv", index_col=[0])
         self.book_table = self.book_table.set_index("Unnamed: 0.1")
         self.rv_table = pd.read_csv(DATA / "review1_pre.csv", index_col=[0])
         self.rv_table = self.rv_table.drop_duplicates(['Author', 'BookCode'], keep='first')
         self.rv_table = self.rv_table[~pd.isna(self.rv_table["Author"])]

         self.rv_book_pivot = self.rv_table.pivot(index='Author', columns='BookCode', values='SumRate')
         self.rv_book_pivot = self.rv_book_pivot.fillna(0)
         self.us_list = self.rv_book_pivot.index
         self.book_list = self.rv_book_pivot.columns

         self.pred_res = scipy.sparse.load_npz(DATA / "pred_tfidf_comb1_k100.npz")
         self.pred_res = pd.DataFrame(self.pred_res.todense(), index=self.us_list, columns=self.book_list)

    def search_book(self, search_text, n=10):
        search_table = self.book_table.copy()
        search_table["JamoEditDis"] = [soyh.jamo_levenshtein(t, search_text) for t in search_table["BookTitle"].tolist()]
        search_table["levEditDis"] = [soyh.levenshtein(t, search_text) for t in search_table["BookTitle"].tolist()]
        search_table["EditDis"] = np.mean(search_table[["JamoEditDis", "levEditDis"]], axis=1)
        search_table = search_table.sort_values("EditDis")
        return search_table.head(n)

    def sample(self, n):
        user_table = self.rv_table.groupby(["Author"]).count()
        return self.book_table.sample(n), user_table[["Title"]].sample(n)

    def recommend_book(self, user, n=10):
        if user in self.us_list:
            pred_score = self.pred_res.loc[user, :]
            pred_score = pred_score.T
            pred_score = pred_score.sort_values(ascending=False)
            pred_score = pred_score.reset_index()
            pred_book = pd.merge(pred_score, self.book_table, left_on="BookCode", right_on="ISBN", how="left")
            pred_book = pred_book.rename(columns={user:"PredScore"})
            pred_book = pred_book.drop(["BookCode"], axis=1)

            real_score = self.rv_book_pivot.loc[user, :]
            real_score = real_score.T
            real_score = real_score.reset_index()
            pred_book = pd.merge(pred_book, real_score, left_on="ISBN", right_on="BookCode", how="left")
            pred_book = pred_book.rename(columns={user: "RealScore"})

            rated_num = len(pred_book[pred_book["RealScore"] > 0])

            return pred_book[pred_book["RealScore"] == 0].iloc[:n, :], pred_book[pred_book["RealScore"] > 0].iloc[:min(rated_num, n), :]
        else:
            print("존재하지 않는 유저입니다.")