# Good patterns

good_pattern1 = '''
X---------X
'''

good_pattern2 = '''
X
|
|
X
'''

good_pattern3 = '''
   +--------+   
X--+        +--+
               |
               X
'''

good_pattern4 = '''

   +-------------+
   |             |
   |      X------+
X--+

'''

good_pattern5 = '''

   +-------+     
   |      +++---+
X--+      +-+   X

'''

good_pattern6 = '''

      +------+
      |      |
X-----+------+
      |       
      X       

'''

good_pattern7 = '''

+-----------+
|           |
+-------+   |
        |   |
        |   |
    X---+   |
            |
            |
    X-------+
             
'''

good_pattern8 = '''

X---+       +---+---+
    |       |   |   |
    +---+   |   +---+
        |   |       |
+---+   +---+   +---+
|   |           |   |
|   +---+---+---+   +---+
|           |           |
+---+---+   +---+---+   +---+
        |       |   |
    +---+   +---+   +-------+
    |           |           |
+---+   +---+   +---+   +---+
|       |   |       |   |
+---+   |   +-------+   +---+---X
    |   |              +----+   |
    +---+--------------+|       |
                       ++-------+
                       
'''


# Bad patterns


bad_pattern1 = '''

X-----|----X

'''

bad_pattern2 = '''

X
|
+
X

'''

bad_pattern3 = '''

   |--------+   
X---        ---+
               |
               X

'''

bad_pattern4 = '''

   +------ 
   |       
X--+      X

'''

class Neighbors:
    def __init__(
        self,
        column: int,
        row: int,
        table: dict[tuple[int, int], str],
    ):
        self.top = (column, row-1)
        self.bottom = (column, row+1)
        self.right = (column+1, row)
        self.left = (column-1, row)
        
        self.all = [
            self.top,
            self.bottom,
            self.right,
            self.left
        ]
        
        self.valued_coordinates = [
            i for i in self.all if
            i in table
            and
            table[i] != " "
        ]
        
                
        self.vertical_neighbors = [
            i for i in [self.top, self.bottom] if i in self.valued_coordinates
        ]
        
        self.horizontal_neighbors = [
            i for i in [self.right, self.left] if i in self.valued_coordinates
        ]
        
class Holder:
    def __init__(
        self,
        main: tuple[tuple[int, int]] = tuple(),
        subs: tuple[tuple[int, int]] = tuple(),
    ):
        self.main = main
        self.subs = subs
        

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
        
        self.prv = self.find_prv()
        
        self.neighbors = self.create_neighbors()
        
    def find_prv(self) -> tuple[int, int] | None:
        intersection = [i for i in self.path if i in self.all_neighbors.valued_coordinates]            
        if intersection:
            return intersection[-1]
        return None
    
    def have_unused_neighbor(self, coordinates: tuple[int, int]):
        n = Neighbors(*coordinates, self.table)
        check = set(n.valued_coordinates).issubset(self.path)
        if check:
            return False
        return True
    
        
    def is_neighbor(self, desired_coordinates: tuple[int, int]) -> bool:
        
        if desired_coordinates == self.prv:
            return False
        
        if desired_coordinates not in self.path or self.have_unused_neighbor(desired_coordinates):
            return True
        
        return False
    
    def create_neighbors(self) -> Holder:        
        holder: Holder = Holder()
        
        main = list()
        subs = list()
        
        if self.value == "X":
            main = self.all_neighbors.valued_coordinates
        
        if self.value == "-":
            main = [ i for i in self.all_neighbors.horizontal_neighbors if self.table[i] != "|" ]
                    
        if self.value == "|":
            main = [ i for i in self.all_neighbors.vertical_neighbors if self.table[i] != "-" ]
        
        if self.value == "+":
            
            for coordinates in self.all_neighbors.valued_coordinates:
                
                if coordinates not in self.table or coordinates in self.path:
                    continue

                if self.prv in self.all_neighbors.horizontal_neighbors:
                    if coordinates in self.all_neighbors.vertical_neighbors and self.table[coordinates] != "-":
                        main.append(coordinates)
                    elif coordinates in self.all_neighbors.horizontal_neighbors and self.table[coordinates] != "|":
                        subs.append(coordinates)

                elif self.prv in self.all_neighbors.vertical_neighbors:
                    if coordinates in self.all_neighbors.horizontal_neighbors and self.table[coordinates] != "|":
                        main.append(coordinates)
                    elif coordinates in self.all_neighbors.vertical_neighbors and self.table[coordinates] != "-":
                        subs.append(coordinates)


        main = [ i for i in main if (self.is_neighbor(i) and i in self.all_neighbors.valued_coordinates)]
        subs = [ i for i in subs if (self.is_neighbor(i) and i in self.all_neighbors.valued_coordinates)]
        
        holder.main = tuple(main)
        holder.subs = tuple(subs)
                                                
        return holder
        
        
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
    data: str,
) -> tuple[tuple[int, int], list[list[str]], dict[tuple[int, int], str], tuple[int, int]]:
    
    lines = data.strip().split("\n")

    grid: list[list[str]] = [ list(i) for i in lines ]
    
    max_row_length = max( len(row) for row in grid )
    
    grid: list[list[str]] = [ row + [ " " for _ in range(max_row_length - len(row)) ] for row in grid]

    table: dict[tuple[int, int], str] = {
        (column_index, row_index): value
            for row_index, row in enumerate(grid)
                for column_index, value in enumerate(row)
    }
        
    start_coordinates = next(
        (column_index, row_index)
        for row_index, row in enumerate(grid)
            for column_index, value in enumerate(row)
                if value == "X"
    )
    
    row_length = len(grid)
    column_length = max_row_length
    
    length = (column_length, row_length)
    
    return length, grid, table, start_coordinates

def navigate(
    start_coordinates: tuple[int, int],
    table: dict[tuple[int, int], str],
) -> list[list[tuple[int, int]]]:        
    
    def explore(
        current_path: list[tuple[int, int]] = [start_coordinates],
    ) -> list[list[tuple[int, int]]]:
        
        latest_coordinates = current_path[-1]
        value = table[latest_coordinates]

        if len(current_path) > 1 and value == "X":
            return [current_path]
            
        cell = Cell(latest_coordinates, current_path, table)
        
        all_paths: list[list[tuple[int, int]]] = []
                    
        for main in cell.neighbors.main:
            result = explore(current_path + [main])
            if result:
                all_paths.extend(result)
                            
        if len(cell.neighbors.main) > 0:
            for sub in cell.neighbors.subs:
                result = explore(current_path + [sub])
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
    
    length, grid, table, start = prepare_data(good_pattern8)
    
    show(grid)
    
    modes = navigate(start, table)
    
    print("-"*50, f" All correct paths - {len(modes)} path ", "-"*50)
    
    for index, path in enumerate(modes, 1):
        print("\n", f"Path {index}:")
        print("\n")
        print(path)
        grid = create_path_grid(length, path, table)
        show(grid)
