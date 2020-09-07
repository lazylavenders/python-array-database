"""
Stores data in arrays. A simple and fun project.

The Table() is the main class.
"""

class TableError(TypeError):...

class Table:
  """The main class."""
  def __init__(self, *columns):
    self.columns = columns
    self.data = {}
    
    for i in columns:
      seld.data[str(i)]=[]
    self.no_cols, self.no_rows = len(columns), 0
  
  
  def row_add(self, *columns) -> None:
    """Adds a row to the table."""
    
    if len(*columns) != self.no_cols:
      raise TableError(f"Wrong number of columns given, required : {self.cols} given : {columns}")
    for x,y in zip(self.columns, columns):
      self.data[x].append(y)
      
      
  def row_get(self, index) -> list:
    """Gets a row from a given index as a form of list.
    Index begins from one, negative values are for reverse indicing."""
    
    data = []
    for i in self.columns:
      data.append(self.data[i][index-1])
    return data

  
if __name__=='__main__':
  q = Table("Name","Age","GeniusLevel on a scale of one to ten")
  q.row_add("Knigt","Very young","Could be ten")
  q.row_add("Edmond","Old","Anything!")
  
  print(q.row_get(1),q.row_get(-1), sep="\n")
  quit()
  print(q.row_get(1))
