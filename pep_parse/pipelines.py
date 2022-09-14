import datetime as dt

from pathlib import Path


BASE_DIR = Path(__file__).parents[1]
RESULT_DIR = BASE_DIR / 'results'
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'


class PepParsePipeline():

    def __init__(self) -> None:
        self.results_dir = RESULT_DIR
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.results_data = {}

    def process_item(self, item, spider):
        status = item['status']
        self.results_data[status] = self.results_data.get(status, 0) + 1
        return item

    def close_spider(self, spider):
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        total = 0
        with open(
                f'{RESULT_DIR}/status_summary_{now_formatted}.csv',
                mode='w',
                encoding='utf-8'
        ) as f:
            f.write('Статус, Количество\n')
            for key, value in self.results_data.items():
                total += int(value)
                f.write(f'{key}, {value}\n')
            f.write(f'Total,{total}\n')
