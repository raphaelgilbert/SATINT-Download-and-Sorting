def area(coo) :
    x = coo[1]
    y = coo[0]
    tlxx = x+0.006
    tlyy = y-0.006
    brxx = x-0.006
    bryy = y+0.006
    return(tlxx, tlyy, brxx, bryy)
    