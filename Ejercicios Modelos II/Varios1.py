from tkinter import Tk,Label,Button,Frame

limite = input("Ingrese el tiempo limite de la siguiente forma HH:MM:SS : ")
 
proceso = 0
 
def iniciar(h=0, m=0, s=0):
    global proceso
 
    if s >= 60:
        s = 0
        m = m + 1
    if m >= 60:
        m = 0
        h = h + 1
    if h >= 24:
        h = 0
        
    time['text'] = str(h) + ":" + str(m) + ":" + str(s)
 
    # iniciamos la cuenta progresiva de los segundos
    proceso = time.after(1000, iniciar, (h), (m), (s+1))
 
def parar():
    global proceso
    time.after_cancel(proceso)
 
root = Tk()
root.title('Cronometro')
 
time = Label(root, fg='red', width=20, font=("","18"))
time.pack()
iniciar()
frame = Frame(root)
##btnIniciar = Button(frame, fg = 'blue', text = 'Iniciar', command = iniciar)
##btnIniciar.grid(row = 1, column = 1)
##btnParar = Button(frame, fg = 'blue', text = 'Parar', command = parar)
##btnParar.grid(row = 1, column = 2)
frame.pack()
 
root.mainloop()
