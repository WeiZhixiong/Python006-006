from itemadapter import ItemAdapter
import csv


class MaoYanPipeline:

    def __init__(self):
        columns = ["movie_name", "movie_type", "show_time"]
        file_name = "movie_list.csv"
        self.file = open(file_name, 'a+', newline='', encoding='utf-8')
        self.writer = csv.DictWriter(self.file, columns)
        self.writer.writeheader()

    def process_item(self, item, spider):
        self.writer.writerow(item)
        return item

    def close_spider(self, spider):
        self.file.close()
