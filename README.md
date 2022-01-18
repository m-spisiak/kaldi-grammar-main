
## Getting Started

```buildoutcfg
sudo apt install xdotool python3 python3-venv
git clone https://github.com/m-spisiak/kaldi-grammar-main.git && cd kaldi-grammar-main
python3 -m venv venv && source venv/bin/activate && \
     python -m pip install --upgrade pip setuptools wheel
python -m pip install kaldi-active-grammar 'dragonfly2[kaldi]' playsound
wget https://github.com/daanzu/kaldi-active-grammar/releases/download/v3.1.0/kaldi_model_daanzu_20211030-mediumlm.zip && unzip kaldi_model_*.zip
cp settings.py-example settings.py
python kaldi_module_loader_plus.py
```
