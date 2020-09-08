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
      self.data[str(i)]=[]
    self.no_cols, self.no_rows = len(columns), 0
  
  
  def row_add(self, *columns) -> None:
    """Adds a row to the table."""
    
    if len(columns) != self.no_cols:
      raise TableError(f"Wrong number of columns given, required : {self.cols} given : {columns}")
    for x,y in zip(self.columns, columns):
      self.data[x].append(y)
    self.no_rows += 1
      
      
  def row_get(self, index) -> list:
    """Gets a row from a given index as a form of list.
    Index begins from one, negative values are for reverse indicing."""
    
    data = []
    for i in self.columns:
      data.append(self.data[i][index-1])
    return data
  
  def row_remove(self, index):
    """Removes a row from the table of the given index beginning from one.
    Returns self."""
    for i in self.columns:
      self.data[i].remove(index-1)
    return self

  
if __name__=='__main__':
  q = Table("Name","Age","GeniusLevel on a scale of one to ten")
  q.row_add("Knigt","Very young","Could be ten")
  q.row_add("Edmond","Old","Anything!")
  
  print(q.row_get(1),q.row_get(-1), sep="\n")
  quit()
  print(q.row_get(1))
