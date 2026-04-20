pattern1 = '''
+--+--+--+
|  |  |  |
+ -+--+--+
|  |  |  |
+--+--+--+
'''

pattern2 = '''
+--+--+--+
|  |     |
+  +  +--+
|  |  |  |
+--+--+--+
'''

pattern3 = '''
+--+--+--+
|  |     |
+  +  +--+
|        |
+--+--+--+
'''

pattern4 = '''

+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|  |     |  |     |  |  |  |  |     |  |     |  |  |     |  |  |     |  |     |  |  |  |  |     |  |     |  |  |     |  |
+  +--+  +--+  +  +  +  +--+  +--+  +--+  +--+  +--+  +  +--+  +--+  +--+  +  +  +  +--+  +--+  +--+  +--+  +--+  +  +--+
|     |  |  |     |  |  |  |  |     |     |  |  |     |  |        |  |  |     |  |  |  |  |     |     |  |  |     |  |  |
+--+  +  +--+  +--+  +  +  +--+  +  +  +--+  +  +  +--+  +  +--+  +  +--+  +--+  +  +  +--+  +  +  +--+  +  +  +--+  +  +
|  |  |     |  |  |     |  |  |  |  |  |     |  |  |  |     |  |  |     |  |  |     |  |  |  |  |  |     |  |  |  |     |
+  +--+  +  +--+  +  +--+  +  +--+  +  +--+  +  +  +--+  +  +  +--+  +  +--+  +  +--+  +  +--+  +  +--+  +  +  +--+  +  +
|  |  |  |     |  |  |  |     |  |     |  |  |     |  |  |  |  |  |  |     |  |  |  |     |  |     |  |  |     |  |  |  |
+--+--+  +--+  +  +--+  +--+  +--+  +  +  +--+  +--+  +  +  +--+--+  +--+  +  +--+  +--+  +--+  +  +  +--+  +--+  +  +  +
|     |  |     |  |  |  |  |     |  |     |  |     |  |  |  |     |  |     |  |  |  |  |     |  |     |  |     |  |  |  |
+  +  +  +--+  +--+  +  +--+  +  +--+  +--+  +  +--+  +  +--+  +  +  +--+  +--+  +  +--+  +  +--+  +--+  +  +--+  +  +--+
|  |  |  |  |     |  |  |  |     |  |  |  |     |  |  |  |     |  |  |  |     |  |  |  |     |  |  |  |     |  |  |  |  |
+--+  +--+  +--+  +--+  +--+  +--+  +  +  +  +--+  +  +--+  +--+  +--+  +--+  +--+  +--+  +--+  +  +  +  +--+  +  +--+  +
|  |     |  |     |  |  |     |  |     |  |  |     |  |     |  |     |  |     |  |  |     |  |     |  |  |     |  |     |
+  +  +--+  +  +--+  +  +--+  +  +  +--+  +--+  +  +--+  +--+  +  +--+  +  +--+  +  +--+  +  +  +--+  +--+  +  +--+  +--+
|  |  |  |  |     |  |  |     |  |  |  |  |     |  |  |  |  |  |  |  |  |     |  |  |     |  |  |  |  |     |  |  |  |  |
+--+  +--+  +  +--+  +--+  +--+  +--+  +  +--+  +  +--+  +  +--+  +--+  +  +--+  +--+  +--+  +--+  +  +--+  +  +--+  +  +
|     |  |  |     |  |     |  |  |     |  |     |  |  |     |     |  |  |     |  |     |  |  |     |  |     |  |  |     |
+  +--+  +--+  +--+  +  +--+  +  +  +--+  +  +--+  +  +--+  +  +--+  +--+  +--+  +  +--+  +  +  +--+  +  +--+  +  +--+  +
|  |  |     |  |  |     |  |  |     |  |  |  |     |  |  |     |  |     |  |  |     |  |  |     |  |  |  |     |  |  |  |
+--+  +  +--+  +  +--+  +  +  +--+  +--+  +--+  +  +  +--+  +--+  +  +--+  +  +--+  +  +  +--+  +--+  +--+  +  +  +--+  +
|  |     |  |     |  |  |     |  |  |     |  |  |  |     |     |     |  |     |  |  |     |  |  |     |  |  |  |     |  |
+  +--+  +--+  +--+  +  +--+  +  +  +  +--+  +  +--+  +--+  +  +--+  +--+  +--+  +  +--+  +  +  +  +--+  +  +--+  +--+  +
|  |  |  |  |  |     |  |     |  |  |  |     |  |  |  |     |  |  |  |  |  |     |  |     |  |  |  |     |  |  |  |     |
+--+  +  +  +--+  +--+  +--+  +--+  +  +--+  +--+  +--+  +--+--+  +  +  +--+  +--+  +--+  +--+  +  +--+  +--+  +--+  +--+
|     |  |     |  |  |     |  |     |  |  |     |  |  |  |        |  |     |  |  |     |  |     |  |  |     |  |  |  |  |
+  +--+  +  +--+  +--+  +  +--+  +  +--+  +--+  +  +--+  +  +  +--+  +  +--+  +--+  +  +--+  +  +--+  +--+  +  +--+  +  +
|  |  |     |  |  |     |  |  |  |  |     |  |  |  |     |  |  |  |     |  |  |     |  |  |  |  |     |  |  |  |     |  |
+  +  +--+  +  +--+  +  +--+  +  +  +--+  +--+  +  +--+  +--+  +  +--+  +  +--+  +  +--+  +  +  +--+  +--+  +  +--+  +--+
|  |     |  |     |  |  |  |  |     |  |     |  |  |     |  |  |     |  |     |  |  |  |  |     |  |     |  |  |     |  |
+  +--+  +--+  +  +  +  +--+  +--+  +--+  +--+  +--+  +  +--+  +--+  +--+  +  +  +  +--+  +--+  +--+  +--+  +--+  +  +--+
|     |  |  |     |  |  |  |  |     |     |  |  |     |  |        |  |  |     |  |  |  |  |     |     |  |  |     |  |  |
+--+  +  +--+  +--+  +  +  +--+  +  +  +--+  +  +  +--+  +  +--+  +  +--+  +--+  +  +  +--+  +  +  +--+  +  +  +--+  +  +
|  |  |     |  |  |     |  |  |  |  |  |     |  |  |  |     |  |  |     |  |  |     |  |  |  |  |  |     |  |  |  |     |
+  +--+  +  +--+  +  +--+  +  +--+  +  +--+  +  +  +--+  +  +  +--+  +  +--+  +  +--+  +  +--+  +  +--+  +  +  +--+  +  +
|  |  |  |     |  |  |  |     |  |     |  |  |     |  |  |  |  |  |  |     |  |  |  |     |  |     |  |  |     |  |  |  |
+--+--+  +--+  +  +--+  +--+  +--+  +  +  +--+  +--+  +  +  +--+--+  +--+  +  +--+  +--+  +--+  +  +  +--+  +--+  +  +  +
|     |  |     |  |  |  |  |     |  |     |  |     |  |  |  |     |  |     |  |  |  |  |     |  |     |  |     |  |  |  |
+  +  +  +--+  +--+  +  +--+  +  +--+  +--+  +  +--+  +  +--+  +  +  +--+  +--+  +  +--+  +  +--+  +--+  +  +--+  +  +--+
|  |  |  |  |     |  |  |  |     |  |  |  |     |  |  |  |     |  |  |  |     |  |  |  |     |  |  |  |     |  |  |  |  |
+--+  +--+  +--+  +--+  +--+  +--+  +  +  +  +--+  +  +--+  +--+  +--+  +--+  +--+  +--+  +--+  +  +  +  +--+  +  +--+  +
|  |     |  |     |  |  |     |  |     |  |  |     |  |     |  |     |  |     |  |  |     |  |     |  |  |     |  |     |
+  +  +--+  +  +--+  +  +--+  +  +  +--+  +--+  +  +--+  +--+  +  +--+  +  +--+  +  +--+  +  +  +--+  +--+  +  +--+  +--+
|  |  |  |  |     |  |  |     |  |  |  |  |     |  |  |  |  |  |  |  |  |     |  |  |     |  |  |  |  |     |  |  |  |  |
+--+  +--+  +  +--+  +--+  +--+  +--+  +  +--+  +  +--+  +  +--+  +--+  +  +--+  +--+  +--+  +--+  +  +--+  +  +--+  +  +
|     |  |  |     |  |     |  |  |     |  |     |  |  |     |     |  |  |     |  |     |  |  |     |  |     |  |  |     |
+  +--+  +--+  +--+  +  +--+  +  +  +--+  +  +--+  +  +--+  +  +--+  +--+  +--+  +  +--+  +  +  +--+  +  +--+  +  +--+  +
|  |  |     |  |  |     |  |  |     |  |  |  |     |  |  |     |  |     |  |  |     |  |  |     |  |  |  |     |  |  |  |
+--+  +  +--+  +  +--+  +  +  +--+  +--+  +--+  +  +  +--+  +--+  +  +--+  +  +--+  +  +  +--+  +--+  +--+  +  +  +--+  +
|  |     |  |     |  |  |     |  |  |     |  |  |  |     |     |     |  |     |  |  |     |  |  |     |  |  |  |     |  |
+  +--+  +--+  +--+  +  +--+  +  +  +  +--+  +  +--+  +--+  +  +--+  +--+  +--+  +  +--+  +  +  +  +--+  +  +--+  +--+  +
|  |  |  |  |  |     |  |     |  |  |  |     |  |  |  |     |  |  |  |  |  |     |  |     |  |  |  |     |  |  |  |     |
+--+  +  +  +--+  +--+  +--+  +--+  +  +--+  +--+  +--+  +--+--+  +  +  +--+  +--+  +--+  +--+  +  +--+  +--+  +--+  +--+
|     |  |     |  |  |     |  |     |  |  |     |  |  |  |        |  |     |  |  |     |  |     |  |  |     |  |  |  |  |
+  +--+  +  +--+  +--+  +  +--+  +  +--+  +--+  +  +--+  +  +  +--+  +  +--+  +--+  +  +--+  +  +--+  +--+  +  +--+  +  +
|  |  |     |  |  |     |  |  |  |  |     |  |  |  |     |  |  |  |     |  |  |     |  |  |  |  |     |  |  |  |     |  |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+

'''

