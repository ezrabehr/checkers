
from tkinter import PhotoImage, Tk, messagebox


first_push=False
board = []


def button_pressed(self, letter, number):
    global first_push, first_player_letter, first_player_number, first_player_image,first_player_button_id

    if first_push==False: #first push
        if self.cget('image')=='':
            pass
        else:
            first_player_letter = letter
            first_player_number = number
            first_player_image=self.cget('image')
            first_player_button_id=self


            first_push=True
    
    else: # second push
        if self.cget('image')!='':
            first_push=False
            button_pressed(self,letter,number)

        else: # if second push was empty

            # chose X
            if first_player_image == str(local_x_photo):

                # regular moving forward 
                if letter == first_player_letter-1 and (number == first_player_number+1 or number == first_player_number-1):
                    regular_move(self,letter)
                    first_push=False

                # eating move to the right (X)
                checking_eating_side(self, letter, number, first_player_letter-2,first_player_number+2,first_player_letter-1,first_player_number+1,local_o_photo,local_o_king_photo)
                # eating move to the left (X)
                checking_eating_side(self, letter, number, first_player_letter-2,first_player_number-2,first_player_letter-1,first_player_number-1,local_o_photo,local_o_king_photo)
            
            # chose O
            if first_player_image == str(local_o_photo):
                # regular moving forward
                if letter == first_player_letter+1 and (number == first_player_number+1 or number == first_player_number-1):
                    regular_move(self,letter)
                    first_push=False

                # eating move to the right (O)
                checking_eating_side(self, letter, number, first_player_letter+2,first_player_number+2,first_player_letter+1,first_player_number+1,local_x_photo,local_x_king_photo)
                # eating move to the left (O)
                checking_eating_side(self, letter, number, first_player_letter+2,first_player_number-2,first_player_letter+1,first_player_number-1,local_x_photo,local_x_king_photo)

            if str(first_player_image) == str(local_o_king_photo) or str(first_player_image) == str(local_x_king_photo):
                king_move(self,letter,number,first_player_image)


# checking that the move is legal
def checking_eating_side(self, letter, number, players_letter_to_be, player_number_to_be, letter_in_between, number_in_between, image, king_image):
    if letter == players_letter_to_be and number == player_number_to_be:

        if str(board[letter_in_between][number_in_between].cget('image'))==str(image) or str(board[letter_in_between][number_in_between].cget('image'))==str(king_image):
            
            eat_move(self,board[letter_in_between][number_in_between],letter)


# if you want to move the king
def king_move(self,letter,number,first_player_image):
    global first_push

    if (letter == first_player_letter-1 or letter == first_player_letter + 1) and (number == first_player_number+1 or number == first_player_number-1):
        regular_move(self,letter)
        first_push=False
    
    # differance for X and O
    if first_player_image == local_o_king_photo:
        eating_player= local_x_photo
        king_eating_player = local_o_king_photo
    else:
        eating_player= local_o_photo
        king_eating_player = local_x_king_photo

    checking_eating_side(self, letter, number, first_player_letter-2,first_player_number+2,first_player_letter-1,first_player_number+1,eating_player,king_eating_player)
    checking_eating_side(self, letter, number, first_player_letter-2,first_player_number-2,first_player_letter-1,first_player_number-1,eating_player,king_eating_player)
    checking_eating_side(self, letter, number, first_player_letter+2,first_player_number+2,first_player_letter+1,first_player_number+1,eating_player,king_eating_player)
    checking_eating_side(self, letter, number, first_player_letter+2,first_player_number-2,first_player_letter+1,first_player_number-1,eating_player,king_eating_player)
                

# classic move forward
def regular_move(self,letter):
    global first_player_button_id, first_player_number, first_player_letter

    self.config(image=first_player_image, width=65, height=65 )
    first_player_button_id.config(image= '', width=9, height=4 )
    reaching_end(self,letter)
    end_game()


# if you want to eat a player
def eat_move(self, player_to_eat,letter):
    global first_player_button_id, first_player_number, first_player_letter, x_counter, o_counter
    # to check winner
    if str(player_to_eat.cget('image'))== str(local_x_photo) or str(player_to_eat.cget('image'))==str(local_x_king_photo):
        x_counter = x_counter - 1
    if str(player_to_eat.cget('image'))== str(local_o_photo) or str(player_to_eat.cget('image'))==str(local_o_king_photo):
        o_counter = o_counter - 1

    player_to_eat.config(image='', width=9, height=4)
    self.config(image=first_player_image, width=65, height=65)
    first_player_button_id.config(image='', width=9, height=4)
    reaching_end(self,letter)
    first_player_number = first_player_letter = -1
    end_game()


# checks if the player made it to the end and then changing the image
def reaching_end(self,letter):
    # for O
    if str(self.cget('image'))==str(local_o_photo):
        if letter == 7:
            self.config(image=local_o_king_photo, width=65, height=65)

    # for X
    if str(self.cget('image'))==str(local_x_photo):
        if letter == 0:
            self.config(image=local_x_king_photo, width=65, height=65)
            
    
# checks for end game
def end_game():
    restart = ''
    if x_counter == 0:
        restart = messagebox.askyesnocancel('WINNER!','Cyan won!\nWould you like to restart the game?')
    if o_counter == 0:
        restart = messagebox.askyesnocancel('WINNER!','Purple won!\nWould you like to restart the game?')
    
    if restart == True:
        reset_board(local_x_photo,local_o_photo,local_x_king_photo,local_o_king_photo)
    elif restart == False:
        exit()

    

# reset the board
def reset_board(x_photo,o_photo,x_king_photo,o_king_photo):
    global x_counter,o_counter, local_x_photo, local_o_photo,local_o_king_photo,local_x_king_photo

    local_x_photo = x_photo
    local_o_photo= o_photo
    local_x_king_photo = x_king_photo
    local_o_king_photo = o_king_photo
    x_counter = o_counter = 12

    for x in range(3):
        for y in range(8):
            if board[x][y].cget('background')=='black':
                board[x][y].config(image= local_o_photo, width=65, height=65)

    for x in range(5,8):
        for y in range(8):
            if board[x][y].cget('background')=='black':
                board[x][y].config(image= local_x_photo, width=65, height=65)
    
    for x in range(3,5):
        for y in range(8):
            if board[x][y].cget('background')=='black':
                board[x][y].config(image='', width=9, height=4)

        
    
