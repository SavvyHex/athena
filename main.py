import pygame as pg

from engine import *
from settings import *

def main() -> None:
    pg.init()
    screen = pg.display.set_mode(RES)
    clock = pg.time.Clock()
    screen.fill(pg.Color("gray"))
    gs = GameState()

    running = True
    square_selected = tuple()
    selection = list()
    
    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False
    
            elif e.type == pg.MOUSEBUTTONDOWN:
                location = pg.mouse.get_pos()
                column = location[0]//SQUARE_SIZE
                row = location[1]//SQUARE_SIZE
                if square_selected == (row, column):
                    square_selected = tuple()
                    selection = list()
                else:
                    square_selected = (row, column)
                    selection.append(square_selected)
                    if len(selection) == 2:
                        move = Move(selection[0], selection[1], gs.board)
                        gs.move(move)
                        square_selected = tuple()
                        selection = list()

        draw(screen, gs)
        clock.tick(FPS)
        pg.display.flip()

def draw(screen:pg.display, gs:GameState) -> None:
    drawBoard(screen)
    drawPieces(screen, gs)

def drawBoard(screen:pg.display) -> None:
    colours = [pg.Color("white"), pg.Color("gray")]
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            pg.draw.rect(screen, colours[(row+column)%2], pg.Rect(column*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def drawPieces(screen:pg.display, gs:GameState) -> None:
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            piece = gs.board[row][column]
            if piece != "--":
                screen.blit(gs.images[piece], pg.Rect(column*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

if __name__ == "__main__":
    main()