from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

unmber = 1

for i in range(8):
        for j in range(unmber):
            mc.spawnEntity(x,y,z,60)
            
        unmber = unmber * 2
        mc.postToChat('這次生成了'+str(unmber))

