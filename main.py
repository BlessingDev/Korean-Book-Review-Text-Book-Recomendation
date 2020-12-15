import pandas as pd
import book_recommender

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

def show_menu():
    menu_list = [
        '책 검색',
        '랜덤 책, 유저 샘플',
        '책 추천'
    ]

    print("------리뷰 기반 책 추천기------")
    for i, m in enumerate(menu_list):
        print("{0}. {1}".format(i + 1, m))
    print("-1. 프로그램 종료")
    print("--------------------------------------")

def book_search(search_text, br):
    res = br.search_book(search_text)
    print(res[["BookTitle", "BookAuthor", "Category-2"]])

def sample_data(n, br):
    book, us = br.sample(n)
    print(book[["BookTitle", "BookAuthor", "Category-2"]])
    print(us)

def book_recommend(user, n, br):
    res = br.recommend_book(user, n)
    print(res[["BookTitle", "BookAuthor", "ISBN", "PredScore"]])

if __name__ == "__main__":
    br = book_recommender.BookRecommender()

    program = True
    while program:
        show_menu()
        c = input("메뉴를 선택하세요: ")

        if c == '1':
            search_text = input("검색어를 입력하세요: ")
            book_search(search_text, br)
        elif c == '2':
            n = input("몇 개를 샘플하시겠습니까? ")
            if n.isdigit():
                n = int(n)
                sample_data(n, br)
            else:
                print("숫자가 아닙니다")
        elif c == '3':
            user = input("추천을 받을 유저를 입력하세요: ")
            book_recommend(user, 10, br)
        elif c == '-1':
            print("프로그램을 종료합니다.")
            program=False
