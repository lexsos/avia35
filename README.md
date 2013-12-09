avia35
======

avia35 web site


установка PIL
-------------

Для установки PIL сделать следующее:

sudo apt-get build-dep python-imaging
sudo apt-get install libjpeg62 libjpeg62-dev

32-bit version
sudo ln -s /usr/lib/i386-linux-gnu/libz.so /usr/lib/libz.so
sudo ln -s /usr/lib/i386-linux-gnu/libjpeg.so /usr/lib/libjpeg.so
sudo ln -s /usr/lib/i386-linux-gnu/libfreetype.so /usr/lib/libfreetype.so

64-bit version
sudo ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib/libz.so
sudo ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib/libjpeg.so
sudo ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib/libfreetype.so

pip install PIL
