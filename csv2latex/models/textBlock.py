class TextBlock:
    def __init__(self, style, page, text):
        self.style = style
        self.page = page
        self.text = text

        if self.style == "paragraph":
            self.child_elements = None
        else:
            self.child_elements = list()
