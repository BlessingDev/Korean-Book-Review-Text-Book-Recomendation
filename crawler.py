from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import requests
import time

driver = None

class Yes24ReviewCrawler :
    def __init__(self) :
        options = webdriver.chrome.options.Options()
        options.binary_location = "C:/Program Files/chrome-win/chrome.exe"
        options.add_argument('headless')

        self.driver = webdriver.Chrome(options=options)

    def from_most_reviewed_books(self, n=100):
        '''
        한 주간 가장 많이 리뷰된 책에서 가져오기 - 카테고리 순회
        :param n: 각 카테고리에서 가져올 책 수
        :return: 책 DataFrame, 리뷰 DataFrame
        '''

        print("크롤 시작")
        # 6, 12, 17, 18, 20번 카테고리는 존재하지 않는다
        # 24(잡지)는 전시제한 상품이 너무 많아서 스킵
        category_num = {
            1: range(1, 28), # 8부터 크롤 시작
            17: [46, 38, 45, 63, 50, 48]
        }
        category_num = {
            17: [46, 38, 45, 63, 50, 48]
        }

        # yes24 로그인
        self.driver.get("https://www.yes24.com/Templates/FTLogin.aspx")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//input[@id="SMemberID"]').send_keys("wnsghekd2006")
        self.driver.find_element_by_xpath('//input[@id="SMemberPassword"]').send_keys("qkrWnsgh98%")
        self.driver.find_element_by_xpath('//button[@id="btnLogin"]').click()
        self.driver.implicitly_wait(10)

        # 제목, 작가, 출판사, 출판일, 가격, 2단계 카테고리
        book_df = pd.DataFrame(columns=["ISBN", "BookTitle", "BookAuthor", "Publisher", "PubDate", "Price", "Category-2"])
        book_df.set_index("ISBN")
        # 제목, 내용 점수, 디자인 점수, 리뷰어, 날짜, 내용, 책 인덱스
        review_df = pd.DataFrame(columns=["Title", "ConRate", "DesRate", "Author", "Date", "Content", "BookCode"])
        for c1 in list(category_num.keys()):
            for c2 in category_num[c1]:
                print("카테고리 {0}-{1}".format(c1, c2))
                cate_link = "http://blog.yes24.com/BlogMain/Review/ManyReviewGoods?c1={0:03d}&c2={1:03d}".format(c1, c2)
                self.driver.get(cate_link)
                self.driver.implicitly_wait(10)

                book_links = []
                while len(book_links) <= n :
                    bs = BeautifulSoup(self.driver.page_source)
                    review_div = bs.find("div", {'class': 'rvgul'})
                    review_lists = review_div.find("ul").children

                    for rv in review_lists:
                        if rv.name == "li" :
                            book_link = rv.find("a")["href"]
                            if book_link not in book_links :
                                book_links.append(book_link)
                            # 책 리뷰, 정보를 테이블 형태로 반환
                        if len(book_links) >= n :
                            break

                    if len(book_links) >= n :
                        break

                    page_list_p = bs.find("p", {"class": "page"})
                    try:
                        cur_page = page_list_p.find("strong")
                        next_link = cur_page.find_next_sibling("a")["href"]
                        self.driver.get("http://blog.yes24.com" + next_link)
                        self.driver.implicitly_wait(10)
                    except Exception as e:
                        print("no more books", e)
                        break

                for i, book_link in enumerate(book_links):
                    print("책 ({0}/{1})".format(i + 1, len(book_links)))
                    crawl_without_error = False
                    while not crawl_without_error :
                        try :
                            book_rvs, book_info = self.crawl_review_and_info_from_book_page(book_link)
                            crawl_without_error = True
                        except Exception as e :
                            print("에러가 발생했습니다", e)


                    df = pd.DataFrame([book_info], columns=["ISBN", "BookTitle", "BookAuthor", "Publisher", "PubDate", "Price", "Category-2"],  index=[book_info[0]])
                    # 책 테이블 준비
                    book_df = book_df.append(df)
                    # 책 인덱스를 Foreign key로 리뷰 정보에 집어넣기
                    idx = book_df.index[book_df["BookTitle"] == book_info[1]]

                    book_rvs = pd.DataFrame(book_rvs, columns=["Title", "ConRate", "DesRate", "Author", "Date", "Content"])
                    book_idx = np.zeros((book_rvs.shape[0], 1), dtype=np.uint64)
                    book_idx.fill(idx[0])
                    book_rvs["BookCode"] = book_idx

                    review_df = review_df.append(book_rvs, ignore_index=True)

                review_df.to_csv("review_{0}_{1}.csv".format(c1, c2), sep=',', na_rep='NaN')
                book_df.to_csv("book_{0}_{1}.csv".format(c1, c2), sep=',', na_rep='NaN')
                book_df = pd.DataFrame(
                    columns=["ISBN", "BookTitle", "BookAuthor", "Publisher", "PubDate", "Price", "Category-2"])
                book_df.set_index("ISBN")
                # 제목, 내용 점수, 디자인 점수, 리뷰어, 날짜, 내용, 책 인덱스
                review_df = pd.DataFrame(
                    columns=["Title", "ConRate", "DesRate", "Author", "Date", "Content", "BookCode"])

    def crawl_review_and_info_from_book_page(self, book_link):
        self.driver.get(book_link)
        WebDriverWait(self.driver, 5) \
            .until(EC.presence_of_element_located((By.XPATH, '//table[@class="tb_nor tb_vertical"]')))
        rv_list = []
        book_info = []

        bs = BeautifulSoup(self.driver.page_source)
        # 책 정보 크롤
        book_title = ""
        try:
            book_title = bs.find("div", {"class": "gd_titArea"}).get_text().replace('\n', ' ').strip()
        except :
            print("책 제목 크롤 오류")
        book_author = ""
        try :
            book_author = bs.find("span", {"class": "gd_auth"}).get_text().replace('저', '').strip()
        except :
            print("책 저자 크롤 오류")
        book_pub = ""
        try :
            book_pub = bs.find("span", {"class": "gd_pub"}).get_text().strip()
        except :
            print("출판사 크롤 오류")
        book_date = ""
        try :
            book_date = bs.find("span", {"class": "gd_date"}).get_text().strip()
        except :
            print("날짜 크롤 오류")
        book_price = -1
        try :
            book_price = bs.find("tr", {"class": "accentRow"}).find("em").get_text().strip()
            book_price = int(book_price.replace(',', ''))
        except :
            print("가격 크롤 오류")
        book_category = ""
        try :
            book_category = bs.find("div", {"class": "yLocaSet"}).find_next_sibling("div").find("li", {"class": "on"}).get_text().strip()
        except :
            print("카테고리 크롤 오류")
        book_info_table = bs.find("tbody", {"class": "b_size"})
        book_isbn = -1
        try :
            for tr in book_info_table.children :
                if tr.name == "tr" :
                    if tr.find("th").get_text().strip() == "ISBN13" :
                        book_isbn = tr.find("td").get_text().strip()
                        break
            book_isbn = int(book_isbn)
        except :
            print("ISBN 크롤 오류")

        # ISBN, 제목, 작가, 출판사, 출판일, 가격, 카테고리
        book_info.extend([book_isbn, book_title, book_author, book_pub, book_date, book_price, book_category])

        print("책 제목: {0}".format(book_title))
        # 리뷰 페이지 수가 1인지 검사
        end_button = bs.find("div", {"id": "infoset_reviewContentList"}).find("a", {"class": "end"})
        if "dim" not in end_button["class"] :
            # 리뷰 페이지가 1이 아닐 때만 마지막 리뷰 페이지로 가는 버튼 누르기
            num_list_div = self.driver.find_element_by_xpath('//*[@id="infoset_reviewContentList"]/div[1]')
            num_list_div.find_element_by_xpath('.//a[@class="bgYUI end"]').click()
            time.sleep(0.5)

        # 가장 마지막 페이지의 번호를 얻는다
        num_list_div = self.driver.find_element_by_xpath('//*[@id="infoset_reviewContentList"]/div[1]')
        last_number = num_list_div.find_element_by_xpath('.//strong[@class="num"]').text
        rv_page_num = int(last_number)
        # 다시 가장 첫 페이지로
        self.driver.find_element_by_xpath('//*[@id="infoset_reviewContentList"]/div[1]/div[1]/div/a[1]').click()
        time.sleep(0.5)
        for i in range(rv_page_num):
            print("리뷰 페이지 {0}/{1}".format(i + 1, rv_page_num))
            rv_bs = BeautifulSoup(self.driver.page_source)

            # 리뷰 크롤
            rvs = rv_bs.find_all("div", {"class": "reviewInfoGrp"})
            for rv in rvs:
                rv_title = rv.find("span", {"class": "review_tit"}).get_text().strip()
                rv_rate_span = rv.find("span", {"class": "review_rating"})
                rates = []
                for rate in rv_rate_span("span"):
                    rates.append(int(rate.get_text()[2]))
                rv_con_rate = rates[0]
                rv_des_rate = rates[1]
                rv_author_nodes = rv.find_all(lambda tag : "class" in tag.attrs and "lnk_id" in tag["class"])
                rv_author = rv_author_nodes[0].get_text().strip()
                rv_date = rv.find("em", {"class": "txt_date"}).get_text().strip()
                # 숨겨져 있는 원본 리뷰글을 찾아서 크롤
                rv_content = rv.find("div", {"class": ["origin"]}) \
                    .find("div", {"class": "review_cont"}).get_text().strip()

                # 제목, 내용 점수, 디자인 점수, 리뷰어, 날짜, 내용
                rv_list.append([rv_title, rv_con_rate, rv_des_rate, rv_author, rv_date, rv_content])

            # 다음 페이지로 가는 버튼 누르기
            num_list_div = self.driver.find_element_by_xpath('//*[@id="infoset_reviewContentList"]/div[1]')
            cur_page = num_list_div.find_element_by_xpath('.//strong[@class="num"]')
            next_button = cur_page.find_element_by_xpath('following-sibling::a')
            next_button.click()
            time.sleep(0.5)


        return rv_list, book_info

def crawl_review_text_content(link) :
    res = requests.get(link)
    if res.status_code == 200 :
        bs = BeautifulSoup(res.text)
        content_div = bs.find("div", {"class": "blogContArea"})
        rv_text = content_div.find("span").get_text().strip()
        return rv_text
    else :
        return ""