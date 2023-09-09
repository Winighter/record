import keyboard

running = True
counter = 0
not_pressed = True
while running:
    input = keyboard.read_key(suppress = True)
    if input== "esc":
        running = False
    else:
        if not_pressed:
            counter += 1
            print(input)
            not_pressed = False
        else:
            not_pressed = True