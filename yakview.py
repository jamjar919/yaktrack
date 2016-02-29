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
    while (i < len(yaks)) and (currentLine < sz.lines-9):
        yak = yaks[i];
        if (yak["type"] != 0):
            yakwindow.addstr(currentLine,1,str(yak["message"]+" [image]"));
        else:
            yakwindow.addstr(currentLine,1,yak["message"]);
        yakwindow.addstr(currentLine,sz.columns-6,str(math.floor(float(yak["score"]))));
        currentLine += 1;
        i += 1;
        yakwindow.refresh();

sz = os.get_terminal_size();
screen = curses.initscr();
curses.noecho(); 
curses.curs_set(0); 
screen.keypad(1);
yakwindow = curses.newwin(sz.lines-7,sz.columns-2,1,1);
yakwindow.border(0);
yakwindow.addstr("Yaks");

bottomwin = curses.newwin(5,sz.columns-2,sz.lines-6,1);
bottomwin.border(0)
bottomwin.addstr("Commands");
bottomwin.addstr(1,1,"q - Quit");
bottomwin.addstr(2,1,"h - Print Hot Yaks");
bottomwin.addstr(3,1,"n - Print New Yaks");
screen.refresh();
yakwindow.refresh();
bottomwin.refresh();
event = "n";
while True: 
    if event == ord("q"): break;
    elif event == ord("h"):
        yaks = yt.getHotYaks(yt.getYid(None));
        printYaks(yaks,yakwindow);
    elif event == ord("n"):
        yaks = yt.getNewYaks(yt.getYid(None));
        printYaks(yaks,yakwindow);
    event = screen.getch() 
    
curses.nocbreak();
screen.keypad(0);
curses.echo();
curses.endwin()