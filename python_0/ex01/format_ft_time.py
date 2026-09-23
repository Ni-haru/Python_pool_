import datetime
import time

print("form 1 with datetime")
print(datetime.datetime.now())

print("form 2 with time")
print(time.time())
print("Current local time:", time.ctime())

print("form we need")
print(f"Seconds since January 1, 1970: {time.time()}")
print(f"{time.time():.2e}")
print(datetime.datetime.now().strftime("%b %d %Y"))