class Cell:
    
    def __init__(
        self,
        column: int,
        row: int,
        pattern: str,
    ):
        self.x = column
        self.y = row 
        
        part1, part2, part3 = pattern.split('\n')
                
        self.top_wall, self.right_wall, self.bottom_wall, self.left_wall = False, False, False, False

        if part1.count("-") == 2:
            self.top_wall = True
        
        if part2[0] == '|':
            self.left_wall = True
        
        if part2[-1] == '|':
            self.right_wall = True
            
        if part3.count("-") == 2:
            self.bottom_wall = True
            
        self.top: tuple[int, int] = (column, row-1)
        self.right: tuple[int, int] = (column+1, row)
        self.bottom: tuple[int, int] = (column, row+1)
        self.left: tuple[int, int] = (column-1, row)
                
        self.walls: dict[tuple[int, int], bool] = {
            self.top: self.top_wall,
            self.right: self.right_wall,
            self.bottom: self.bottom_wall,
            self.left: self.left_wall,
        }
        
    def check_have_neighboor(self) -> bool:
        return not all(self.walls.values())
    
    def neighboors(self) -> list[tuple[int, int]] | None:
        n = list()
        if self.check_have_neighboor():
            for direction, wall in self.walls.items():
                if not wall:
                    n.append(direction)
        
        return n if n else None
    
