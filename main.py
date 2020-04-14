import numpy as np
import pyautogui
from PIL import ImageGrab
import keyboard
game = [635, 245, 1263, 873]
top_left_tile_center = [713, 323]
tile_length = 157
while True:
    if (pyautogui.position()[0] > 635):
        print("start")
        break
while True:
    mouse_pos = pyautogui.position()
    if (game[0] < mouse_pos.x < game[2] and game[1] < mouse_pos.y < game[3]):
        count = 0 
        screen = np.array(ImageGrab.grab(bbox=game).convert('LA'))
        
        for i in range(4):
            y = top_left_tile_center[1] + i * tile_length
            for j in range(4):
                x = top_left_tile_center[0] + j * tile_length
                # print(f'i: {i}, j: {j}, score: {screen[x-game[0]][y-game[1]][0]}')
                if ((screen[y-game[1]][x-game[0]][0])==0):
                    pyautogui.click(x=x,y=y)
    if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('You Pressed A Key!')
            break  # finishing the loop