class Grid2D:
    def __init__(self, grid):
        self.grid = grid

    def __getitem__(self, key):
        assert isinstance(key, tuple), "grid should be index with a tuple"

        row_key, col_key = key
        rows = self.grid[row_key]

        if isinstance(row_key, int):
            return rows[col_key]

        cols = [row[col_key] for row in rows]
        return cols

    def size(self):
        return len(self.grid), len(self.grid[0])

    def find_all(self, key):
        indices = []
        for r_index, row in enumerate(self.grid):
            for c_index, elem in enumerate(row):
                if elem == key:
                    indices.append((r_index, c_index))
        return indices