from tkinter import *
from move import button_pressed, board, reset_board

root = Tk(screenName= 'Checkers')
root.title('Checkers')
root.iconbitmap(r'C:\Users\ezrab\python\checkers\images\chess_macos_bigsur_icon_190299.ico')
root.configure(background='black')

board_frame = LabelFrame(root, padx=5,pady=5, background='dark red')
board_frame.pack(padx=10, pady=10)

# setting up the player images
x_photo = PhotoImage(file=r'C:\Users\ezrab\python\checkers\images\X_player.png')
x_king_photo = PhotoImage(file=r'C:\Users\ezrab\python\checkers\images\X_king_player.png')
o_photo = PhotoImage(file=r'C:\Users\ezrab\python\checkers\images\O_player.png')
o_king_photo = PhotoImage(file=r'C:\Users\ezrab\python\checkers\images\O_king_player.png')



#creating the board
for y in range(8):
    z = []
    for x in range(8):
        x = Button(board_frame, command= lambda y=y, x=x: button_pressed(board[y][x],y,x))
        z.append(x)
    board.append(z)

for x in range(8):
    for y in range(8):
        board[x][y].grid(row=x, column=y)

for i in range(0,8,2):
    for u in range(0,8,2):
        board[u][i].config(background= 'black', activebackground='black')
        board[u][i+1].config(background= 'brown', state= 'disabled', width=9, height=4)
        board[u+1][i+1].config(background= 'black', activebackground='black')
        board[u+1][i].config(background= 'brown', state= 'disabled', width=9, height=4)


reset_board(x_photo,o_photo,x_king_photo,o_king_photo)


mainloop()