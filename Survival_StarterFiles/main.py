from gamelib import *

game = Game(800,600, "TagOrGetTagged")
bk = Animation("images/background pygame.png",game)
game.setBackground(bk)


while not game.over:
    game.processInput
    game.scrollBackground("down",2)
