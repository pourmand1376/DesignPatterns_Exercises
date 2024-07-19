# the problem of this implementation is that font information is stored for each cell! 
# That should be separated.
# That is easy in a database way. But how you will store it in memory when no db is available?

class Cell:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.content = None
        self.font_family = None
        self.font_size = None
        self.is_bold = None

    def should_show_info(self, item):
        return item if item is not None else ""

    def render(self):
        font_info = f"[{self.font_family}]{self.should_show_info(self.font_size)}{self.should_show_info(self.is_bold)}"
        print(f"({self.row}, {self.column}): {self.content} [{font_info}]")


class SpreadSheet:
    MAX_ROWS = 3
    MAX_COLS = 3

    # In a real app, these values should not be hardcoded here.
    # They should be read from a configuration file.
    FONT_FAMILY = "Times New Roman"
    FONT_SIZE = 12
    IS_BOLD = False

    def __init__(self):
        self.cells = [[None for _ in range(self.MAX_COLS)] for _ in range(self.MAX_ROWS)]
        self.generate_cells()

    def set_content(self, row, col, content):
        self.ensure_cell_exists(row, col)
        self.cells[row][col].content = content

    def set_font_family(self, row, col, font_family):
        self.ensure_cell_exists(row, col)
        self.cells[row][col].font_family = font_family

    def ensure_cell_exists(self, row, col):
        if row < 0 or row >= self.MAX_ROWS:
            raise ValueError("Invalid row index")
        if col < 0 or col >= self.MAX_COLS:
            raise ValueError("Invalid column index")

    def generate_cells(self):
        for row in range(self.MAX_ROWS):
            for col in range(self.MAX_COLS):
                cell = Cell(row, col)
                cell.font_family = self.FONT_FAMILY
                self.cells[row][col] = cell

    def render(self):
        for row in range(self.MAX_ROWS):
            for col in range(self.MAX_COLS):
                self.cells[row][col].render()

def main():
    sheet = SpreadSheet()
    sheet.set_content(0, 0, "Hello")
    sheet.set_content(1, 0, "World")
    sheet.set_font_family(0, 0, "Arial")
    sheet.set_font_family(0, 2, "MyFont")
    sheet.render()

if __name__ == "__main__":
    main()

