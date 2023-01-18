from utils import load_images

class GameState():
    def __init__(self) -> None:
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.whiteToMove = True
        self.moveLog = list()
        self.images = load_images()
    
    def move(self, move):
        self.board[move.start_row][move.start_column] = "--"
        self.board[move.end_row][move.end_column] = move.piece_selected
        self.moveLog.append(str(move))
        self.whiteToMove = not self.whiteToMove

class Move():
    ranks_to_rows = {"1" : 7, "2" : 6, "3" : 5, "4" : 4, "5" : 3, "6" : 2, "7" : 1, "8" : 0}
    rows_to_ranks = {v : k for k, v in ranks_to_rows.items()}

    files_to_cols = {"a" : 0, "b" : 1, "c" : 2, "d" : 3, "e" : 4, "f" : 5, "g" : 6, "h" : 7}
    cols_to_files = {v : k for k, v in files_to_cols.items()}

    def __init__(self, start_square, end_square, board) -> None:
        self.start_row, self.start_column = start_square
        self.end_row, self.end_column = end_square
        self.piece_selected = board[self.start_row][self.start_column]
        self.piece_captured = board[self.end_row][self.end_column]

    def __str__(self) -> str:
        return f"{self.piece_selected[1]}{self.cols_to_files[self.start_column]}{self.rows_to_ranks[self.start_row]}-{self.cols_to_files[self.end_column]}{self.rows_to_ranks[self.end_row]}"