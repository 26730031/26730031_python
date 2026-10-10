h, m = map(int, input().split())
if h >= 12:
    print("%02d : %02d PM" % (h-12 if h > 12 else h, m))
else:
    print("%02d : %02d AM" % (h, m))
