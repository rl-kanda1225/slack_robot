import time
import sys
import traceback
from robt_con import *
SLEEP_INTERVAL =60*60*24# 24hour

if __name__ == "__main__":
    while True:
        print("{}: Starting scrape cycle".format(time.ctime()))
        try:
            sc()
        except KeyboardInterrupt:
            print("Exiting....")
            sys.exit(1)
        except Exception as exc:
            print("Error with the scraping:", sys.exc_info()[0])
            traceback.print_exc()
        else:
            print("{}: Successfully finished scraping".format(time.ctime()))
            time.sleep(SLEEP_INTERVAL)
