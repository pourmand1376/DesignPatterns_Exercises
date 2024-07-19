class FontInfo():
    def __init__(self, font_family, font_size, is_bold) -> None:
        self._font_family = font_family
        self._font_size = font_size
        self._is_bold = is_bold
        print("a new font is created")

    @property
    def font_size(self):
        return self._font_size
    
    @property
    def font_family(self):
        return self._font_family
    
    @property
    def is_bold(self):
        return self._is_bold
    
    @staticmethod
    def should_show_info(item):
        return item if item is not None else ""


    def render_font(self):
        return f"[{self.font_family}]{FontInfo.should_show_info(self.font_size)}{FontInfo.should_show_info(self.is_bold)}"

class FontFactory():
    def __init__(self):
        self.fonts = {}

    def get_font(self, font_family: str, font_size: int=None, is_bold:bool=None):
        key= (font_family, font_size, is_bold)
        if key not in self.fonts:
            self.fonts[key] = FontInfo(font_family=font_family, font_size=font_size, is_bold=is_bold)
        
        return self.fonts[key]


class Cell:
    def __init__(self, row, column, font_info:FontInfo=None):
        self.row = row
        self.column = column
        self.content = None
        self.font_info = font_info

    def should_show_info(self, item):
        return item if item is not None else ""

    def render(self):
        print(f"({self.row}, {self.column}): {self.content} {self.font_info.render_font()}")


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
        self.font_factory = FontFactory()
        self.generate_cells()

    def set_content(self, row, col, content):
        self.ensure_cell_exists(row, col)
        self.cells[row][col].content = content

    def set_font_family(self, row, col, font_family,font_size=None, is_bold=None):
        self.ensure_cell_exists(row, col)
        font=self.font_factory.get_font(font_family=font_family,font_size=font_size,is_bold=is_bold)
        self.cells[row][col].font_info = font

    def ensure_cell_exists(self, row, col):
        if row < 0 or row >= self.MAX_ROWS:
            raise ValueError("Invalid row index")
        if col < 0 or col >= self.MAX_COLS:
            raise ValueError("Invalid column index")

    def generate_cells(self):
        font=self.font_factory.get_font(self.FONT_FAMILY,self.FONT_SIZE, self.IS_BOLD)
        for row in range(self.MAX_ROWS):
            for col in range(self.MAX_COLS):
                cell = Cell(row, col)
                cell.font_info = font
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
    sheet.set_font_family(1,1,"AmirTest", 11, True)
    sheet.render()

if __name__ == "__main__":
    main()

