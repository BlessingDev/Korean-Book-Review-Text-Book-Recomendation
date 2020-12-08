# 한국어 책 리뷰 텍스트를 이용한 아이템 기반 협업 필터링

## 배경

빅데이터 시대를 맞아 적지 않은 수의 이커머스 업체가 고객 맞춤 추천 서비스를 하고 있다. 개인화 마케팅이 뜨거운 화두로 떠오른 가운데 그러한 추세를 협업 필터링이 뒷받침하고 있다. 또한 한국어 자연어 처리는 활발히 연구되고 있는 영역이며, 아직 무궁무진한 가능성을 갖고 있는 분야이다. 

전자상으로 거래되는 수많은 상품 중에서도 서적은 콘텐츠 특성상 하나를 사서 소비하는데 적지 않은 심력과 시간이 소모된다. 그런 만큼 많은 수의 독서가들은 **자신에게 맞는** 책을 사서 조금이나마 더 행복한 독서 생활을 보내기를 바란다. 다독가의 충고 중 하나가 '자신에게 맞지 않는다고 생각되는 책은 과감하게 덮어라.'일 정도이다. 하지만 자신에게 맞지 않는다고 판단한 시점에서는 그 책을 구매한 후일 것이다. 그러나 정작 서적 분야에서는 비슷한 책 추천을 비롯한 개인화 서비스가 많이 활성화돼 있지 않다. 각 서점마다 유사 책 추천이란 시스템을 갖추고 있기는 하지만, 그것이 주요한 판촉 요소가 되지는 않는다. 이러한 상황에 아쉬움을 느껴 서적 분야, 한국어 분야에서 아이템 추천을 할 수 있는 방법론을 개발해 보려고 한다.

## 데이터

