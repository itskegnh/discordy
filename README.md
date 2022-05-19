# discordy
A Discord API wrapper for python.

```py
import discordy

client = discordy.Client(
    token="CLIENT_TOKEN",
)

channel = client.fetch.channel("CHANNEL_ID")
channel.send(embeds=[
    discordy.Embed(
        title="Hello World",
        description="This is an example embed.",
        color=0xFF0000,
    ),
])
```