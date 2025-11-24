
################# Function Section #############################

# teleport
def come():
   agent.teleport_to_player()

# moving
def forward(steps):
    agent.move(FORWARD, steps)

def back(steps):
    agent.move(BACK, steps)

def up(steps):
    agent.move(UP, steps)

def down(steps):
    agent.move(DOWN, steps)

# turning
def left():
    agent.turn(TurnDirection.LEFT)

def right():
    agent.turn(TurnDirection.RIGHT)

#obby1
def movestep():
    agent.move(FORWARD, 4)
    agent.turn(TurnDirection.LEFT)
    agent.move(FORWARD, 4)
    agent.turn(TurnDirection.RIGHT)
    agent.move(FORWARD, 3)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 4)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
# mf 4
# lt
# mf 5
# rt
# mf 3
# up n fw 3
# fw 1
# dw n fw 3
################## On Chat Commands Section #####################

# teleport
player.on_chat("c", come)

# moving
player.on_chat("mf", forward)

player.on_chat("bk", back)

player.on_chat("up", up)

player.on_chat("dw", down)

# turning
player.on_chat("lt", left)

player.on_chat("rt", right)

#obby1

player.on_chat("obby", movestep)
    
