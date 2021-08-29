import requests
from bs4 import BeautifulSoup


# User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36
def douBan250():
    returnMap = {}
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
        , "Host": "movie.douban.com"}
    movie_list = []
    movie_scores = []
    for i in range(0, 10):
        link = "https://movie.douban.com/top250?start=" + str(i * 25)
        r = requests.get(link, headers=headers, timeout=20)
        # print(str(i+1), "页面响应码:", r.status_code)
        # print(r.text)
        soup = BeautifulSoup(r.text, "lxml")
        div_list = soup.find_all('div', class_='hd')
        for each in div_list:
            movie = each.a.span.text.strip()
            movie_list.append(movie)

        bd_list = soup.find_all('div', class_='star')
        for each in bd_list:
            score = each.find('span',class_="rating_num").get_text()
            movie_scores.append(score)

    for i, movie in enumerate(movie_list):
        returnMap[movie] = movie_scores[i]
        # returnMap["score"] =
        # returnMap.pop("name", movie)
        # returnMap.pop("score", movie_scores[i])

    return returnMap


if __name__ == '__main__':
    movie_list = douBan250()
    print(movie_list)
