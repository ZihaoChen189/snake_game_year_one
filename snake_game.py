import os
from tkinter import *
import random
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askinteger
#1366*768

def login_():
    current_path = os.path.abspath(os.path.dirname(__file__))
    # 设置登录窗口
    win = Tk()
    win.title('Login')

    sw = win.winfo_screenwidth()
    #得到屏幕宽度
    sh = win.winfo_screenheight()
    #得到屏幕高度

    ww = 380
    wh = 280

    #窗口宽高为100

    x = (sw-ww) / 2
    y = (sh-wh) / 2

    win.geometry("%dx%d+%d+%d" %(ww,wh,x,y-15))
    win.resizable(0, 0)

    Label(text='Name:').place(x=80, y=110)
    uname = Entry(win)
    uname.place(x=145, y=110)

    Label(text='Password:').place(x=80, y=150)
    pwd = Entry(win, show='*')
    pwd.place(x=145, y=150)
    with open('user.txt', 'r', encoding='utf-8') as f:
        data = eval(f.read())


    photo = PhotoImage(file="img.png")
    imgLabel = Label(win, image=photo)  # 把图片整合到标签类中
    imgLabel.place(x=10, y=0)


    def login():
        username = uname.get()
        password = pwd.get()
        if username in data:
            if password == data.get(username):
                with open('login.txt', 'w', encoding='utf-8') as f:
                    f.write(username)
                win.destroy()
                run_game()

            else:
                showinfo(title="Tips",
                         message="Please check your password or name")

        else:
            showinfo(title="Tips",message='You haven‘t registered an account，please click the Sign in.')

    # 登陆按钮
    Button(text='Login', command=login).place(x=100, y=200)

    def register():
        win.destroy()
        register_win()

    Button(text='Sign in', command=register).place(x=250, y=200)
    win.mainloop()


def register_win():
    # 设置登录窗口
    win = Tk()
    win.title('register')
    sw = win.winfo_screenwidth()
    # 得到屏幕宽度
    sh = win.winfo_screenheight()
    # 得到屏幕高度

    ww = 380
    wh = 280

    # 窗口宽高为100

    x = (sw - ww) / 2
    y = (sh - wh) / 2

    win.geometry("%dx%d+%d+%d" % (ww, wh, x, y - 15))
    win.resizable(0, 0)
    # 设置账号
    Label(text='name:').place(x=90, y=60)
    uname = Entry(win)
    uname.place(x=150, y=60)
    # 设置密码
    Label(text='password:').place(x=80, y=100)
    pwd1 = Entry(win, show='*')
    pwd1.place(x=150, y=100)
    # 确认密码
    Label(text='comfirm:').place(x=85, y=150)
    pwd2 = Entry(win, show='*')
    pwd2.place(x=150, y=150)

    with open('user.txt', 'r', encoding='utf-8') as f:
        data = f.read()

    def register():
        username = uname.get()
        password1 = pwd1.get()
        password2 = pwd2.get()
        if username in data:
            showinfo(title='tips', message='The name have been registered!')
        else:
            if password1 == password2:
                data1 = eval(data)
                data1[username] = password1
                with open('user.txt', 'w', encoding='utf8') as f1:
                    f1.write(str(data1))
                showinfo(title='tips', message='Register successfully!')
                win.destroy()
                login_()
            else:
                showinfo(title='tips', message='please check input!')

    Button(text='Register', command=register).place(x=150, y=200)

    def cancel_():
        win.destroy()


    # 登陆按钮
    Button(text='Cancel', command=cancel_).place(x=250, y=200)

    win.mainloop()


