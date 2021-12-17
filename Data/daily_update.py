import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import auto_download
import unzip
import data_preprocess
import merge_country
import csv_to_html

def func():
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('start time: ',ts)

    auto_download.auto_download()

    file = 'D:/GLA Lessons/MSc Project/Data/test/data.zip'
    unzip.un_zip(file)

    data_preprocess.data_preprocess()
    merge_country.merge_country()
    csv_to_html.show_csv()

    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('update time: ',ts)

def update():
    # BlockingScheduler
    scheduler = BlockingScheduler()
    
    # 10s test
    scheduler.add_job(func, 'interval', seconds=10, id='test_job1')
    
    # update every 6 hours
    # scheduler.add_job(func, 'interval', hours=6, id='test_job1')

    scheduler.start()


if __name__ == '__main__':
    update()
