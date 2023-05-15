class node:
  def __init__(self,data):
    self.data = data
    self.next_nodes = []

  def size(self):
    count = 1
    for node in self.next_nodes:
      count += node.size()
    return count

  def search(self,data):
    if self.data == data:
      return True
    else : 
      result = False
      for N in self.next_nodes:
        result = result or N.search(data)
      return result

class tree:
  def __init__(self, data):
    self.first_node = node(data)

  def size(self):
    return self.first_node.size()

  def search(self, data):
    return self.first_node.search(data)

class node :
  def __init__(self,data):
    self.data = data
    self.right_node = None
    self.left_node = None

  def append(self, data):
    if data == self.data:
      return
    if data > self.data:
      if self.right_node == None:
        self.right_node = node(data)
      else:
        self.right_node.append(data)
    else:
      if self.left_node == None:
        self.left_node = node(data)
      else:
        self.left_node.append(data)

    def search(self, data):
      if data == self.data:
        return True
      elif data < self.data:
        if self.left_node == None:
          return False
        else:
          self.left_node.search(data)
      else:
        if self.right_node == None:
          return False
        else:
          self.right_node.search(data)

class binary_tree:
  def __init__(self,data):
    self.first_node = node(data)

  def append(self, data):
    self.first_node.append(data)
