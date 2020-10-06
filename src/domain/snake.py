class Snake:
  def __init__(self, current_location, current_heading):
    self.current_location = current_location
    self.current_heading = current_heading

  def location(self):
    return self.current_location 

  def head(self):
    return 'N'
