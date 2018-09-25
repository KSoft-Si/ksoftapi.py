# KSoft.Si API

## Official Python wrapper
### Install
You can install using pip: `pip install ksoftapi`

### Example (with discord.py)

```python
import ksoftapi

client = ksoftapi.Client(api_key="your_api_key_here")

@commands.command()
async def birb(ctx):
    img = await client.random_image("birb")
    await ctx.send(img.url)
    
```
