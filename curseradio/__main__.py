from .curseradio import OPMLBrowser
import curses

def main():
    curses.wrapper(OPMLBrowser)

if __name__ == '__main__':
    main()
