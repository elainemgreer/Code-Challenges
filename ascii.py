class Canvas(object):

  def __init__(self, max_num):
    max_num = max_num
    self.container = []

  def render(self, max_num):
    # add shape
    # calculate height and width of shape
    # get starting coordinates of shape upper left
    # move right from upper left by width with character specificed
    # move down from upper left by heigth with character specificed
    # move down from upper right by height specificed
    # move right from lower left by width with character specified 
    
    for i in range(max_num):
      self.container.append([])
      for j in range(max_num):
        self.container[i].append(' ')

    for lst in self.container:
      print(lst)


  def add_shape(self, max_num, shape):
     # add shape
    # calculate height and width of shape
    # get starting coordinates of shape upper left
    # move right from upper left by width with character specificed
    # move down from upper left by heigth with character specificed
    # move down from upper right by height specificed
    # move right from lower left by width with character specified 
    for i in range(max_num):
      self.container.append([])
      for j in range(max_num):
        self.container[i].append(' ')
    
    length = shape.end_x - shape.start_x
    height = shape.end_y - shape.start_y
   
    for i in range(length):
        self.container[shape.start_x][shape.start_x + i] = shape.fill_char
        # self.container[shape.start_y][shape.start_x] = "1"
    for i in range(length):
        self.container[shape.end_x][shape.start_y + i] = shape.fill_char

    for i in range(height):
       self.container[shape.start_x + i][shape.start_y] = shape.fill_char

    for i in range(height):
       self.container[shape.start_y + i][shape.end_y] = shape.fill_char

    self.container[shape.end_y][shape.end_x] = shape.fill_char

   

    for lst in self.container:
      print(lst)



  def clear(self, max_num):
    # reprint canvas with nothing on it

    for i in range(max_num):
      self.container.append([])
      for j in range(max_num):
        self.container[i].append(' ')



class Rectangle(object):

  def __init__(self, start_x, start_y, end_x, end_y, fill_char):
    self.start_x = start_x
    self.start_y = start_y
    self.end_x = end_x
    self.end_y = end_y
    self.fill_char = fill_char

  def change_fill_char(self, fill_char):
    # change fill character

    self.fill_char = fill_char