def prepare_data(
    grid: str
) -> dict[tuple[int, int], list[tuple[int, int]]]:
    
    lines: list[str] = grid.strip().split('\n')
    
    max_line_length = max( len(line) for line in lines )
    
    lines: list[str] = [ line + ( " " * ( max_line_length - len(line) ) ) for line in lines]

    horizontal_lines = [line for line in lines if line.__contains__('+')]

    plus_number = sum(list(map(lambda x: x.count('+'), horizontal_lines)))

    vertical_lines = [line for line in lines if line.__contains__('|')]

    rows = len(vertical_lines)
    cols = int(plus_number / len(horizontal_lines)) - 1
    
    table: dict[tuple[int, int]: list[tuple[int, int]]] = dict()

    for row in range(rows):
        for column in range(cols):
            cell_lines = [
                lines[2*row][3*column:3*column+3+1],
                lines[2*row+1][3*column:3*column+3+1],
                lines[2*row+2][3*column:3*column+3+1],
            ]
            cell_data = "\n".join(cell_lines)
            cell = Cell(column, row, cell_data)
            table[(column, row)] = cell.neighboors() or []
            
    return table
                
def extract_components(
    graph: dict[tuple[int, int], list[tuple[int, int]]],
) -> list[list[tuple[int, int]]]:
    seen = set()
    result = []

    for node in graph:
        if node in seen:
            continue
        stack = [node]
        comp = []
        while stack:
            n = stack.pop()
            if n in seen:
                continue
            seen.add(n)
            comp.append(n)
            neighbors = (graph.get(n) or [])
            for other, neighs in graph.items():
                if neighs and n in neighs:
                    neighbors = neighbors + [other]
            stack.extend(neighbors)
        result.append(comp)

    return result

def count_components(
    components: list[list[tuple[int, int]]],
) -> list[tuple[int, int]]:
    count = {}
    for sublist in components:
        length = len(sublist)
        if length in count:
            count[length] += 1
        else:
            count[length] = 1

    result = sorted([(count[k], k) for k in count], reverse=True)
    return result

if __name__ == "__main__":
    
    table = prepare_data(pattern2)
    
    components = extract_components(table)
    
    count = count_components(components)
    
    for number, cell_number in count:        
        print()
        if cell_number > 1:
            print(f"We have {number} composite cells that were obtained from the combination of {cell_number} cells.")
        else:
            print(f"We have {number} single cells.")
                    
    print()