import token_handler
import discord
import message_handler

### Create async function

def run_bot():
    token = token_handler.get_token()

    intents = discord.Intents.default() #Configures bot
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user}, is now up and running")
    
    @client.event
    async def on_message(message):
        if message.author == client.user: # Prevents loops
            return
        
        username = message.author
        user_message = message.content
        channel = message.channel

        print(f"{username} posted {user_message} in {channel}")

        await message_handler.normal_message(message)


    client.run(token)
    
run_bot()