# Terminal time
It's terminal time!

For when you don't know what time it is and you're near-sighted like me.
As a bonus, this script does not use ~30% of my CPU while idling like some of the existing solutions I was able to find on pip do.

Only tested with Python 3.7, but should work in Python <= 3.5 since that's when type hints were added.
I personally use this by adding it as a bash alias:

    alias clock="py ~/tools/terminal_time/clock.py"

## Usage

    usage: clock.py [-h] [-l] [-s] [-f FILENAME]

    What time is it? I'm near-sighted.

    optional arguments:
    -h, --help            show this help message and exit
    -l, --loop            The clock "takes over" the terminal it's in, instead
                            of printing the current time and exiting
    -s, --seconds         Show seconds. By default time is shown as HH:MM,
                            adding this flag changes format to HH:MM:SS
    -f FILENAME, --filename FILENAME
                            File to load the font from. Default uses the bundled
                            font file

The argument -l/--loop can be passed to have the clock clear the terminal it's called in and stay there, refreshing every few seconds.
Shrink your terminal and pin it with your window manager of choice to always have this nice, big clock visible without squinting, because vision tests and glasses are expensive but this little script is free.

The argument -s/--seconds can be passed to show HH:MM:SS instead of the default HH:MM.
Using both -l and -s at the same time is not recommended as there is a noticeable flicker or blink whenever the clock updates, and when -ls is passed this happens once per second.

### Example output
    jakob in ~: clock
        ██      ██          ██████  ██████
        ██      ██    ██    ██  ██  ██  ██
        ██      ██          ██  ██  ██████
        ██      ██    ██    ██  ██      ██
        ██      ██          ██████  ██████

## Customizability
Make a copy of the *font* file, and edit away!
Open the new *font* file in your text editor of choice, and you can change the symbols that are used to display the time.
The *font* file contains the digits 0-9 and a separator, which is : by default.
All symbols in *font* should be of equal height, and all lines within a symbol should be of the same length.

When you're happy with your font, pass -f <*your_font_file*> when running clock.py to use it!