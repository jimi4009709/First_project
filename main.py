import os
import time
import pyfiglet
from random import choice

# Rang sozlamalari
YASHIL = "\033[92m"
DEFAULT = "\033[0m"

# ASCII banner
def ascii_xush_kelibsiz():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = pyfiglet.figlet_format("Welcome to Tic Tac Toe")
    print(YASHIL + banner + DEFAULT)
    time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')

# Tic Tac Toe logikasi
def doska_yarat():
    return [[" " for _ in range(3)] for _ in range(3)]

def doskani_chiqar(doska):
    print()
    for qator in doska:
        print(" | ".join(qator))
        print("-" * 9)
    print()

def foydalanuvchi_kirit(doska):
    while True:
        try:
            raqam = int(input("Sizning yurishingiz (1-9): "))
            if raqam < 1 or raqam > 9:
                print("Faqat 1 dan 9 gacha bo'lgan raqam!")
                continue
            qator = (raqam - 1) // 3
            ustun = (raqam - 1) % 3
            if doska[qator][ustun] != " ":
                print("Bu joy band! Yana urining.")
            else:
                doska[qator][ustun] = "O"
                break
        except ValueError:
            print("Faqat raqam kiriting.")

def kompyuter_yuradi(doska):
    bosh_joylar = [(i, j) for i in range(3) for j in range(3) if doska[i][j] == " "]
    i, j = choice(bosh_joylar)
    doska[i][j] = "X"
    print("\nKompyuter yurdi.\n")

def golibni_tekshir(doska, belgi):
    for i in range(3):
        if all([doska[i][j] == belgi for j in range(3)]): return True
        if all([doska[j][i] == belgi for j in range(3)]): return True
    if all([doska[i][i] == belgi for i in range(3)]): return True
    if all([doska[i][2 - i] == belgi for i in range(3)]): return True
    return False

def durrangmi(doska):
    return all(doska[i][j] != " " for i in range(3) for j in range(3))

def oyin():
    ascii_xush_kelibsiz()
    doska = doska_yarat()
    while True:
        doskani_chiqar(doska)
        foydalanuvchi_kirit(doska)
        if golibni_tekshir(doska, "O"):
            doskani_chiqar(doska)
            print("🎉 Siz yutdingiz!")
            break
        if durrangmi(doska):
            doskani_chiqar(doska)
            print("🤝 Durrang!")
            break
        kompyuter_yuradi(doska)
        if golibni_tekshir(doska, "X"):
            doskani_chiqar(doska)
            print("💻 Kompyuter yutdi!")
            break
        if durrangmi(doska):
            doskani_chiqar(doska)
            print("🤝 Durrang!")
            break

oyin()
