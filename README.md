# Bitly URL shortener
The script make urls shorter and shows how many times followed the url. 

# How to start

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```bash
pip install -r requirements.txt
```

### Environment variables.

- BITLY_BEARER_TOKEN

.env example:

```
BITLY_BEARER_TOKEN=ab5a34ft462d107da143a9c011g67b5df7470360
```
### How to get

1. Sign up [bit.ly](https://bit.ly)

2. Bitly offers several types of tokens. You need GENERIC ACCESS TOKEN. Use e-mail instead of social networks. It will simplify receiving a token.

### Run

Launch on Linux or Windows as simple

```bash
$ python main.py https://mysite.com

# You will see

$ python main.py https://mysite.com
Short url: https://bit.ly/3x9NyXX
Your url was clicked 1 time(s) 
```

### Project Goals

This code was written for educational purposes as part of an online course for web developers at dvmn.org.
