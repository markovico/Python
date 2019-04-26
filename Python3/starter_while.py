#while loops


x = 0
while x<20:
    x += 1
    if( x%2 == 1):
        continue
    print(x)
    if( x == 8):
        break

print('Stopped looping!')


import time

sec_left = 10
while (sec_left>0):
    print(sec_left)
    sec_left -=1
    time.sleep(0.05)

print('Time is up!')

