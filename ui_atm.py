# -*- coding: utf-8 -*-
import Tkinter as tk
import sqlite3
from Tkinter import IntVar
from Tkinter import Tk
import tkMessageBox


def mainwindow(*args, **kwargs):
    con = sqlite3.connect('test.db')
    cur = con.cursor()
    con.commit()
    root = Tk()
    root.title("Internet Banking")

    def butCallback():
        value = int(text_entry.get())
        root.destroy()
        cur.execute("SELECT card_number FROM atm;")
        for i in cur.fetchall():
            for j in i:
                if value == j:
                    ok()
        else:
            error()

    def clear():
        text_entry.delete(0, tk.END)

    def control_type(event):
        """Проверяет вводимые данные"""
        data = text_entry.get()[0:18]
        if not data.isdigit() and data != '':
            text_entry["bg"] = "red"
            result = ''
            for i in data:
                if i.isdigit():
                    result += i
            text_entry.delete(0, tk.END)
            text_entry.insert(0, result)
            tkMessageBox.showerror(title="Ошибка", message="Неверный тип данных, ожидалось число")
        else:
            text_entry["bg"] = "white"
            result = []
            count = 0
            for i in data:
                count += 1
                result += i
                if count % 4 == 0:
                    result.append('-')
            a = ''.join(result)
            text_entry.delete(0, tk.END)
            text_entry.insert(0, a)

    #mainframe = tk.Frame(root)
    #mainframe.pack(side="top", fill="both", expand=True)
    #mainframe.columnconfigure(0, weight=1)
    #mainframe.rowconfigure(0, weight=1)

    int1 = IntVar()
    tk.Label(root, text="Enter your card number").pack(side=tk.TOP, fill="x")
    text_entry = tk.Entry(root, width=20)
    text_entry.bind("<Any-KeyRelease>", control_type)
    text_entry.pack(side=tk.LEFT)

    tk.Button(root, text="OK", command=butCallback).pack(side="left")
    tk.Button(root, text="Clear", command=clear).pack(side="left")

    root.mainloop()


def ok(*args, **kwargs):
    root = Tk()
    root.title('2')

    def butCallback():
        root.destroy()
        mainwindow()

    tk.Button(root, text="ok", command=butCallback).pack(side="left")
    root.mainloop()


def error():
    root = Tk()
    root.title('ERROR')
    tk.Label(root, text="Your card is blocked").pack(side=tk.TOP, fill="x")
    root.mainloop()


if __name__ == "__main__":
    mainwindow()