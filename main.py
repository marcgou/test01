#test
import ping3
try:
    while 1:
        test = ping3.ping('8.8.8.8', timeout=0.1)
        print(test)
except Exception as e:
    print("type error: " + str(e))