데이터로 [Yes24](http://www.yes24.com/Main/default.aspx)의 리뷰 텍스트를 수집하여 사용했다. [일주일 간 가장 많이 리뷰된 책](http://blog.yes24.com/BlogMain/Review/ManyReviewGoods?c1=001)을 2020-10-07 기준으로 두 번째 카테고리를 순회하며 수집했다.

총 1,523권의 책과 26,483건의 리뷰가 수집되었다. 이중 추천에서는 의미없는, 한 권에만 리뷰를 달은 유저의 리뷰 7,429건을 삭제했다. 그 외에도 중복된 리뷰와 결측치가 있는 리뷰를 제외하여 총 16,780건의 리뷰, 4,100명의 유저, 1,425권의 책이 남았다.

## 협업필터링

협업필터링은 널리 사용되고 있는 추천 알고리즘이다. 협업필터링은 다음과 같은 과정을 거쳐 이루어진다.

* 유저-아이템 행렬 구성

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>BookCode</th>
      <th>8.801748e+12</th>
      <th>8.809124e+12</th>
      <th>8.809255e+12</th>
      <th>8.809255e+12</th>
      <th>8.809264e+12</th>
      <th>8.809333e+12</th>
      <th>8.809417e+12</th>
      <th>8.809470e+12</th>
      <th>8.809475e+12</th>
      <th>8.809475e+12</th>
      <th>...</th>
      <th>9.791197e+12</th>
      <th>9.791197e+12</th>
      <th>9.791197e+12</th>
      <th>9.791197e+12</th>
      <th>9.791197e+12</th>
      <th>9.791197e+12</th>
      <th>9.791197e+12</th>
      <th>9.791197e+12</th>
      <th>9.791197e+12</th>
      <th>1.844674e+19</th>
    </tr>
    <tr>
      <th>Author</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>'_'*</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>**01 22 2020  9:45PM**</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>**09  4 2018  1:15PM**</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>**09 12 2017 10:14AM**</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>**10 27 2017  4:24PM**</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>히또리도리돌</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>히야신스</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>히이이익</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>히키</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>힘찬발걸음</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>8.0</td>
    </tr>
  </tbody>
</table>

* 아이템 간 혹은 유저 간 유사도 행렬 구성: cos 유사도를 사용했다.

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right">
      <th>BookCode</th>
      <th>8.801748e+12</th>
      <th>8.809124e+12</th>
      <th>8.809255e+12</th>
      <th>8.809255e+12</th>
      <th>8.809264e+12</th>
      <th>8.809333e+12</th>
      <th>8.809417e+12</th>
      <th>8.809470e+12</th>
      <th>8.809475e+12</th>
      <th>8.809475e+12</th>
      <th>...</th>
      <th>9.791197e+12</th>
      <th>9.791197e+12</th>
      <th>9.791197e+12</th>
      <th>9.791197e+12</th>
      <th>9.791197e+12</th>
      <th>9.791197e+12</th>
      <th>9.791197e+12</th>
      <th>9.791197e+12</th>
      <th>9.791197e+12</th>
      <th>1.844674e+19</th>
    </tr>
    <tr>
      <th>BookCode</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8.801748e+12</th>
      <td>1.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>8.809124e+12</th>
      <td>0.0</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.070646</td>
    </tr>
    <tr>
      <th>8.809255e+12</th>
      <td>0.0</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>0.728219</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.201619</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.258199</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>8.809255e+12</th>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.728219</td>
      <td>1.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>8.809264e+12</th>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>9.791197e+12</th>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>0.162586</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>9.791197e+12</th>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.162586</td>
      <td>1.000000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>9.791197e+12</th>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>9.791197e+12</th>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>1.000000</td>
      <td>0.029128</td>
    </tr>
    <tr>
      <th>1.844674e+19</th>
      <td>0.0</td>
      <td>0.070646</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.014025</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.029128</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>

* 유사도를 이용해 유저의 아이템에 대한 점수 예측

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right">
      <th>BookCode</th>
      <th>8.801748e+12</th>
      <th>8.809124e+12</th>
      <th>8.809255e+12</th>
      <th>8.809255e+12</th>
      <th>8.809264e+12</th>
      <th>8.809333e+12</th>
      <th>8.809417e+12</th>
      <th>8.809470e+12</th>
      <th>8.809475e+12</th>
      <th>8.809475e+12</th>
      <th>...</th>
      <th>9.791197e+12</th>
      <th>9.791197e+12</th>
      <th>9.791197e+12</th>
      <th>9.791197e+12</th>
      <th>9.791197e+12</th>
      <th>9.791197e+12</th>
      <th>9.791197e+12</th>
      <th>9.791197e+12</th>
      <th>9.791197e+12</th>
      <th>1.844674e+19</th>
    </tr>
    <tr>
      <th>Author</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>'_'*</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>**01 22 2020  9:45PM**</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>**09  4 2018  1:15PM**</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>10.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>**09 12 2017 10:14AM**</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>**10 27 2017  4:24PM**</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>히또리도리돌</th>
      <td>10.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>9.0</td>
      <td>10.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>히야신스</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>히이이익</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>10.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>10.0</td>
      <td>0.0</td>
      <td>10.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>히키</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>힘찬발걸음</th>
      <td>0.0</td>
      <td>8.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>

* 예측된 점수를 평가

|  MAP(Mean Average Precision)  |   Recall  |  F-1 Score  |  F-0.5 Score  |
|:---:|:---:|:---:|:---:|
|0.797|0.729|0.762|0.783|

## 텍스트의 유사도 측정

텍스트를 벡터로 임베딩하는데는 여러 가지 방법이 있다. 본 연구에서는 그 중 두 가지 방법을 시험하였다.

* Word2Vec

Word2Vec은 토큰화된 문장 셋을 이용하여 각 토큰(단어)의 적절한 벡터 좌표를 구하는 머신러닝 기법이다. 이들 단어의 벡터는 가까운 의미를 가진 단어일수록 cos 유사도가 높아진다. 책 리뷰 텍스트로 학습한 Word2Vec 모델의 예시이다.
```
rv_model.most_similar('상상')

[('착각', 0.48839378356933594),
 ('생각', 0.4812341034412384),
 ('즐거워하', 0.47967398166656494),
 ('경험', 0.47305458784103394),
 ('망상', 0.4660475254058838),
 ('초월', 0.4562140107154846),
 ('예상', 0.4553142189979553),
 ('감탄', 0.4543972611427307),
 ('상상도', 0.44329705834388733),
 ('떠올리', 0.4299180507659912)]
```
이러한 Word2Vec 분석을 이용하여 문서에 속하는 단어의 벡터를 더하여 문서 벡터를 구한 후에 문서 벡터 간의 cos 유사도를 구하였다.

* TF-IDF

[TF-IDF](https://ko.wikipedia.org/wiki/Tf-idf)는 단어 빈도-역문서 빈도를 의미한다. 결과물은 문서-단어 행렬이다. 이것을 이용하여 문서 간의 유사도를 구할 수 있다.

본 연구에서는 각 책에 대한 리뷰 문서를 모두 합하여 TF-IDF 행렬을 구한 후에 cos 유사도로 책 간의 리뷰 문서 유사도를 구하였다.

---

두 방법으로 문서 유사도를 구해본 결과 TF-IDF 유사도만 사용하기로 하였다. word2vec으로 구한 유사도가 대부분 0에 가까워 유사도로서 의미를 찾기 어려웠기 때문이다.

![image](https://raw.githubusercontent.com/BlessingDev/Korean-Book-Review-Text-Book-Recomendation/master/Pictures/word2vec%20%EC%9C%A0%EC%82%AC%EB%8F%84%20%EB%B6%84%ED%8F%AC.png)

위 도표에서 rvvec이 w2v 리뷰 벡터로 구한 유사도이다.

## 유사도를 합치는 방법

텍스트 유사도만을 이용한 점수 예측은 성능이 매우 저조했다. 그에 따라 텍스트 유사도만을 이용한 점수 예측에서 평점 유사도 기반 점수 예측을 텍스트 기반 유사도로 보충하는 방향으로 모델 구축 방향을 선회했다. 

유사도를 합치는데는 기본적으로 산술 평균을 사용하였다.

추가로 직접 정의한 평균을 사용하기도 했다. 편의상 이것을 '배타 평균'이라고 지칭하겠다.
```
def sim_comb_excl(a, b):
    comb = np.zeros(a.shape)
    bool_idx = (a == 0.0) & (b > 0)
    comb[bool_idx] = b[bool_idx]
    bool_idx = (b == 0.0) & (a > 0)
    comb[bool_idx] = a[bool_idx]
    bool_idx = (a > 0) & (b > 0)
    comb[bool_idx] = (a[bool_idx] + b[bool_idx]) / 2.0
    
    return comb
```

## 모델 평가 방법

* MAP(Mean Average Precision): 

Precision은 True라고 예측한 것 중, 실제로 True인 것의 비율이다. 그런데 추천 시스템에 Precision을 적용하면 다음과 같은 문제가 생긴다. **0(점수가 매겨지지 않음)을 True로 예측한 경우에는 실제로 True인 것으로 봐야하는가?** 우리는 유저가 이것을 실제로 좋아할지 싫어할지 알 수 없다. Ground Truth를 구하지 못하는 것이다. 따라서 Map은 "유저의 기존 경험에 신경쓰지 말고, 아이템의 추천 여부에 주목하자"는 생각으로 만들어졌다. MAP의 계산 공식은 다음과 같다.

`MAP = sum(추천된 아이템의 비율)/추천된 아이템 수`

실제로 유저가 긍정적으로 평가한 아이템을 긍정적으로 평가했는가보다 얼마나 유용한 추천 정보를 제공했는가에 더 초점을 맞추는 것이다.

출처: [Precision and recall in recommender systems, Kirill Bondarenko](https://bond-kirill-alexandrovich.medium.com/precision-and-recall-in-recommender-systems-and-some-metrics-stuff-ca2ad385c5f8)

* Recall
* F-1 Score
* F-0.5 Score: MAP에 더 가중치를 두어 추천에 더 큰 의미를 두는 점수도 계산하였다.

## 결과

결과는 k를 10, 20, 30으로 늘려가며 측정했다.

![image](https://raw.githubusercontent.com/BlessingDev/Korean-Book-Review-Text-Book-Recomendation/master/Pictures/K%EC%97%90%20%EB%94%B0%EB%A5%B8%20F-1%20%EC%A0%90%EC%88%98.png)

일반 평점 모델
|K|  MAP(Mean Average Precision)  |   Recall  |  F-1 Score  |  F-0.5 Score  |
|:---:|:---:|:---:|:---:|:---:|
|10|0.797|0.729|0.762|0.783|
|20|0.797|0.729|0.762|0.783|
|30|0.797|0.729|0.762|0.783|

일반 평점+TF-IDF 유사도 평균 조합 모델
|K|  MAP(Mean Average Precision)  |   Recall  |  F-1 Score  |  F-0.5 Score  |
|:---:|:---:|:---:|:---:|:---:|
|10|0.785|0.525|0.629|0.714|
|20|0.776|0.847|0.810|0.789|
|30|0.776|0.847|0.810|0.789|

일반 평점+TF-IDF 유사도 배타 평균 조합 모델
|K|  MAP(Mean Average Precision)  |   Recall  |  F-1 Score  |  F-0.5 Score  |
|:---:|:---:|:---:|:---:|:---:|
|20|0.775|0.849|0.811|0.789|
|30|0.775|0.849|0.811|0.789|

## 결론

* Word2Vec을 이용해 문서 간 유사도를 구하는 방법은 결과가 좋지 않았다.
* 텍스트 유사도는 단독으로 사용하면 평점 유사도보다 점수가 떨어진다.
* 충분한 k가 주어진다면 텍스트와 평점 유사도를 조합한 모델이 평점 유사도만 사용한 모델보다 성능이 높다.
* 평점 유사도는 K=10을 넘으면 k가 늘어나도 추가적인 정보를 얻지 못했고, tf-idf 유사도도 k=20을 넘으면 추가적인 정보를 얻지 못했다.
