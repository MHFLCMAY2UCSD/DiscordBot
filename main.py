import random
import time
import discord
from discord.ext import commands


def main():
    bot = commands.Bot(command_prefix='$')

    # Creating Decorators
    @bot.event
    async def on_ready():

        await bot.change_presence(status=discord.Status.invisible)

        print("The Bot is ready.")

    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Not a command in here.")

    @bot.command()
    async def ping(ctx):
        await ctx.send(f'Ping! {round(bot.latency * 1000)}ms')

    # Clear messages
    @bot.command()
    async def clear(ctx, amount=5):

        await ctx.channel.purge(limit=amount)

    # Kick members
    @bot.command()
    async def kick(ctx, member: discord.Member, *, reason = None):
        await member.kick(reason = reason)

    # Ban member
    @bot.command()
    async def ban(ctx, member: discord.Member, *, reason = None):
        await member.ban(reason = reason)

    # Infinite disconnect of @member
    @bot.command("disconnect", aliases=["dc"])
    async def disconnect(ctx, member: discord.Member, value=10):

        if str(member.id) == "193219019292016641":
            return

        # Infinite Dc!!!

        # clear user messages before action
        for iteration in range(int(value)):
            big_winner = random.randint(1, 1)

            time.sleep(big_winner)
            await member.move_to(None)

            # await ctx.send(f"iterations: {iteration}. Timer: {big_winner}")

    @bot.command(aliases=["sw"])  # TODO Does not work
    async def switch(ctx, member: discord.member):

        await ctx.send("Yes")

        channel_one = bot.get_channel(822722026803953688)
        channel_two = bot.get_channel(823110715950891068)

        await member.move_to(channel_one)
        await member.move_to(channel_two)

        # for iteration in range(60):
        #     await member.move_to(channel)

    # Just to state what the user is doing wrong.
    # @clear.error
    # @disconnect.error
    # # @switch.error
    # async def integer_errors(ctx, error):
    #     if isinstance(error, commands.UserInputError):
    #         await ctx.send("This is not an integer, please try again.")
    #         return

    @bot.command()
    async def shutdown(ctx):

        await ctx.send("Shutting Down")

        time.sleep(2)
        await ctx.channel.purge(limit=1)

        await bot.close()

    @bot.command()
    async def test(ctx, member: discord.Member):
        await ctx.send(member.id)

    bot.run("ODcwOTAzNDY3NjM4Njc3NTE1.YQTiDw.BV6KK98NYoNb_JQvnJ6CnuvywJw", bot=True)


main()
