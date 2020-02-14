def compute_lcm(x,y):
    if x > y:
        greater = x
    else:
        greater = y
    while true:
        if(greater % x ==0) and (greater % y ==0):
            lcm = greater
            break
            greater += 1
    return lcm