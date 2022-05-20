def findWaterPurity(waterSample):
    salty=0
    hydrogen=0
    oxygen=0

    for ws in waterSample:
        if ws>=0 and ws<=9:
            salty+=ws
        elif ws>=10 and ws<=99:
            hydrogen+=ws
        elif ws>=100 and ws<=999:
            oxygen+=ws
    total=salty+hydrogen+oxygen
    salty=((salty/total)*100)
    hydrogen=(hydrogen/total)*100
    oxygen=(oxygen/total)*100

    if salty==0.0 and hydrogen==70.0 and oxygen==30.0:
        print("Water is pure")
    else:
        print("Water is not pure")

    print("Salt % in water:{}%".format(salty))
    print("Hydrogen % in water{}%:".format(hydrogen))
    print("Oxygen % in water:{}%".format(oxygen))

#Driver code
waterSample=[1,80,628,2,72,92,3]
findWaterPurity(waterSample)
waterSample=[5,69,300,4,67,58,3]
findWaterPurity(waterSample)
waterSample=[9,70,300,8,300,67,7]
findWaterPurity(waterSample)





