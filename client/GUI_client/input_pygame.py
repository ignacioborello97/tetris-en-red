import pygame as pg


class InputText:
    def __init__(self, x, y, width, height):
        self.font = pg.font.Font(None, 32)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.input_box = pg.Rect(
            self.x, self.y, self.x + self.width, self.y + self.height)
        self.color_inactive = pg.Color('lightskyblue3')
        self.color_active = pg.Color('dodgerblue2')
        self.color = pg.Color('dodgerblue2')
        self.active = False
        self.text = ''
        self.done = False

    def draw(self, screen):
        txt_surface = self.font.render(self.text, True, self.color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        self.input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (self.input_box.x+5, self.input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, self.color, self.input_box, 2)

    def capture_event(self, event):
        if event.type == pg.QUIT:
            self.done = True
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.input_box.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = self.color_active if self.active else self.color_inactive
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    self.emit_value()
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.emit_value()
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def emit_value(self):
        print('value : '+self.text)


if __name__ == '__main__':
    pg.init()
    screen = pg.display.set_mode((640, 480))
    screen.fill((0, 0, 0))
    input = InputText(100, 100, 200, 50)
    input1 = InputText(100, 100, 200, 50)
    input2 = InputText(100, 100, 200, 50)
    input3 = InputText(100, 100, 200, 50)
    input4 = InputText(100, 100, 200, 50)
    input5 = InputText(100, 100, 200, 50)
    input_list = [input, input1, input2, input3, input4, input5]
    while True:
        for event in pg.event.get():
            for input in input_list:
                input.capture_event(event)
        for input in input_list:
            input.draw(screen)

        pg.display.flip()
        # clock.tick(30)

    pg.quit()
