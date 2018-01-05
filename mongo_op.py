# code-encoding utf-8

from pymongo import MongoClient


class MongoUtil:
    def __init__(self):
        self.client = MongoClient("127.0.0.1", 27017)
        self.db = self.client.sina
        self.collection = self.db.sina_data

    def insert(self, data):
        self.collection.insert(data)

    # 获取所有数据
    def get_data_list(self):
        return self.collection.find()

    # 获取分页数据
    def get_page_data(self, page_num):
        return self.collection.find().skip(10*page_num).limit(10)



if __name__ == "__main__":
    mongo_util = MongoUtil()
    data_list = mongo_util.get_data_list()
    for data in data_list:
        print(data["url"])