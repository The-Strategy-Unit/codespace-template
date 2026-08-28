import time

i = 0
minutes = 5
while True:
    print("it's been", i, "minute since this started. Thank you for your patience!")
    i = i + minutes
    time.sleep(minutes * 60)
