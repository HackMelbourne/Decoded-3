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

            self.style = discord.ButtonStyle.danger
            self.label = 'X'
            self.disabled = True
            self.view.board[self.row][self.col] = 1
            self.view.current_player = self.view.player_2
            content = f":game_die: `{self.view.player_1.display_name}` **VS** `{self.view.player_2.display_name}`\n\n{self.view.player_2.mention}, select your move:"

        else:
            if interaction.user != self.view.player2:
                await interaction.response.send_message("Its not your Turn!", ephemeral=True)
                return

            self.style = discord.ButtonStyle.success
            self.label = 'O'
            self.disabled = True
            self.view.board[self.row][self.col] = -1
            self.view.current_player = self.view.player_1
            content = f":game_die: `{self.view.player_1.display_name}` **VS** `{self.view.player_2.display_name}`\n\n{self.view.player_1.mention}, select your move:"

        winner = self.view.check_winner()
        if winner == self.view.player1:
            content = f":tada: {self.view.player_1.mention} has won the game!"
        elif winner == self.view.player2:
            content = f":tada: {self.view.player_2.mention} has won the game!"
        elif winner == "tie":
            content = "No one won the game, it's a tie! Try again?"

        # for child in self.view.children:
        #     child.disabled = True
        #     self.view.stop()

        await interaction.response.edit_message(content=content, view=self.view)


class TicTacToe(discord.ui.View):
    def __init__(self, player_1, player_2):
        super().__init__()
        self.player_1 = player_1
        self.player_2 = player_2
        self.current_player = self.player_1
        self.board = np.zeros((SIZE, SIZE))

        for row in range(SIZE):
            for col in range(SIZE):
                self.add_item(TicTacToeButton(row, col))

    def check_winner(self):
        col_sums = np.sum(self.board, axis=1)
        for col_sum in col_sums:
            if col_sum == SIZE:
                return self.player_1
            elif col_sum == -SIZE:
                return self.player_2

        row_sums = np.sum(self.board, axis=0)
        for row_sum in row_sums:
            if row_sum == SIZE:
                return self.player_1
            elif row_sum == -SIZE:
                return self.player_2

        diag_sum = self.board[0, 0] + self.board[1, 1] + self.board[2, 2]
        if diag_sum == SIZE:
            return self.player_1
        elif diag_sum == -SIZE:
            return self.player_2

        diag_sum = self.board[0, 2] + self.board[1, 1] + self.board[2, 0]
        if diag_sum == SIZE:
            return self.player_1
        elif diag_sum == -SIZE:
            return self.player_2

        if np.all(self.board):
            return "tie"


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="tictactoe",
        description="Play a game of TicTacToe"
    )
    @app_commands.describe(
        opponent="User you want to play with"
    )
    async def tictactoe(self, interaction, opponent: discord.Member):
        player_1 = interaction.user
        player_2 = opponent

        if player_1 == player_2 or player_2.bot:
            await interaction.response.send_message("you cannot challenge that user")
        else:
            await interaction.response.send_message(
                f":game_die: `{player_1.display_name}` **VS** `{player_2.display_name}`\n\n{player_1.mention}, select your move:",
                view=TicTacToe(player_1, player_2))


async def setup(bot):
    await bot.add_cog(
        Commands(bot),
        guilds=bot.GUILDS
    )
