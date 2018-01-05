# 主函数
from xinlang_split import url_manager, html_download, html_parser, html_output, mongo_op

class SpiderMain(object):
    def __init__(self):
        self.urls_set = url_manager.UrlManager()
        self.downloader = html_download.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.output = html_output.HtmlOutputer()
        self.db_util = mongo_op.MongoUtil()

    def craw(self, root_url):
        count = 1
        self.urls_set.add_new_url(root_url)
        print(self.urls_set.has_new_url())
        while self.urls_set.has_new_url():
            try:
                new_url = self.urls_set.get_new_url()
                print('craw %d : %s' % (count, new_url))
                # 下载网页内容
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                # print('对应的数据%s' % new_data)
                if new_data.get("title", None) is not None:
                    self.db_util.insert(new_data)
                print("insert to database successful")
                self.urls_set.add_new_urls(new_urls)
                self.output.collect_data(new_data)
                if count == 500:
                    break
                count = count + 1
            except Exception as e:
                print("craw %d failed" % count)

        self.output.output_html()


if __name__ == '__main__':
    # 设置入口爬虫url
    root_url = 'http://www.sina.com.cn'
    # 启动爬虫
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
