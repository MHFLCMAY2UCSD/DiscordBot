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
    @commands.check_any(commands.is_owner(), commands.has_role("Bot Boi"))
    async def clear(ctx, amount=5):
        await ctx.channel.purge(limit=amount)

    # Kick members
    @bot.command()
    @commands.check_any(commands.is_owner(), commands.has_role("Bot Boi"))
    async def kick(ctx, member: discord.Member, *, reason=None):
        if str(member.id) == "193219019292016641":
            print(member, " tried to ban you")
            return

        await ctx.channel.purge(limit=1)

        print("Kick member: ", member, "\n")

        await member.kick(reason=reason)

    # Ban member
    @ bot.command()
    @ commands.check_any(commands.is_owner(), commands.has_role("Bot Boi"))
    async def ban(ctx, member: discord.Member, *, reason=None):
        if str(member.id) == "193219019292016641":
            print(member, " tried to Kick you")
            return

        await ctx.channel.purge(limit=1)

        print(f"Ban member: {member}")

        await member.ban(reason=reason)

    # UnBan member
    @bot.command()
    @commands.check_any(commands.is_owner(), commands.has_role("Bot Boi"))
    async def unban(ctx, *, member):
        await ctx.channel.purge(limit=1)

        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                print(f"Unbanned member: {user}")
                break

    # Looping Disconnect member
    @ bot.command("disconnect", aliases=["dc"])
    # @commands.is_owner()
    @ commands.check_any(commands.is_owner(), commands.has_role("Bot Boi"))
    async def disconnect(ctx, value=10, *members: discord.Member):
        await ctx.channel.purge(limit=1)  # Clean the evidence.

        for member in members:
            print("log: ", member, " Iteration: ", value)

            if str(member.id) == "193219019292016641":
                print(member, " tried to DC you.")
                return

            for iteration in range(int(value)):
                big_winner = random.randint(1, 3)

                time.sleep(big_winner)
                await member.move_to(None)

            print("Event over for", member, "\n")
            # await ctx.send(f"iterations: {iteration}. Timer: {big_winner}")

    @ bot.command()
    @ commands.is_owner()
    async def move(ctx, member: discord.Member, channel1: discord.VoiceChannel, channel2: discord.VoiceChannel, value=10):
        # No Russians (CoD II Reference, not a racist)
        await ctx.channel.purge(limit=1)

        print("Moving Member:", member, "to channel:",
              channel1, "and channel:", channel2)

        for i in range(value):
            channel = channel1 if i % 2 == 0 else channel2
            await member.move_to(channel)
            time.sleep(.4)

        print("Event over for:", member, "\n")

    # TODO
    # Mute/Deafen alternate
    # @bot.command(aliases=["m"])
    # @commands.has_permissions(manage_messages=True)
    # async def mute(ctx, member: discord.Member):
    #     await ctx.channel.purge(limit=1)

    #     muted_role = ctx.guild.get_role(962601359117516811)

    #     await member.add_role(muted_role)

    @ bot.command()
    @ commands.check_any(commands.is_owner(), commands.has_role("Bot Boi"))
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
