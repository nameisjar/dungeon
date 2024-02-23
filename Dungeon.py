import random
import tkinter as tk


window = tk.Tk()
window.title('Algo')
canvas = tk.Canvas(window, height=700, width=700)
canvas.pack()


def get_map(num1,num2):
    result = []
    idx = 0
    try:
        for x in range(num1):
            for y in range(num2):
                result.insert(idx,[x,y])
                idx += 1
            idx += 1
    except:
        print("Value Must Number")

    return result,num1,num2

CELLS,valx,valy = get_map(25,25)
type(CELLS)

def get_location():
    #random player
    #random door
    #random monster
    start = random.choice(CELLS)
    door = random.choice(CELLS)
    monster = random.choice(CELLS)

    if start == door or start == monster or monster == door:
        return get_location()

    return start,door,monster



        
def player_move(player,move):

    x, y = player

    if move == "LEFT":
        player[0] -= 1
    elif move == "RIGHT":
        player[0] += 1
    elif move == "UP":
        player[1] -= 1
    elif move == "DOWN":
        player[1] += 1
    canvas.create_oval(player[0]*30,player[1]*30,player[0]*30+30,player[1]*30+30,fill="blue")
    
def draw_map():
    for idx, cell in enumerate(CELLS): 
        canvas.create_rectangle(cell[0]*30,cell[1]*30,cell[0]*30+30,cell[1]*30+30,fill="gray")
        if cell == door:
            canvas.create_rectangle(cell[0]*30,cell[1]*30,cell[0]*30+30,cell[1]*30+30,fill="green")            

player,door,monster = get_location()
print("Welcome to the dungeon")

def moveMonster(monster):
    if(monster[0]<player[0]):
        monster[0] += 1
        return
    if(monster[0]>player[0]):
        monster[0] -= 1
        return
    if(monster[1]<player[1]):
        monster[1] += 1
        return
    if(monster[1]>player[1]):
        monster[1] -= 1
        return

tick = 0
def update():
    global tick
    canvas.create_oval(player[0]*30,player[1]*30,player[0]*30+30,player[1]*30+30,fill="blue")
    if tick == 2:
        moveMonster(monster)
        tick = 0
    tick += 1
    canvas.create_oval(monster[0]*30,monster[1]*30,monster[0]*30+30,monster[1]*30+30,fill="red")
    if player == monster:
        print("Ente kemakan monster gan ")
        window.destroy()
    elif player == door:
        print("Bisa kabur hebat ente gan ")
        window.destroy()
draw_map()
update()

def up(event):
    draw_map()
    player_move(player, "UP")
    update()

window.bind("<Up>",up)

def down(event):
    draw_map()
    player_move(player, "DOWN")
    update()

window.bind("<Down>",down)

def left(event):
    draw_map()
    player_move(player, "LEFT")
    update()

window.bind("<Left>",left)

def right(event):
    draw_map()
    player_move(player, "RIGHT")
    update()

window.bind("<Right>",right)

window.mainloop()