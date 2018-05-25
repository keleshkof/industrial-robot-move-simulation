#!/usr/bin/python3

import random
import time
import os

turn = False
mal_c = 0
x_dim = 20
y_dim = 7
x_d = x_dim - 1
y_d = y_dim - 1
mallist = list(range(3))
zone = [[" " for x in range(x_dim)] for y in range(y_dim)]

def print_zone():
    for i in range(y_dim):
        for j in range(x_dim):
            print(zone[i][j],end=" ",flush=True)
        print()

def zona():
    for  i in range(x_dim):
        zone[0][i] = "M"
        zone[y_d][i] = "M"
    for i in range(1,y_d):
        zone[i][0] = "S"
        zone[i][x_d] = "D"
    zone[3][1] = "X"

def move(x,y):
    global turn
    global mal_c
    mvx = 0
    mvy = 0
    for i in range(y_dim):
        for j in range(x_dim):
            if(zone[i][j] == "X"):
                mvx = i
                mvy = j
    mvx += x
    mvy += y
    if(zone[mvx][mvy] == "D"):
        turn = True
    elif(zone[mvx][mvy] == "S"):
        turn = False
    elif(zone[mvx][mvy] == "M"):
        mal_c += 1
    if((mvx <= y_d-1 and mvx >= 1) and (mvy <= x_d-1 and mvy >= 1)):
        zone[mvx - x][mvy - y] = " "
        zone[mvx][mvy] = "X"

def robot_1():
    global turn
    rnd = random.randint(1,10)
    if(rnd == 1):
        move(-1,0)
    elif(rnd == 2):
        move(1,0)
    else:
        if(turn == False):
            move(0,1)
        else:
            move(0,-1)

def robot_2():
    global turn
    rnd = random.randint(1,100)
    for i in range(y_dim):
        for j in range(x_dim):
            if(zone[i][j] == "X"):
                row_num = i
    if(row_num == 3):
        if(rnd < 25 and rnd >=1):
            move(-1,0)
        elif(rnd < 50 and rnd >=25):
            move(1,0)
        else:
            if(turn == False):
                move(0,1)
            else:
                move(0,-1)
    else:
        if(row_num > 3):
            if(rnd > 50 and rnd <= 100):
                move(-1,0)
            elif(rnd > 10 and rnd <= 50):
                if(turn == False):
                    move(0,1)
                else:
                    move(0,-1)
            else:
                move(1,0)
        else:
            if(rnd > 50 and rnd <= 100):
                move(1,0)
            elif(rnd > 10 and rnd <= 50):
                if(turn == False):
                    move(0,1)
                else:
                    move(0,-1)
            else:
                move(-1,0)

def robot_3():
    global turn
    rnd = random.randint(1,100)
    for i in range(y_dim):
        for j in range(x_dim):
            if(zone[i][j] == "X"):
                row_num = i
    if(row_num == 3):
        if(rnd < 40 and rnd >=1):
            move(-1,0)
        elif(rnd < 80 and rnd >=40):
            move(1,0)
        else:
            if(turn == False):
                move(0,1)
            else:
                move(0,-1)
    elif(row_num == 2 or row_num == 4):
        rnd_2 = random.randint(1,3)
        if(rnd_2 == 1):
            move(-1,0)
        elif(rnd_2 == 2):
            if(turn == False):
                move(0,1)
            else:
                move(0,-1)
        else:
            move(1,0)
    else:
        if(row_num > 3):
            if(rnd > 30 and rnd <= 90):
                move(-1,0)
            elif(rnd > 1 and rnd <= 30):
                if(turn == False):
                    move(0,1)
                else:
                    move(0,-1)
            else:
                move(1,0)
        else:
            if(rnd > 30 and rnd <= 90):
                move(1,0)
            elif(rnd > 1 and rnd <= 30):
                if(turn == False):
                    move(0,1)
                else:
                    move(0,-1)
            else:
                move(-1,0)

def edit():
    global turn
    global zone
    turn = False
    for i in range(y_dim):
        for j in range(x_dim):
            if(zone[i][j] == "X"):

                zone[i][j] = " "
    zone[3][1] = "X"

def simulate():
    print("Simulating....")
    n = 500
    wait = 15
    global mal_c
    count = 0
    zona()
    for i in range(n):
        clear()
        print("--Robot 1--\nmove:",i,"\tmalfunction:",mal_c)
        print_zone()
        time.sleep(1/wait)
        robot_1()
    mallist[count] = mal_c
    mal_c = 0
    count+=1
    edit()
    for i in range(n):
        clear()
        print("--Robot 2--\nmove:",i,"\tmalfunction:",mal_c)
        print_zone()
        time.sleep(1/wait)
        robot_2()
    mallist[count] = mal_c
    mal_c = 0
    count+=1
    edit()
    for i in range(n):
        clear()
        print("--Robot 3--\nmove:",i,"\tmalfunction:",mal_c)
        print_zone()
        time.sleep(1/wait)
        robot_3()
    mallist[count] = mal_c
    mal_c = 0
    edit()
    print("\nSimulation complete...")
    print("------------------------------------------------")
    print("---->Robot1 malfuntion rate",str(mallist[0]/n)+"%.")
    print("---->Robot2 malfuntion rate",str(mallist[1]/n)+"%.")
    print("---->Robot3 malfuntion rate",str(mallist[2]/n)+"%.")
    print("------------------------------------------------")
    minm = 99999999
    index = 0
    for i in range(3):
        if(mallist[i] < minm):
            minm = mallist[i]
            index = i
    print("\nRobot"+str(index + 1)+" would has the least malfunctions.\n")

def clear():
    print(100*"\n")

def main():
    menu = """
                Robot Malfunction Analyser
                1-Simulate
                0-EXIT
           """
    while(True):
        clear()
        print(menu)
        choice = str(input("choice:"))
        if(choice == "1"):
            simulate()
            print("Press any key...")
            choice = str(input(""))
        elif(choice == "0"):
            break
        else:
            print("Wrong input")
            print("Press any key...")
            choice = str(input(""))
main()
