from discord.ext import commands
import discord
from discord import app_commands

import numpy as np

SIZE = 3


class TicTacToeButton(discord.ui.Button):
    def __init__(self, row, col):
        super().__init__(style=discord.ButtonStyle.secondary, label=" ", row=row)
        self.row = row
        self.col = col

    async def callback(self, interaction):
        if self.view.current_player == self.view.player1:
            if interaction.user != self.view.player1:
                await interaction.response.send_message("Its not your Turn!", ephemeral=True)
                return
            else:
                self.style = discord.ButtonStyle.danger
                self.label = 'X'
                self.disabled = True
                self.view.board[self.row][self.col] = 1
                self.view.current_player = self.view.player2
                content = f"{self.view.player2.mention}, select your move:"

        else:
            if interaction.user != self.view.player2:
                await interaction.response.send_message("Its not your Turn!", ephemeral=True)
                return
            else:
                self.style = discord.ButtonStyle.success
                self.label = 'O'
                self.disabled = True
                self.view.board[self.row][self.col] = -1
                self.view.current_player = self.view.player1
                content = f"{self.view.player1.mention}, select your move:"

        winner = self.view.check_winner()
        if winner == self.view.player1:
            content = 'player1 won!'
        elif winner == self.view.player2:
            content = 'player2 won!'
        elif winner == "tie":
            content = "It's a tie!"

        # for child in self.view.children:
        #     child.disabled = True
        #
        #     self.view.stop()

        await interaction.response.edit_message(content=content, view=self.view)


class TicTacToe(discord.ui.View):
    def __init__(self, player1, player2):
        super().__init__()
        self.player1 = player1
        self.player2 = player2
        self.current_player = self.player1
        self.board = np.zeros((SIZE, SIZE))

        for row in range(SIZE):
            for col in range(SIZE):
                self.add_item(TicTacToeButton(row, col))

    def check_winner(self):
        col_sums = np.sum(self.board, axis=1)
        for col_sum in col_sums:
            if col_sum == SIZE:
                return self.player1
            elif col_sum == -SIZE:
                return self.player2

        row_sums = np.sum(self.board, axis=0)
        for row_sum in row_sums:
            if row_sum == SIZE:
                return self.player1
            elif row_sum == -SIZE:
                return self.player2

        diag_sum = self.board[0, 0] + self.board[1, 1] + self.board[2, 2]
        if diag_sum == SIZE:
            return self.player1
        elif diag_sum == -SIZE:
            return self.player2

        diag_sum = self.board[0, 2] + self.board[1, 1] + self.board[2, 0]
        if diag_sum == SIZE:
            return self.player1
        elif diag_sum == -SIZE:
            return self.player2

        if np.all(self.board):
            return "tie"


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="tictactoe",
        description="Play a game of TicTacToe"
    )
    async def tictactoe(self, interaction, opponent: discord.Member):
        player1 = interaction.user
        player2 = opponent

        await interaction.response.send_message(f"{player1.mention} **VS** {player2.mention}",
                                                view=TicTacToe(player1, player2))


async def setup(bot):
    await bot.add_cog(
        Commands(bot),
        guilds=bot.GUILDS
    )
