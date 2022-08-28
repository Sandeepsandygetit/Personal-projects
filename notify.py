import time
from plyer import notification


if __name__ =="__main__":
   while True:
        notification.notify(
          title="Good Thoughts",
          message="What you think you become.Thinking makes situations good or bad",
          timeout=5)
        time.sleep(10)