<img style="object-fit: contain;" src="https://cdn.ksoft.si/images/ksoft-logo-text.png" height="50" width="100%">

<center><i>Official Python wrapper</i></center>

## Install
Installing via pip: `pip install ksoftapi`

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