class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"zaousk otrisovki {self.title}"


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"risuem {self.title}"


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"{self.title} - zlenii"


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"{self.title} krasivo pishet"


pen = Pen("pen")
pencil = Pencil("pencil")
handle = Handle("handle")
print(pen.draw())
print(pencil.draw())
print(handle.draw())
