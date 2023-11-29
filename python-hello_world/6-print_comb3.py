for i in range(10):
    for p in range(i+ 1,10):
        print("{:02d}".format(i*10 +p), end= ", " if(i!=8 or p!=9) else "\n")