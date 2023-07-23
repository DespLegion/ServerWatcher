import asyncio

import discord
import psutil

from datetime import datetime
from asyncio import sleep

from src.core.fmt_delta import format_timedelta
from src.core.logger import CustomLogger

custom_logger = CustomLogger(logger_name=__name__, logfile_name='status_update_logs.log')
status_logger = custom_logger.create_logger()


async def update_cpu_stats(bot, sleep_time):
    cpu_stats = psutil.cpu_percent()
    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Game(f'CPU: {cpu_stats}%')
    )
    status_logger.info(f'CPU status updated successfully!')
    await sleep(sleep_time)


async def update_memory_stats(bot, sleep_time):
    vr_memory_stats = psutil.virtual_memory().percent
    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Game(f'RAM: {vr_memory_stats}%')
    )
    status_logger.info(f'RAM status updated successfully!')
    await sleep(sleep_time)


async def uptime_update(bot, sleep_time, start_time):
    now = datetime.now()
    uptime_c = now - start_time
    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Game(f'Uptime: {format_timedelta(uptime_c)}')
    )
    status_logger.info(f'Uptime status updated successfully!')
    await sleep(sleep_time)


async def run_status(bot, start_time, sleep_time, timeout):

    try:
        status_logger.info(f'---- Status loop started! ----')
        while True:
            try:
                await asyncio.wait_for(update_cpu_stats(bot, sleep_time), timeout=timeout)
            except asyncio.TimeoutError as te:
                status_logger.error(f'CPU status update timeout Error {te}')
                await bot.change_presence(
                    status=discord.Status.do_not_disturb,
                    activity=discord.Game(f'CPU status update Error')
                )
                await sleep(sleep_time)

            try:
                await asyncio.wait_for(update_memory_stats(bot, sleep_time), timeout=timeout)
            except asyncio.TimeoutError as te:
                status_logger.error(f'RAM status update timeout Error {te}')
                await bot.change_presence(
                    status=discord.Status.do_not_disturb,
                    activity=discord.Game(f'RAM status update Error')
                )
                await sleep(sleep_time)

            try:
                await asyncio.wait_for(uptime_update(bot, sleep_time, start_time), timeout=timeout)
            except asyncio.TimeoutError as te:
                status_logger.error(f'Uptime status update timeout Error {te}')
                await bot.change_presence(
                    status=discord.Status.do_not_disturb,
                    activity=discord.Game(f'Uptime update Error')
                )
                await sleep(sleep_time)
    except Exception as err:
        status_logger.error(f'Status loop brake Error - {err}', exc_info=True)
        await re_run_status(bot, start_time, sleep_time, timeout)


async def re_run_status(bot, start_time, sleep_time, timeout):
    status_logger.error(f'---- RE run status Started! ----')
    await sleep(60)
    await run_status(bot, start_time, sleep_time, timeout)
