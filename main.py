import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

timer = None

reps = 0
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    window.after_cancel(timer)
    reps = 0
    timer_label.config(text= 'Timer', fg= GREEN)
    canvas.itemconfig(timer_text, text= "00:00")
    checkmark.config(text= '')
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    print(f"REPS: {reps}")
    if reps % 4 == 0:
        count_down(long_break_sec)
        timer_label.config(text= "BREAK", fg= GREEN)
        
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text= "BREAK", fg= PINK)
    else:
        count_down(work_sec)
        timer_label.config(text= "WORK", fg= RED)
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✓"
        
        checkmark.config(text= marks)
        
        
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# since the mainloop is event driven, keeps checking in the loop for an event
def count_down(count):
    minutes = math.floor(count/60) # returns largest whole number that's less than X
    seconds = count%60
    
    if seconds < 10:
        seconds = f'0{seconds}'
    
    
    canvas.itemconfig(timer_text, text= f"{minutes}:{seconds}")

    global timer
    if count>0:
        timer= window.after(1000, count_down, count-1)

    else:
        start()

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = tkinter.Canvas(width= 200, height= 224, bg=YELLOW, highlightthickness= 0)
tomato_img = tkinter.PhotoImage(file= 'tomato.png')
canvas.create_image(100, 112, image= tomato_img)
timer_text = canvas.create_text(100, 130, text= "00:00", fill= 'white', font= (FONT_NAME,35,'bold'))
canvas.grid(row= 2, column= 2)

timer_label = tkinter.Label(text= "Timer", fg= GREEN, font=(FONT_NAME,50,'bold'))
timer_label.grid(row= 1, column= 2)

start_button = tkinter.Button(text= 'Start', command= start)
start_button.grid(row= 3, column= 1)

stop_button = tkinter.Button(text= 'Reset', command= reset)
stop_button.grid(row= 3, column= 3)

checkmark = tkinter.Label(text= "", bg= YELLOW, fg=GREEN, font= (FONT_NAME, 20, 'bold'))
checkmark.grid(row= 5, column= 2)

window.mainloop()