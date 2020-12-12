import numpy as np
import pandas as pd
import scipy.sparse
import soynlp.hangle as soyh


def show_menu():
    menu_list = [
        '책 검색',
        '랜덤 책 샘플',
        '유저 검색',
        '책 추천'
    ]

    print("------리뷰 기반 책 추천기------")
    for i, m in enumerate(menu_list):
        print("{0}. {1}".format(i + 1, m))
    print("--------------------------------------")

def book_search(search_text):


if __name__ == "__main__":
    show_menu()
    c = input("메뉴를 선택하세요: ")

    if c == '1':
        search_text = input("검색어를 입력하세요: ")
