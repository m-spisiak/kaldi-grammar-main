
## Getting started - Installation on Linux

To install all dependencies, clone the repository and download the model (~600MB) copy the following into terminal:
```buildoutcfg
sudo apt install xdotool python3 python3-venv
git clone https://github.com/m-spisiak/voice-shortcuts.git && \
    cd voice-shortcuts
python3 -m venv venv && source venv/bin/activate && \
    python -m pip install --upgrade pip setuptools wheel
python -m pip install kaldi-active-grammar 'dragonfly2[kaldi]' playsound
wget https://github.com/daanzu/kaldi-active-grammar/releases/download/v3.1.0/kaldi_model_daanzu_20211030-mediumlm.zip && \
    unzip kaldi_model_*.zip
cp settings.py-example settings.py
echo 'function voiceshortcuts {
    cd '$(pwd)'
    source venv/bin/activate
    python3 start_up.py
}
export voiceshortcuts' >> ~/.bashrc
source ~/.profile
```

Then you run the program by (you might need to reopen new terminal for the changes to take place):
`voiceshortcuts`

## Basic voice commands to try
The most basic voice commands that are set up from the start are the following:

- "copy" (makes a sound when copied)
- "cut" / "snap" (the two do the same thing)
- "paste"
- "undo"
- "switch window"
- any number can be written by saying "number" and the number, i.e. "number five".
- basic special characters can be written by saying their name, i.e. "underscore".
- parentheses can be invoked by "parentheses", you get both left and right with the cursor ending up in the middle.
- single words recognized by the system can be written preceding them by saying word, i.e. "word fire" writes 'fire'
- full phrases can be dictated by preceding them with "phrase"

### Custom voice commands
A very useful feature of the voice control is to switch between windows by voice
or to bring up new applications with a voice command.

Since everyone calls their applications differently, the specific naming has to be custom.
These custom names are stored in `settings.py`.
For instance the simple command "firefox" will switch to the firefox window if it is open.

The system doesn't know about all of your favorite windows and thus it needs to be configured (see next section)

## Setting up new voice commands
The engine is set up to load commands from multiple sources.
One is in `keyboard.py` in a variable called `myMap` and the other source
is `settings.py` that is gitignored and can be configured as desired.

If you open `settings.py`, you immediately see a dictionary that on the left hand side has the command names,
the actual words you need to pronounce, and on the right there is the function that will be performed.
To switch between windows use `FocusWindow` and to open an application use `BringApp`.

To be able to set up a new command, you need to know the system's name of the application.
To find out a name of an application, open it, then start `voiceshortcuts` and say "list window executables".
That will display a list of names in the terminal where voice-shortcuts is running.
You find the exact name of your application there and put it into `settings.py` where you can call it whatever you wish
(on the left hand side.)

Other commands can be easily set up with the aid of key stroke emulation, just like the "copy" and "paste" commands that
are already set up. 
If you wish to set up your own command, have a look at `keyboard.py` for examples, inside the `grammarCfg` variable.
You can copy-paste those into your `settings.py` and have them working upon a restart of voice-shortcuts.

### Removing voice commands
It might be sometimes profitable to remove certain voice commands,
so that they don't clash with others that you frequently use.
You can do this simply by commenting out a line in either `keyboard.py` in a variable called `myMap`
or in your `settings.py` in the main dictionary.