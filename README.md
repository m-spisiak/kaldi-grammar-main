
## Getting Started

1. `sudo apt install xdotool python3 python3-venv`
1. `git clone https://github.com/m-spisiak/kaldi-grammar-main.git && cd kaldi-grammar-main`
1. `python3 -m venv venv && source venv/bin/activate && \
     python -m pip install --upgrade pip setuptools wheel`
1. `python -m pip install 'dragonfly2[kaldi]' playsound`
TODO it needs active grammar maybe
1. `wget https://github.com/daanzu/kaldi-active-grammar/releases/download/v3.1.0/kaldi_model_daanzu_20211030-mediumlm.zip && unzip kaldi_model_*.zip`
1. `cp settings.py-example settings.py` 
1. `python kaldi_module_loader_plus.py`
