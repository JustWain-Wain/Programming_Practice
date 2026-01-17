class Canvas:
  """Класс коллекции фигур."""

  def __init__(self) -> None:
    """Инициализация экземпляра класса."""
    self.shapes = [] # коллекция фигур

  def AddShape(self, shape: object) -> None:
    """Добавляет фигуру в коллекцию."""
    self.shapes.append(shape)

  def RemoveShape(self, shape) -> None:
    """Удаляет фигуру из коллекции."""
    self.shapes.remove(shape)

  def MoveShape(self, shape, new_position: tuple) -> None:
    """Изменяет координаты фигуры."""
    shape_index = self.shapes.index(shape)
    self.shapes[shape_index].position = new_position

  def ChangeColor(self, shape, new_color: str) -> None:
    """Изменяет цвет фигуры."""
    shape_index = self.shapes.index(shape)
    self.shapes[shape_index].color = new_color


class Shape:
  """Родительский класс фигуры.

  Содержит базовые параметры и методы.
  """

  def __init__(self) -> None:
    """Инициализация экземпляра класса."""
    self.position = () # координаты фигуры
    self.color = None # цвет фигуры
    self.shape_type = None # тип фигуры

  def properties(self) -> list:
    """Возвращает список параметров фигуры, читаемый человеком."""
    return [self.shape_type, self.position, self.color]

  def draw(self) -> None:
    """Отрисовывает фигуру."""
    pass


class Circle(Shape):
  """Класс фигуры Круг.

  Содержит дополнительно радиус.
  """

  def __init__(self, position: tuple, color: str, radius: int) -> None:
    """Инициализация экземпляра класса."""
    self.position = (position[0],position[1])
    self.color = color
    self.radius = radius # радиус круга
    self.shape_type = "Circle"

  def properties(self) -> list:
    """Возвращает список параметров фигуры, читаемый человеком."""
    return [self.shape_type, self.position, self.color, self.radius]


class Rectangle(Shape):
  """Класс фигуры Прямоугольник.

  Содержит дополнительно высоту и ширину.
  """

  def __init__(self, position: tuple, color: str, height: int, width: int) -> None:
    """Инициализация экземпляра класса."""
    self.position = (position[0],position[1])
    self.color = color
    self.height = height # высота
    self.width = width # ширина
    self.shape_type = "Rectangle"

  def properties(self) -> list:
    """Возвращает список параметров фигуры, читаемый человеком."""
    return [self.shape_type, self.position, self.color, self.height, self.width]

class Line(Shape):
  """Класс фигуры Линия.

  Общая позиция включает в себя координаты начала и конца линии.
  """

  def __init__(self, start: tuple, end: tuple, color: str) -> None:
    """Инициализация экземпляра класса."""
    self.position = ((start[0], start[1]), (end[0], end[1]))
    self.color = color
    self.shape_type = "Line"

  def properties(self) -> list:
    """Возвращает список параметров фигуры, читаемый человеком."""
    return [self.shape_type, self.position, self.color]


class EditorHistory:
  """Класс истории изменения.

  Содержит стэки undo и redo для возможности откатить изменения.
  """

  def __init__(self, editor) -> None:
    """Инициализация экземпляра класса."""
    self.undo_stack = []
    self.redo_stack = []
    self.editor = editor # указываем редактор, к которому относится история

  def undo(self) -> None:
    """Функция отката изменения."""
    obj = self.undo_stack.pop(-1)
    # obj[0] - команда
    # obj[1] - объект фигуры
    # obj[2] - предыдущие координаты или предыдущий цвет
    match obj[0]:
      case "AddShape": # вызываем обратную функцию для отката
        self.editor.RemoveShape(obj[1])
      case "RemoveShape":
        self.editor.AddShape(obj[1])
      case "MoveShape":
        self.editor.MoveShape(obj[1], obj[2])
      case "ChangeColor":
        self.editor.ChangeColor(obj[1], obj[2])
    self.redo_stack.append(obj)

  def redo(self) -> None:
    """Функция возвращения отмененных изменений."""
    obj = self.redo_stack.pop(-1)
    # obj[0] - команда
    # obj[1] - объект фигуры
    # obj[3] - новые координаты или новый цвет
    match obj[0]:
      case "AddShape": # просто выполняем операцию повторно
        self.editor.AddShape(obj[1])
      case "RemoveShape":
        self.editor.RemoveShape(obj[1])
      case "MoveShape":
        self.editor.MoveShape(obj[1], obj[3])
      case "ChangeColor":
        self.editor.ChangeColor(obj[1], obj[3])
    self.undo_stack.append(obj)

  def append_history(self, action: tuple) -> None:
    """Добавление действия в историю изменений."""
    self.undo_stack.append(action)


class EditorCommand:
  """Класс редактора.

  Содержит в себе историю и холст с фигурами.
  """

  def __init__(self) -> None:
    """Инициализация экземпляра класса."""
    self.history = EditorHistory(self) # история
    self.canvas = Canvas() # холст

  def AddShape(self, shape) -> None:
    """Добавляет фигуру на холст. Требуется подтверждение."""
    agreement = input(f"Подтвердите добавление фигуры {shape.properties()} (y/n): ")
    if agreement == "y":
      self.canvas.AddShape(shape)
      self.history.append_history(("AddShape", shape))

  def RemoveShape(self, shape) -> None:
    """Удаляет фигуру с холста. Требуется подтверждение."""
    agreement = input(f"Подтвердите удаление фигуры {shape.properties()} (y/n): ")
    if agreement == "y":
      self.canvas.RemoveShape(shape)
      self.history.append_history(("RemoveShape", shape))

  def MoveShape(self, shape, new_position: tuple) -> None:
    """Изменяет координаты фигуры на холсте. Требуется подтверждение."""
    agreement = input(f"Подтвердите изменение координат фигуры {shape.properties()}"
                      f" c {shape.position} на {new_position} (y/n): ")
    if agreement == "y":
      prev_position = shape.position
      self.canvas.MoveShape(shape, new_position)
      self.history.append_history(("MoveShape", shape, prev_position, new_position))

  def ChangeColor(self, shape, new_color: str) -> None:
    """Изменяет цвет фигуры на холсте. Требуется подтверждение."""
    agreement = input(f"Подтвердите изменение цвета фигуры {shape.properties()}"
                      f" с {shape.color} на {new_color} (y/n): ")
    if agreement == "y":
      prev_color = shape.color
      self.canvas.ChangeColor(shape, new_color)
      self.history.append_history(("ChangeColor", shape, prev_color, new_color))

  def undo(self) -> None:
    """Отменяет последнее действие."""
    self.history.undo()

  def redo(self) -> None:
    """Отменяет последнее отменённое действие."""
    self.history.redo()

  def list_shapes(self) -> list:
    """Возвращает список фигур, подходящий для чтения человеку."""
    return [shape.properties() for shape in self.canvas.shapes]

# Тесты и демонстрация
editor = EditorCommand()
r = Rectangle((1, 5), "blue", 5, 15)
c = Circle((5, 2), "red", 7)
l = Line((5, 1), (10, 13), "green")
editor.AddShape(r)
editor.AddShape(c)
editor.AddShape(l)
print(editor.list_shapes())
editor.RemoveShape(l)
print(editor.list_shapes())
editor.undo()
print(editor.list_shapes())
editor.ChangeColor(r, "purple")
print(editor.list_shapes())
editor.redo()
print(editor.list_shapes())
