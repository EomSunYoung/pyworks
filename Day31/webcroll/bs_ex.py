# BeautifulSoup 사용하기 - html 태그 및 데이터 추출 라이브러리

from bs4 import BeautifulSoup

html_str = """
<html>
    <body>
        <ul class="item">
            <li>인공지능</li>
            <li>빅데이터</li>
            <li>로봇공학</li>
        </ul>
        <ul class="lang">
            <li>Python</li>
            <li>C/C++</li>
            <li>JAVA</li>
        </ul>
    </body>
</html>
"""

# find(), selec_one()
html = BeautifulSoup(html_str, "html.parser")
# first_ul = html.find('ul')  # find() : 첫 요소를 찾음
first_ul = html.select_one('ul.item')
second_ul = html.select_one('ul.lang')
# print(first_ul)
print(first_ul.text)
print(second_ul.text)