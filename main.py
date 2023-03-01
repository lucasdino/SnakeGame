






#Function to render game window
def redrawWindow(surface):
    ...

#Function to draw snack
def randomSnack(rows, items):
    ...

#Function to display message box upon win / loss
def message_box(subject, content):
    ...


#Main function to run pygame
def main():
    width = 500
    height = 500
    rows = 20
    win = pygame.display.set_mode((width, height))

    s = snake((255,0,0), (10, 10))

    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)

        redrawWindow(win)