
with open('Depth_Scans.txt') as f:
    depths = f.readlines()


def depth_increase(depth_list):
    y1 = int(depth_list[0])
    count = 0
    for depth in depth_list[1:]:
        y2 = int(depth)
        count += (y2 - y1)/abs(y2-y1)   #add 1 if positive, subtract 1 if negative
        y1 = int(depth)
    return ((len(depth_list) - 1) - count)/2 + count  #since we subtracted 1 when there was a decrease, that means
                                                      #the decreases were "counted twice" in context of finding
                                                      #total increases.  Therefore, You get the final count and
                                                      #find the difference between it and the total possible increases.
                                                      #Since the decreases were counted twice, only half this difference
                                                      #are actual decreases and therefore the other half are increases.


print(depth_increase(depths))



