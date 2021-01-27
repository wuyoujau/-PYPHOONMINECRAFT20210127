from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    hits = mc.events.pollBlockHits()
    if len(hits)>0:
        a = hits[0]
        x,y,z = a.pos.x,a.pos.y,a.pos.z
        block = mc.getBlock(x,y,z)
        mc.postToChat("你打到了了"+str(block))
        if block == 1:
            mc.setBlock(x,y,z,41)

