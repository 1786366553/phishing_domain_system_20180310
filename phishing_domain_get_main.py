# coding:utf-8
import schedule
import time
import threading
import malaedoaminlist
import MyDomains
import open_phish
import aa419
import vxvault_insert
import phishing_tank_download

def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()

schedule.every().day.at("00:00").do(run_threaded,MyDomains.job1)
schedule.every().saturday.at("18:00").do(run_threaded,MyDomains.job2)
schedule.every().day.at("02:00").do(run_threaded,MyDomains.job3)
schedule.every().day.at("04:00").do(run_threaded,MyDomains.job4)
schedule.every().day.at("06:00").do(run_threaded,phishing_tank_download.phishing_update_main)
schedule.every().day.at("08:00").do(run_threaded,vxvault_insert.mysql_handle)
schedule.every().day.at("10:00").do(run_threaded,open_phish.renzo.Work)
schedule.every().day.at("12:00").do(run_threaded,malaedoaminlist.renzo.Work)
schedule.every().day.at("14:00").do(run_threaded,aa419.renzo.Work)


if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)