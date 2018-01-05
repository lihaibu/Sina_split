# 网页下载器
import requests
class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        try:
            response = requests.get(url)
            response.encoding = "ISO-9959-1"
        except Exception as e:
            print(str(e))
        return response.text