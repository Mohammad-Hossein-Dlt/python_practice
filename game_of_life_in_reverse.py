pattern1 = [
    [1,0,0,1,0],
    [0,1,1,0,0],
    [1,0,0,1,0],
    [0,0,0,0,1],
]

pattern2 = [
    [0,0,0,0],
    [1,0,1,0],
    [0,1,1,0],
    [0,1,0,0],
]

pattern3 = [
    [0, 1, 1, 0, 0],
    [1, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

class Neighbors:
    def __init__(
        self,
        column: int,
        row: int,
        table: dict[tuple[int, int], str],
    ):
        self.top = (column, row-1)
        self.topL = (column-1, row-1)
        self.topR = (column+1, row-1)
        self.bottom = (column, row+1)
        self.bottomL = (column-1, row+1)
        self.bottomR = (column+1, row+1)
        self.right = (column+1, row)
        self.left = (column-1, row)
        
        self.all = [
            self.top,
            self.topL,
            self.topR,
            self.bottom,
            self.bottomL,
            self.bottomR,
            self.right,
            self.left
        ]
        
        self.valued_coordinates = [
            i for i in self.all if (i in table) and (table[i] != " ")
        ]
        
        self.values = [
            table[i] for i in self.valued_coordinates
        ]

class Cell:
    
    def __init__(
        self,
        coordinates: tuple[int, int],
        table: dict[tuple[int, int], int],
    ):
        self.coordinates = coordinates
        self.value = table[coordinates]
        self.table = table
                
        self.neighboors = Neighbors(*coordinates, table)
        
    def next_position(self) -> int | None:
        
        neighboors = self.neighboors.values
        
        if len(neighboors) == 0:
            return None
        
        alives_neighboors = neighboors.count(1)
                
        if self.value == 1 and alives_neighboors in [2, 3]:
            
            return 1
        
        elif self.value == 0 and alives_neighboors == 3:
         
            return 1
        
        else:
        
            return 0
        
def show(data: list[list[str]]) -> None:
    
    print("\n")
    
    w = " |   "

    length = len(w)
        
    width: str = " "*length
    
    x_indicator = [ str(i) for i in range(len(data[0])) ]
    
    x_indicator_str = (width*2)+width.join(x_indicator)
    
    divider = ( " " * (length + w.index("|")) ) + "".join([ "—" for _ in range(len(x_indicator_str) - (length + w.index("|")))])
    
    print(x_indicator_str)
    print(divider)
    
    for row_index, row in enumerate(data):
        
        row_items = [ ( " " * ( len( str(column_index) ) - 1) ) + str(value) for column_index, value in enumerate(row)]
        
        y_indicator = str(row_index).rjust(length) + w
        
        row_str = y_indicator + width.join(row_items)
        
        print(row_str)
        if row_index != len(data) -1:
            print(width+w)
        
        
    print("\n")
        
def prepare_data(current_gen: list[list[int]]) -> dict[tuple[int, int], int]:
    table = {
        (cell_index, row_index): cell
        for row_index, row in enumerate(current_gen)
            for cell_index, cell in enumerate(row)
    }
    return table

def create_next_generation(current_gen: list[list[int]], table: dict[tuple[int, int], int]) -> list[list[int]]:
    
    next_generation = [ [] for _ in range(len(current_gen)) ]

    for coordinates in table:
        column, row = coordinates
        new_cell = Cell(coordinates, table)
        next_generation[row].insert(column, new_cell.next_position())
        
    return next_generation


if __name__ == "__main__":
    
    print("\n", "Pattern: ")

    show(pattern3)

    table: dict[tuple[int, int], int] = prepare_data(pattern3)

    print("\n", "Next generation: ")

    next: list[list[int]] = create_next_generation(pattern3, table)

    show(next)