import curses;
import yaktrack as yt;
import os;
import math;

def printYaks(yaks,yakwindow):
    yakwindow.clear();
    yakwindow.border(0);
    sz = os.get_terminal_size();
    yakwindow.addstr(0,math.floor(sz.columns/2)-3,"Yaks");
    currentLine = 1;
    i = 0;
    yakSpace = sz.columns-11;
    while (i < len(yaks)) and (currentLine < sz.lines-9):
        yakLines = list();
        yak = yaks[i];
        if (yak["type"] != 0):
            yak["message"] = yak["message"]+ " [image]";
        n = 0;
        while (n < len(yak["message"])):
            if (n+yakSpace < len(yak["message"])):
                yakLines.append(yak["message"][n:n+yakSpace]);
            else:
                yakLines.append(yak["message"][n:len(yak["message"])]);
            n += yakSpace;
        yakwindow.addstr(currentLine,sz.columns-7,str(math.floor(float(yak["score"]))));
        for messageLine in yakLines:
            yakwindow.addstr(currentLine,2,messageLine);
            currentLine += 1;
        i += 1;
    printYakarma(yakwindow);

def printYakarma(yakwindow):
    sz = os.get_terminal_size();
    yakarma = yt.getYakarma();
    yakwindow.addstr(0,sz.columns-2-len("YK: "+str(yakarma)),"YK: "+str(yakarma));

sz = os.get_terminal_size();
screen = curses.initscr();
curses.noecho(); 
curses.curs_set(0); 
screen.keypad(1);
yakwindow = curses.newwin(sz.lines-7,sz.columns-2,1,1);
printYakarma(yakwindow);
yakwindow.border(0);
yakwindow.addstr(0,math.floor(sz.columns/2)-3,"Yaks");

bottomwin = curses.newwin(5,sz.columns-2,sz.lines-6,1);
bottomwin.border(0)
bottomwin.addstr("Commands");
bottomwin.addstr(1,1,"q - Quit");
bottomwin.addstr(2,1,"h - Print Hot Yaks");
bottomwin.addstr(3,1,"n - Print New Yaks");
yaks = yt.getNewYaks();
printYaks(yaks,yakwindow);
screen.refresh();
yakwindow.refresh();
bottomwin.refresh();
while True: 
    event = screen.getch() 
    if event == ord("q"): break;
    elif event == ord("h"):
        yaks = yt.getHotYaks();
        printYaks(yaks,yakwindow);
    elif event == ord("n"):
        yaks = yt.getNewYaks();
        printYaks(yaks,yakwindow);
    printYakarma(yakwindow);
    yakwindow.refresh();
    
curses.nocbreak();
screen.keypad(0);
curses.echo();
curses.endwin()
