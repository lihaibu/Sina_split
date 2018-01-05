# 网页解析器
from bs4 import BeautifulSoup
import re
import requests
class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        r = requests.get(page_url)
        r.encoding = "ISO-9959-1"
        data = r.text
        # herf 中的链接
        # links = re.findall('[http]{4}\\:\\/\\/([a-zA-Z]|[0-9])*(\\.([a-zA-Z]|[0-9])*)*(\\/([a-zA-Z]|[0-9])*)*\\s?', data)
        links = re.findall(r'href="http://www.sina.com.*"', data)
        for link in links:
            # new_url = link['href']
            # 将newurl按照pageurl的格式自动拼接成其相对应的练歌url
            # new_full_url = requests.urljoin(page_url,new_url)
            # new_urls.add(new_full_url)
            link = link.replace("href=", "")
            link = link.replace("\"", "")
            if link.find(" ") != -1:
                link = link[0:link.index(" ")]
            if link.find(">") != -1:
                link = link[0:link.index(">")]
            new_urls.add(link)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}
        res_data['url'] = page_url
        title_d = soup.find('div', attrs={"class":"main_content", "id":"pl_main_content"})
        if title_d is not None:
            title_h = title_d.find("h1")
            title = title_h.string
            res_data['title'] = title
        # title = soup.find('a', attrs = {'target': "_blank"})

        content = soup.find('div', attrs={'class':'BSHARE_POP blkContainerSblkCon'})
        if content is not None:
            pargs = content.find_all('p')
            text = ''
            for parg in pargs:
                text = text + parg.string
            res_data["content"] = text

        return res_data


    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='ISO-8859-1')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data
