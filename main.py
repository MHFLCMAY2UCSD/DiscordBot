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
    @commands.has_role("Bot Boi")
    async def kick(ctx, member: discord.Member, *, reason=None):
        if str(member.id) == "193219019292016641":
            print(member, " tried to ban you")
            return

        await ctx.channel.purge(limit=1)

        await member.kick(reason=reason)

    # Ban member
    @bot.command()
    @commands.has_role("Bot Boi")
    async def ban(ctx, member: discord.Member, *, reason=None):
        if str(member.id) == "193219019292016641":
            print(member, " tried to Kick you")
            return

        await ctx.channel.purge(limit=1)

        await member.ban(reason=reason)

    # Looping Disconnect member
    @bot.command("disconnect", aliases=["dc"])
    # @commands.is_owner()
    @commands.has_role("Bot Boi")
    async def disconnect(ctx, *, member: discord.Member, value=10):
        print("log: ", member, " Iteration: value")

        # Clean the evidence.
        await ctx.channel.purge(limit=1)

        if str(member.id) == "193219019292016641":
            print(member, " tried to DC you.")
            return

        # clear user messages before action
        for iteration in range(int(value)):
            big_winner = random.randint(1, 1)

            # Infinite Dc!!
            time.sleep(big_winner)
            await member.move_to(None)

        print("Event over for", member, "\n")
        # await ctx.send(f"iterations: {iteration}. Timer: {big_winner}")

    @bot.command()  # TODO Does not work
    @commands.is_owner()
    async def move(ctx, member: discord.Member, channel1: discord.VoiceChannel, channel2: discord.VoiceChannel, value=0):

        await ctx.channel.purge(limit=1)

        print("Moving Member:", member, "to channel:",
              channel1, "and channel:", channel2)

        for i in range(value):
            if i % 2 == 0:
                await member.move_to(channel1)
            else:
                await member.move_to(channel2)
            time.sleep(.5)

        print("Event over for:", member, "\n")

    @ bot.command()
    async def shutdown(ctx):

        await ctx.send("Shutting Down")

        time.sleep(2)
        await ctx.channel.purge(limit=2)

        await bot.close()

    @ bot.command()
    async def test(ctx, member: discord.Member):
        await ctx.send(member.id)

    bot.run("", bot=True)


main()
