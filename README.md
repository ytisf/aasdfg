# aasdfg

This project is meant to assist in creating a truly random, en-masse, random seed. 

The name of the project is a play on the meaning of randomness. 

The logic behind it is that at times, it is desireable to provide a truly random seed to a CSPRNG. However, is many cases, the seed used to generate the random seed is not truly random. This project aims to provide a way to generate a truly random seed, en-masse. Some solutions were attempted using mouse movements, temperature, datetime, keyboard and screen size. Some of these solutions are adequet, some are not, but it seems like generating a truly large seed (rules out user input, for example) and truly secure (rules out datetime, etc) has been an challenge.

This small script aims at capturing several photos from a camera, and then using the image data to generate a truly random seed. The script is written in Python, and uses the OpenCV library to capture images from a camera. The script then uses the image data to generate a truly random seed. It will then XOR least significant bits of the image data for all channels (giving more significance to noise and other almost impossible to predict artifacts) and then "fold" the data with additional XOR to derrive at a large seed. 

Our tests persistently show over 0.99999 factors on the Shannon Entropy scale, which is a very high level of entropy.

## Measurements

|Folds|Snaps|Size|Entropy
|:---:|:---:|:---:|:---:|
|2|1|86400|0.9999999803778411|
|4|1|21600|0.9999944340397522|
|8|1|1350|0.9999679398727177|
|2|2|86400|0.999999883311868|
|4|2|21600|0.9999910697190608|
|8|2|1350|0.999980605658771|
|2|4|86400|0.9999997461922827|
|4|4|21600|0.9999994564498254|
|8|4|1350|0.9999661340026522|

## Usage & Installation

Installation:
```bash
cd /tmp
git clone https://www.github.com/ytisf/aasdfg
cd aasdfg
python3 setup.py install
cd ..
rm -rf aasdfg
```

Usage: (will require webcam access!)
```python
from aasdfg import GenerateSeed

seed = GenerateSeed()
```



