from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    hits = mc.events.pollProjectileHits()
    if len(hits) > 0 :
        a = hits[0]
        x,y,z = a.pos.x,a.pos.y,a.pos.z
        mc.player.setTilePos(x,y,z)
        mc.spawnEntity(x,y,z,99)