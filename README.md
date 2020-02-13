<img align="right" src="https://cdn.ksoft.si/images/Logo1024-W.png" height="150" width="150">

# KSoft.Si API
## Official Python wrapper

## Install
Installing via pip is as easy as running the following: `pip install ksoftapi`

## Example Usage:
```python
import ksoftapi

kclient = ksoftapi.Client('Your API key here')

async def find_lyrics(query: str):
    try:
        results = await kclient.music.lyrics(query)
    except ksoftapi.NoResults:
        print('No lyrics found for ' + query)
    else:
        first = results[0]
        print(first.lyrics)
```

[Obtain an API key](https://api.ksoft.si/) | [Join the Discord server](https://discordapp.com/invite/gRB2mNh)