import schedule
import time
import tests.system_test_031220 as t

schedule.every(5).minutes.do(t.test)

t.test()

while True:
    schedule.run_pending()
    time.sleep(1)

