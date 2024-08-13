import turtle
import tkinter as tk
from tkinter import simpledialog

def desenhar_gato():
    turtle.reset()
    turtle.pendown()
    turtle.circle(50)  
    turtle.penup()
    turtle.goto(-15, 60)  
    turtle.pendown()
    turtle.goto(0, 100)
    turtle.goto(15, 60)
    turtle.penup()
    turtle.goto(-30, 40)  
    turtle.pendown()
    turtle.goto(-50, 100)
    turtle.goto(-65, 40)
    turtle.penup()
    turtle.goto(-25, 30)
    turtle.pendown()
    turtle.circle(5)
    turtle.penup()
    turtle.goto(25, 30)  
    turtle.pendown()
    turtle.circle(5)
    turtle.penup()
    turtle.goto(0, 10)  
    turtle.pendown()
    turtle.circle(3)

def desenhar_cachorro():
    turtle.reset()
    turtle.pendown()
    turtle.circle(50)  
    turtle.penup()
    turtle.goto(-20, 70)  
    turtle.pendown()
    turtle.circle(20)
    turtle.penup()
    turtle.goto(20, 70)  
    turtle.pendown()
    turtle.circle(20)
    turtle.penup()
    turtle.goto(-25, 30) 
    turtle.pendown()
    turtle.circle(5)
    turtle.penup()
    turtle.goto(25, 30)  
    turtle.pendown()
    turtle.circle(5)
    turtle.penup()
    turtle.goto(0, 10)  
    turtle.pendown()
    turtle.circle(3)

def desenhar_peixe():
    turtle.reset()
    turtle.pendown()
    turtle.circle(50)  
    turtle.penup()
    turtle.goto(-50, 0)  
    turtle.pendown()
    turtle.goto(-80, 20)
    turtle.goto(-80, -20)
    turtle.goto(-50, 0)
    turtle.penup()
    turtle.goto(-20, 10)  
    turtle.pendown()
    turtle.circle(5)

def executar_comando(comando):
    if comando.lower() == 'gato':
        desenhar_gato()
    elif comando.lower() == 'cachorro':
        desenhar_cachorro()
    elif comando.lower() == 'peixe':
        desenhar_peixe()
    else:
        print(f"Desenho não suportado para: {comando}")

def ler_comandos():
    comando = simpledialog.askstring("Comando", "Digite o nome do animal para desenhar:")
    if comando:
        executar_comando(comando)

root = tk.Tk()
root.title("Desenho de Animais com Turtle")
root.geometry("400x300")

btn_comando = tk.Button(root, text="Inserir Comando", command=ler_comandos)
btn_comando.pack(pady=20)

turtle_screen = turtle.Screen()
turtle_screen.setup(width=400, height=400)
turtle_screen.title("Turtle Drawing")

root.mainloop()
