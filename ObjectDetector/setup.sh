pip3 install -r requirements.txt
gdown https://drive.google.com/uc?id=1xWxqQGDH_szfCe8eWDBwTcjzCmq7Bnf1
unzip snapshot930.ckpt.zip
mkdir detection_compound_figure/checkpoints
mv snapshot930.ckpt detection_compound_figure/checkpoints
