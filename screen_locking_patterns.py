from string import ascii_uppercase

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
        value: str,
        table: dict[tuple[int, int], str],
    ):
        self.coordinates = coordinates
        
        self.column = coordinates[0]
        self.row = coordinates[1]
        
        self.value = value
        
        self.table = table
        
        self.neighboors = Neighbors(*coordinates, table)
    
    def find_accessible(self, path: list[tuple[int, int]] = []) -> list[tuple[int, int]]:
        
        accessibles: list[tuple[int, int]] = []
        
        for coordinates in self.table:
                     
            if self.can_connect(*coordinates):
                accessibles.append(coordinates)
            else:
                betweens = self.find_betweens(*coordinates)
                        
                intersection = list(set(path).intersection(betweens))
                
                if len(intersection) == len(betweens):
                    accessibles.append(coordinates)
                
        return accessibles
        
    
    def can_connect(self, column: int, row: int) -> bool:
        
        column_difference = abs(self.column - column)
        row_difference = abs(self.row - row)
        
        if (column, row) in self.neighboors.valued_coordinates:
            # neighboor
            return True
        
        if column_difference >= 1 and row_difference >= 1 and column_difference != row_difference:
            # accessible
            return True
        
        # blocked
        return False
    
    def find_betweens(self, column: int, row: int) -> list[str]:
        column_difference = abs(self.column - column)
        row_difference = abs(self.row - row)
        
        max_column = max([self.column, column])
        min_column = min([self.column, column])
        
        max_row = max([self.row, row])
        min_row = min([self.row, row])
        
        result = []
        
        if ((column, row) not in self.neighboors.valued_coordinates) and not (column_difference >= 1 and row_difference >= 1 and column_difference != row_difference):
            if self.column == column or self.row == row:
                if self.column == column:
                    for i in range(min_row+1, max_row):
                        result.append((self.column, i))
                if self.row == row:
                    for i in range(min_column+1, max_column):
                        result.append((i, self.row))
            
            if column_difference == row_difference:
                for c in range(min_column+1, max_column):
                    for r in range(min_row+1, max_row):
                        result.append((c, r))
                        
        
        return result

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
    scale: int,
) -> tuple[list[list[str]], dict[str, tuple[int, int]], dict[tuple[int, int], str]]:
    
    grid = [
        list(ascii_uppercase[i*scale: i*scale+scale])
        for i in range(scale)
    ]
    
    value_base_table = {
        cell: (cell_index, row_index)
        for row_index, row in enumerate(grid)
            for cell_index, cell in enumerate(row)
    }
    
    coordinates_base_table = {
        (cell_index, row_index): cell
        for row_index, row in enumerate(grid)
            for cell_index, cell in enumerate(row)
    }
    
    return grid, value_base_table, coordinates_base_table
    
def navigate(
    coordinates: tuple[int, int],
    length: int,
    table: dict[tuple[int, int], str],
) -> list[list[tuple[int, int]]]:
        
    def explore(
        current_path: list[tuple[int, int]] = [coordinates],
    ) -> list[list[tuple[int, int]]]:
        
        last_coordinates = current_path[-1]
        
        cell = Cell(last_coordinates, table[last_coordinates], table)
        
        
        if len(current_path) == length:
            return [current_path]
    
        all_paths: list[list[tuple[int, int]]] = []

        for nxt in cell.find_accessible(current_path):
            if nxt not in current_path:
                result = explore(current_path + [nxt])
                if result:
                    all_paths.extend(result)
            
        return all_paths
    
    return explore()

if __name__ == "__main__":
    
    start = "E"
    
    path_length = 9
    
    scale = 3
    
    grid, value_base_table, table = prepare_data(scale)
    
    show(grid)
        
    modes = navigate(value_base_table[start], path_length, table)
    
    length = len(modes)
    
    print(f"Modes = {length}", "\n")
    
    valued_modes = [ [ table[coordinates] for coordinates in path ] for path in modes ]
    
    for path in valued_modes:
        print(path)


'''

E = 23280

B, D, F, H = 15564

A, C, G, I = 13792

'''