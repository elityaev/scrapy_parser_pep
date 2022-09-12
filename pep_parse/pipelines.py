import datetime as dt

from pep_parse.settings import BASE_DIR, RESULTS_DIR

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'


class PepParsePipeline():

    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS_DIR
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.results_data = {}

    def process_item(self, item, spider):
        status = item['status']
        if status not in self.results_data:
            self.results_data[status] = 1
        else:
            self.results_data[status] += 1
        print(self.results_data)
        return item

    def close_spider(self, spider):
        print(self.results_data)
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        total = 0
        with open(
                f'{RESULTS_DIR}/status_summary_{now_formatted}.csv',
                mode='w',
                encoding='utf-8'
        ) as f:
            f.write('Статус, Количество\n')
            for key, value in self.results_data.items():
                total += int(value)
                f.write(f'{key}, {value}\n')
            f.write(f'Total,{total}\n')
