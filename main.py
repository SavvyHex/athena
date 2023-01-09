import pygame as pg

from engine import GameState
from settings import *

def main() -> None:
    pg.init()
    screen = pg.display.set_mode(RES)
    clock = pg.time.Clock()
    screen.fill(pg.Color("gray"))
    gs = GameState()

    running = True

    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False
        
        draw(screen, gs)
        clock.tick(FPS)
        pg.display.flip()

def draw(screen:pg.display, gs:GameState) -> None:
    drawBoard(screen)
    drawPieces(screen, gs.board)

def drawBoard(screen:pg.display) -> None:
    colours = [pg.Color("white"), pg.Color("gray")]
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            pg.draw.rect(screen, colours[(row+column)%2], pg.Rect(column*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def drawPieces(screen:pg.display, board:list) -> None:
    pass

if __name__ == "__main__":
    main()