
## Getting started - Installation on Linux

To install all dependencies, clone the repository and download the model (~600MB) copy the following into terminal:
```buildoutcfg
sudo apt install xdotool python3 python3-venv
git clone https://github.com/m-spisiak/voice-shortcuts.git && \
    cd voice-shortcuts
echo 'function voiceshortcuts {
    cd '$(pwd)'
    source venv/bin/activate
    python3 start_up.py
}
export voiceshortcuts' >> ~/.bashrc
source ~/.profile
python3 -m venv venv && source venv/bin/activate && \
    python -m pip install --upgrade pip setuptools wheel
python -m pip install kaldi-active-grammar 'dragonfly2[kaldi]' playsound
wget https://github.com/daanzu/kaldi-active-grammar/releases/download/v3.1.0/kaldi_model_daanzu_20211030-mediumlm.zip && \
    unzip kaldi_model_*.zip
cp settings.py-example settings.py
```

Then you run the program by:
`kaldistart`