# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
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

# deforestation
def cut_trees(height):
    for c in range(height):
        agent.destroy(FORWARD)
        agent.move(UP, 1)
    agent.move(DOWN, height)
    agent.collect_all()

# mining ore
def mining(length):
    for o in range(length): 
        agent.destroy(FORWARD)
        agent.destroy(DOWN)
        agent.destroy(LEFT)
        agent.destroy(RIGHT)
        agent.collect_all()
        agent.move(FORWARD, 1)

# build wall
def on_chat(length,height):
    for j in range(length):
        for i in range(height):
            agent.place(FORWARD) 
            agent.move(UP, 1)
        agent.move(DOWN, height)
        agent.move(RIGHT, 1)

        


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
    
# deforestation

player.on_chat("cut", cut_trees)

# mining ore
player.on_chat("mine", mining)

# build wall
player.on_chat("run", on_chat)