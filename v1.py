import discord
import numpy as np
from discord.ext import commands
import numpy
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")
ROWS = 3
COLS = 3

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@client.event
async def on_ready():
    print("ready...")


class TicTacToe(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.board = np.zeros((ROWS, COLS))
        self.player = 0

    for i in range(ROWS):
        for j in range(COLS):
            exec(f"""
@discord.ui.button(label=f" ", style=discord.ButtonStyle.secondary, row={i}) 
async def button_{i}_{j}(self, interaction, button):     
    if self.board[{i}, {j}] == 1:
        await interaction.response.edit_message(content="invalid move")
        return
    else:
        self.board[{i}, {j}] = 1

    if self.player == 0:
        button.style = discord.ButtonStyle.primary
        button.label = "X"
    if self.player == 1:
        button.style = discord.ButtonStyle.danger
        button.label = "O"
    
    if self.player == 1:
        self.player = 0
    elif self.player == 0:
        self.player = 1
    
    await interaction.response.edit_message(content="valid move", view=self)
            """)


@client.command()
async def tictactoe(ctx):
    await ctx.send(view=TicTacToe())


client.run(TOKEN)

if __name__ == '__main__':
    pass
