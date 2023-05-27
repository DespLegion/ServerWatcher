import discord
from discord.ext import commands
import psutil
from datetime import datetime
from asyncio import sleep

from src.core.fmt_delta import format_timedelta
from src.core.fmt_mem import memory_format

from config import settings

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix=settings['prefix'], intents=intents)

global start_time


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    global start_time
    start_time = datetime.now()
    sleep_time = settings['sleep time']

    while True:
        try:
            cpu_stats = psutil.cpu_percent()
            try:
                await bot.change_presence(
                    status=discord.Status.online,
                    activity=discord.Game(f'CPU: {cpu_stats}%')
                )
            except Exception:
                await bot.change_presence(
                    status=discord.Status.do_not_disturb,
                    activity=discord.Game(f'CPU status update Error')
                )
        except Exception:
            await bot.change_presence(
                status=discord.Status.do_not_disturb,
                activity=discord.Game(f'CPU update Error')
            )
        await sleep(sleep_time)

        try:
            vr_memory_stats = psutil.virtual_memory().percent
            try:
                await bot.change_presence(
                    status=discord.Status.online,
                    activity=discord.Game(f'RAM: {vr_memory_stats}%')
                )
            except Exception:
                await bot.change_presence(
                    status=discord.Status.do_not_disturb,
                    activity=discord.Game(f'RAM status update Error')
                )
        except Exception:
            await bot.change_presence(
                status=discord.Status.do_not_disturb,
                activity=discord.Game(f'RAM update Error')
            )
        await sleep(sleep_time)

        try:
            now = datetime.now()
            uptime_c = now - start_time
            try:
                await bot.change_presence(
                    status=discord.Status.online,
                    activity=discord.Game(f'Uptime: {format_timedelta(uptime_c)}')
                )
            except Exception:
                await bot.change_presence(
                    status=discord.Status.do_not_disturb,
                    activity=discord.Game(f'Uptime status update Error')
                )
        except Exception:
            await bot.change_presence(
                status=discord.Status.do_not_disturb,
                activity=discord.Game(f'Uptime update Error')
            )
        await sleep(sleep_time)


@bot.command()
@commands.has_permissions(administrator=True)
async def status(ctx):
    now = datetime.now()
    uptime_c = now - start_time
    embed = discord.Embed(title='System Status', description='')
    embed.add_field(name='CPU', value=f'{psutil.cpu_percent()}%', inline=False)
    embed.add_field(name='RAM', value=f'{psutil.virtual_memory().percent}%', inline=False)
    embed.add_field(name='Uptime', value=f'{format_timedelta(uptime_c)}', inline=False)
    await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(administrator=True)
async def system(ctx):
    disks = psutil.disk_partitions()
    now = datetime.now()
    uptime_c = now - start_time
    embed = discord.Embed(title='System Resource', description='')
    embed.add_field(name='CPU count', value=f'{psutil.cpu_count()}', inline=False)
    embed.add_field(name='Physical CPU count', value=f'{psutil.cpu_count(logical=False)}', inline=False)
    embed.add_field(name='Total RAM memory', value=f'{memory_format(psutil.virtual_memory().total)} GB', inline=False)
    for disk in disks:
        embed.add_field(
            name=f'Disk {disk.mountpoint} memory',
            value=f'{memory_format(psutil.disk_usage(f"{disk.mountpoint}").total)} GB |'
                  f' {memory_format(psutil.disk_usage(f"{disk.mountpoint}").free)} GB Free',
            inline=False
        )
    embed.add_field(name='Server Uptime', value=f'{format_timedelta(uptime_c)}', inline=False)
    await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(administrator=True)
async def net(ctx):
    net_stats = psutil.net_io_counters()
    embed = discord.Embed(title='Network usage', description='')
    embed.add_field(name='Sent', value=f'{memory_format(net_stats.bytes_sent)} GB', inline=False)
    embed.add_field(name='Received', value=f'{memory_format(net_stats.bytes_recv)} GB', inline=False)
    await ctx.send(embed=embed)


@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    exit()


@status.error
@system.error
@net.error
@shutdown.error
async def permission_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            description=f'{ctx.message.author.mention}, Permission Denied!',
            color=0xFF0000
        )
        await ctx.send(embed=embed)


bot.run(settings['token'])
