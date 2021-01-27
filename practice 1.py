from mcpi.minecraft import Minecraft


import random,time
while True:
    x,y,z = mc.player.getTilePos()
    
    color = random.randrange(0,9)
    mc.setBlock(x,y,z-1,38,color)
    time.sleep(0.01)           

