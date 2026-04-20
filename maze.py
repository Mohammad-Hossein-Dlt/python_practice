import random

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

class Cell:
    
    def __init__(
        self,
        coordinates: tuple[int, int],
        path: list[tuple[int, int]],
        table: dict[tuple[int, int], str],
    ):
        self.coordinates = coordinates
        self.value = table[coordinates]
        self.path = path
        self.table = table
        
        self.all_neighbors = Neighbors(*coordinates, table)
                
        self.neighbors = list(filter(lambda x: self.is_allowed(x), self.all_neighbors.valued_coordinates))
    
    def is_allowed(self, coordinates: tuple[int, int]) -> bool:
        if coordinates in self.table and coordinates not in self.path and self.value == 0:
            return True
        
        return False
    
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
    
def prepare_data(
    column: int,
    row: int,
) -> tuple[list[list[int]], dict[tuple[int, int], int]]:
        
    total = column * row
    
    values = ( [0] * int((total * 0.4)) ) + ( [1] * int((total * 0.6)) )
    
    random.shuffle(values)
    
    values[0] = 0
    values[-1] = 0
            
    grid = [values[i*column:(i+1)*column] for i in range(row)]
    
    table: dict[tuple[int, int], int] = {
        (column_index, row_index): value
            for row_index, row in enumerate(grid)
                for column_index, value in enumerate(row)
    }
    
    return grid, table    

def navigate(
    start_coordinates: tuple[int, int],
    end_coordinates: tuple[int, int],
    table: dict[tuple[int, int], str],
) -> list[list[tuple[int, int]]]:
    
    def explore(
        current_path: list[tuple[int, int]] = [start_coordinates],
    ) -> list[list[tuple[int, int]]]:          
    
        latest_coordinates = current_path[-1]

        if latest_coordinates == end_coordinates and table[latest_coordinates] == 0:
            return [current_path]
            
        cell = Cell(latest_coordinates, current_path, table)
        
        all_paths: list[list[tuple[int, int]]] = []
                    
        for main in cell.neighbors:
            result = explore(current_path + [main])
            if result:
                all_paths.extend(result)

        return all_paths
    
    return explore()

def create_path_grid(
    length: tuple[int, int],
    path: list[tuple[int, int]],
    table: dict[tuple[int, int], str],
) -> list[list[str]]:
    grid = [ [ " " for _ in range(length[0]) ] for i in range(length[1]) ]
    
    row_length = len(grid)
    column_length = len(grid[0])
    
    for coordinates in path:
        column = coordinates[0]
        row = coordinates[1]
        if column_length >= column and row_length >= row:
            grid[row][column] = table[coordinates]
                
    return grid

if __name__ == "__main__":
    
    scale = (10, 6)
    
    grid, table = prepare_data(*scale)
    
    modes = navigate((0, 0), (scale[0]-1, scale[1]-1), table)
    
    show(grid)
    
    if not modes:
        print("No path exist.")

    for index, path in enumerate(modes, 1):
        print(f"Path {index}:")
        print("\n")
        print(path)
        new_grid = create_path_grid(scale, path, table)
        show(new_grid)
            