def show_rank_win():
    root = Tk()
    root.title('rank')
    theLB = Listbox(root, width=30, height=20)

    theLB.pack()

    item_list = []
    with open('history.txt', 'r', encoding='utf8') as f:
        score_ids = f.read()
    score_id_list = score_ids.split(' ')[:-1]
    id_score_dict = {}
    print(score_id_list[:-1])
    for index, score_id in enumerate(score_id_list):
        id_score_dict[score_id.split('-')[0]] = int(score_id.split('-')[1])
    new_dict = sorted(id_score_dict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    for id, score in new_dict:
        item_list.append('   ID:' + id + '                 SCORE:' + str(score))
    theLB.insert(0, '                     Rank\n\n\n')
    for item in item_list:
        theLB.insert(END, item)  # END表示每插入一个都是在最后一个位置

    def close_win():
        root.destroy()

    theButton = Button(root, text='Close', \
                       command=close_win)
    theButton.pack()

    mainloop()
PAUSE_ = False

class SnakeGame:
    def __init__(self):


        # moving step for snake & food that means the block size of food & snake
        self.step = 10

        # game score
        self.lengeth = 1

        with open('login.txt', 'r', encoding='utf-8') as f:
            self.user_name = f.read()
        his_score = self.get_history_score(self.user_name)
        if his_score == None:
            self.gamescore = 0
        else:
            self.gamescore = int(his_score)


        # to initialize the snake in the range of (x1,y1,x2,y1)                
        r = random.randrange(500, 500 + 15 * 10, self.step)
        self.snakeX = [r, r + self.step*2, r + self.step * 4]
        self.snakeY = [r, r, r]

        # to initialize the moving direction
        self.snakeDirection = 'left'
        self.snakeMove = [-1, 0]
        # to draw the game frame 
        self.window = Tk()
        self.window.geometry()
        self.screen_x = 1366
        self.screen_y = 768
        self.window.maxsize(self.screen_x, self.screen_y)
        self.window.minsize(self.screen_x,self.screen_y)
        self.window.title("Snake game")

        self.frame1 = Frame(self.window, bg="white", relief=GROOVE, borderwidth=5)
        self.frame2 = Frame(self.window, bg="white", relief=RAISED, borderwidth=2, height=40, width=600)
        self.canvas = Canvas(self.frame1, bg='green', width=self.screen_x, height=self.screen_y-100)
        self.score_label = Label(self.frame2, text='User: '+self.user_name+"         Score: 0"+'           (1920*1080)',
                                 fg="red", font=("Arial", 16, "bold", "italic"))

        self.cheat_label = Label(self.window, text="(Please input 'c' to cheat!)",
                                 fg="red", font=("Arial", 16, "bold", "italic"))

        # self.cheat_label.place(x=1450, y=1000)
        self.cheat_label.place(x=self.screen_x-350, y=self.screen_y-40)


        self.introduction = Label(
            self.window, text="(w:up a:Left d:Right s:down)",fg="red", font=("Arial", 16, "bold", "italic"))

        self.introduction.place(x=10, y=self.screen_y-40)



        self.action = Button(self.window, text="Pause", command=self.pause_game, font=("Arial", 16, "bold", "italic"))
        self.action.place(x=400, y=720)
        self.btn_close = Button(self.window, text="Logout", command=self.exit_game, font=("Arial", 16, "bold", "italic"))
        self.btn_close.place(x=900, y=720)
        self.btn_rank = Button(self.window, text="leader board", command=self.open_rank, font=("Arial", 16, "bold", "italic"))
        self.btn_rank.place(x=600, y=720)

        self.frame1.pack()
        self.frame2.pack(fill=BOTH)
        self.score_label.pack(side=BOTTOM)
        self.canvas.pack(fill=BOTH)
        # self.canvas.place(x=100,y=200)

        self.draw_wall()
        self.draw_score()
        self.draw_food()
        self.draw_snake()

        self.play()


        self.window.mainloop()

    def get_history_score(self, login_name):
        with open('history.txt', 'r', encoding='utf-8') as f:
            users = f.read().split(' ')
        for index, user in enumerate(users[::-1]):
            name = user.split('-')[0]
            if name == login_name:
                return user.split('-')[1]

    def open_rank(self):
        show_rank_win()


    def pause_game(self):
        global PAUSE_
        if self.action["text"] == "continue":
            PAUSE_ = False
            self.action["text"] = "Pause"
            self.play()

        else:
            PAUSE_ = True
            print('pause')
            self.action["text"] = "continue"

    def exit_game(self):
        with open('history.txt', 'a+', encoding='utf-8') as f:
            f.write(self.user_name+'-'+str(self.gamescore-10)+' ')
        current_path = os.path.abspath(os.path.dirname(__file__))
        register_path = os.path.join(current_path, 'login.py')
        self.window.destroy()
        os.system('python ' + register_path)





    "=== View Part ==="
    def draw_wall(self):

        self.canvas.create_line(10, 10, self.screen_x-10, 10, fill='blue', width=10)
        self.canvas.create_line(10, self.screen_y-100, self.screen_x-10, self.screen_y-100, fill='blue', width=10)
        self.canvas.create_line(10, 8, 10, self.screen_y-10, fill='blue', width=10)
        self.canvas.create_line(self.screen_x-10, 8, self.screen_x-10, self.screen_y-100, fill='blue', width=10)

    def draw_score(self):
        self.score_label.config(self.score_label, text='User: '+self.user_name+"         Score: " +
                                                       str(self.gamescore)+'           (1366*768)')
        self.score()

    def draw_food(self):
        self.canvas.delete("food")

        self.foodx, self.foody = self.random_food()

        self.canvas.create_rectangle(self.foodx, self.foody, \
                                     self.foodx + self.step, self.foody + self.step, fill='red', tags='food')

    def draw_snake(self):

        self.canvas.delete("snake")

        x, y = self.snake()

        for i in range(len(x)):
            #line
            self.canvas.create_rectangle(x[i], y[i], x[i] + self.step, y[i] + self.step, \
                                         fill='orange', tags='snake')


    "=== Model Part ==="

    def random_food(self):
        return (random.randrange(50, 1200, self.step), random.randrange(50, 600, self.step))

    def snake(self):
        for i in range(len(self.snakeX) - 1, 0, -1):
            self.snakeX[i] = self.snakeX[i - 1]
            self.snakeY[i] = self.snakeY[i - 1]
        self.snakeX[0] += self.snakeMove[0] * self.step
        self.snakeY[0] += self.snakeMove[1] * self.step
        return (self.snakeX, self.snakeY)

    def score(self):
        self.gamescore += 10

    "=== Control Part ==="

    def iseated(self):

        x_ = self.snakeX[0]-self.foodx
        y_ = self.snakeY[0]-self.foody
        if abs(x_)<=10 and abs(y_) <=10:
            print(x_)
            print(y_)
            return True
        # if self.snakeX[0] == self.foodx and self.snakeY[0] == self.foody:
        #     return True
        else:
            return False

    def isdead(self):
        if self.snakeX[0] < 8 or self.snakeX[0] > 1280 or \
                        self.snakeY[0] < 8 or self.snakeY[0] > 640:
              return True

        for i in range(1, len(self.snakeX)):
            if self.snakeX[0] == self.snakeX[i] and self.snakeY[0] == self.snakeY[i]:
                return True
        else:
            return False

    def move(self, event):

        if event.char == 'd' and self.snakeDirection != 'left':
            self.snakeMove = [self.lengeth, 0]
            self.snakeDirection = "right"
        elif event.char == 'w' and self.snakeDirection != 'down':
            self.snakeMove = [0, -self.lengeth]
            self.snakeDirection = "up"
        elif event.char == 'a' and self.snakeDirection != 'right':
            self.snakeMove = [-self.lengeth, 0]
            self.snakeDirection = "left"
        elif event.char == 's' and self.snakeDirection != 'up':
            self.snakeMove = [0, self.lengeth]
            self.snakeDirection = "down"
        elif event.char == 'c':
            step_ = askinteger(title="Cheat Code",
                                 prompt="Click c during the game，and then input 5 ，don‘t tell anyone！！！")
            self.step = step_*10
            self.restart(event)
        elif event.char == 'q':
            self.step = 10
            showinfo(title="Tips",
                     message="Cheating will be restored!")
            self.restart(event)

        else:
            print(event.keycode)

    def play(self):
        self.canvas.bind('<Key>', self.move)
        self.canvas.focus_set()

        while True:
            if self.isdead():
                self.gameover()
                break
            elif self.iseated():
                self.snakeX[0] += self.snakeMove[0] * self.step
                self.snakeY[0] += self.snakeMove[1] * self.step
                self.snakeX.insert(1, self.foodx)
                self.snakeY.insert(1, self.foody)

                self.draw_score()
                self.draw_food()
                self.draw_snake()
            elif PAUSE_ == True:
                break
            else:
                self.draw_snake()
                self.canvas.after(200)
                self.canvas.update()

    def gameover(self):
        self.canvas.unbind('<Key>')
        print('res:'+str(self.gamescore))
        self.canvas.bind("<Key>", self.restart)
        self.canvas.create_text(700, 350, text="Name:"+self.user_name+"   Your Current Score:"+str(self.gamescore-10)+"\n                   Game Over!\n \
        Press any key to continue", font='Helvetica -60 bold', tags='text')

    def restart(self, event):
        self.canvas.delete("food", "snake", "text")
        self.canvas.unbind('<Key>')

        # to initialize the snake in the range of (191,191,341,341)                
        r = random.randrange(500, 500 + 15 * 10, self.step)
        self.snakeX = [r, r + self.step, r + self.step * 2]
        self.snakeY = [r, r, r]

        # to initialize the moving direction
        self.snakeDirection = 'left'
        self.snakeMove = [-1, 0]

        # reset the score to zero 
        self.gamescore = 0
        self.draw_score()

        # to initialize the game (food and snake)
        self.draw_food()
        self.draw_snake()

        # to play the game
        self.play()

def run_game():
    SnakeGame()

if __name__ == '__main__':
    login_()

