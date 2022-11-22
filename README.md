# aasdfg

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=round)](https://github.com/ytisf/aasdfg/issues)

![Logo](https://github.com/ytisf/aasdfg/raw/main/logo.png)

This project is meant to assist in creating a truly random, en-masse, cryptographically secure seed. 

The name of the project is a play on the meaning of randomness. 

The logic behind it is that at times, it is desireable to provide a truly random seed to a CSPRNG. However, is many cases, the seed used to generate the random seed is not truly random. This project aims to provide a way to generate a truly random seed, en-masse. Some solutions were attempted using mouse movements, components' temperature, [datetime](https://pynative.com/python-random-seed/), [keyboard](https://www.redhat.com/sysadmin/creating-gpg-keypairs) and screen size. Some of these solutions are adequet, some are not, but it seems like generating a truly large seed (rules out user input, for example) and truly secure (rules out datetime, etc) has been an challenge.

This small script aims at capturing several photos from a camera, and then using the image data to generate a truly random seed. The script is written in Python, and uses the OpenCV library to capture images from a camera. The script then uses the image data to generate a truly random seed. It will then XOR least significant bits of the image data for all channels (giving more significance to noise and other almost impossible to predict artifacts) and then "fold" the data with additional XOR to derrive at a large seed. 

The idea is to enhance the noise effects of the optical sensor, and then use the image data to generate a truly random seed. Image randomness is relatively high and unpredictable. Elements such as dust particles, light, reflection, air pressure, moisture, sensor noise and other artifacts are the ones this script aims to capture and magnify. The image itself is of no value. As long as the sensor is not completely covered or completely exposed, entropy of the data should be high on the [Shannon scale](https://towardsdatascience.com/what-is-shannons-entropy-5ad1b5a83ce1).

Our tests consistently show over 0.99999 factors on the Shannon Entropy scale, which is a very high level of entropy.

We know the code is not perfect, and we are open to suggestions and improvements [at any time](https://www.github.com/ytisf/aasdfg).

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

Installation from Github:
```bash
pip install -U git+https://github.com/ytisf/aasdfg.git
```

Installation (manual):
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

seed = GenerateSeed(photo_count=1, folds=1, verbose=False, trigger=True)
# photo_count = How many photos to take from the webcam. Will directly impact length of seed.
# folds = How many times to fold the data. Will directly impact length of seed. The higher the fold, less data and less entropy. 
# verbose = Print out the seed as it is generated.
# trigger = Will raise exception if shannon entropy is not high enough. Setting this flag to False is NOT recommended. As for whatever reason entropy is not high enough, the seed will be returned as usual and no alerts will be raised.
```



