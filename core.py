import discord
from discord.ext import commands
import psutil
from datetime import datetime

from src.core.fmt_delta import format_timedelta
from src.core.fmt_mem import memory_format
from src.commands.status_update import run_status
from src.core.logger import CustomLogger
from src.core.get_os import get_os_name

from config_dev import settings

custom_logger = CustomLogger(logger_name=__name__, log_level='info', logfile_name='core.log')
core_logger = custom_logger.create_logger()

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix=settings['prefix'], intents=intents)

start_time = datetime.now()


@bot.event
async def on_connect():
    sleep_time = settings['sleep time']
    timeout = settings['timeout']

    return await run_status(bot, start_time, sleep_time, timeout)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print(f'ON OS -  {get_os_name()}')
    core_logger.info(f'Logged in as {bot.user.name} on {bot.guilds}')


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
    core_logger.info(f'{bot.user.name} Shutdown by {ctx.message.author.name} (user ID - {ctx.message.author.id})')
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
