import pygame as pg

def load_images() -> dict:
    imgs = dict()
    for piece in ["bp", "bR", "bN", "bB", "bQ", "bK", "wQ", "wK", "wB", "wN", "wR", "wp"]:
        imgs[piece] = pg.image.load(f"assets/images/{piece}.png")
    return imgs