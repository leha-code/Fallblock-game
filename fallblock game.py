#Importing all the needed modules.
#Some commented functions are in beta developement.
#Points are still in beta.
from mcpi.minecraft import Minecraft
from mcpi import block as block
import sys
from time import sleep
mc = Minecraft.create()
limit = 0
level = 0
points = 0
inpt = ' '
while inpt != 'exit' or 'n' or 'N':
    mc.saveCheckpoint()
    pos = mc.player.getTilePos()
    mc.setBlocks(pos.x + 6, pos.y - 11, pos.z + 6, pos.x - 6, pos.y + 20, pos.z - 6, block.ICE)
    mc.setBlocks(pos.x + 5, pos.y - 10, pos.z + 5, pos.x - 5, pos.y + 20, pos.z - 5, block.AIR)
    mc.postToChat('Fall BLK 1.8')
    mc.postToChat('=================')
    mc.postToChat('======   ========')
    mc.postToChat('=========== =====')
    mc.postToChat('===   ===========')
    mc.postToChat('=================')
    mc.postToChat('Enter Your level in the Shell')
    level = input('Do not use more than 5 for best effect. Write the level here:')
    limiter = input('use 0 for defalut. Write the score adder here:')
    level = int(level)
    limiter = int(limiter)
    print('Go back to Minecraft window')
    mc.postToChat('Click the right mouse button as much as you can. Avoid sand')
    mc.postToChat('And hold a sword.')
    while limit != 100 + limiter:
        ps = mc.player.getTilePos()
        blk1 = mc.getBlock(ps.x, ps.y, ps.z)
        blk2 = mc.getBlock(ps.x, ps.y + 1, ps.z)
        #if blk1 and blk2 != 0:
            #sleep(2)
            #if blk1 and blk2 != 0:
                #mc.restoreCheckpoint()
                #mc.player.setTilePos(0, 100, 0)
                #sys.exit
            #elif blk1 and blk2 == 0:
             #   points = points + 1
        for hit in mc.events.pollBlockHits():
                p = mc.player.getTilePos()
                mc.setBlock(p.x, p.y + 10 - level, p.z, block.SAND)
                limit = limit + 1
                mc.setBlock(p.x, p.y - 1, p.z, block.MELON)
    mc.postToChat('Whoa, Whoa stop there, you won, phew!')
    mc.setBlocks(pos.x + 6, pos.y - 11, pos.z + 6, pos.x - 6, pos.y + 20, pos.z - 6, block.AIR)
    mc.restoreCheckpoint()
    mc.player.setTilePos(0, 100, 0)
    #mc.postToChat('You scored: ', points)
    mc.postToChat('Go to the shell')
    inpt = input('Type exit or n/N to quit.')
sys.exit()