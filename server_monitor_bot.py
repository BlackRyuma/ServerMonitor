import psutil
import asyncio
import subprocess
from telegram import Bot

# Masukkan token API bot Anda
BOT_TOKEN = "YOUR_BOT_API_TOKEN"
CHANNEL_ID = "@YourChannelUsername"  # Ganti dengan username channel Anda

async def get_server_info():
    # CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)

    # Memory usage
    memory = psutil.virtual_memory()
    memory_usage = memory.percent

    # Ping Google
    try:
        ping_output = subprocess.check_output(
            ["ping", "-c", "1", "8.8.8.8"], universal_newlines=True
        )
        ping_time = ping_output.split("time=")[-1].split(" ")[0]
    except Exception as e:
        ping_time = "Ping failed"

    # Format informasi
    server_info = (
        f"**Server Status**\n"
        f"CPU Usage: {cpu_usage}%\n"
        f"Memory Usage: {memory_usage}%\n"
        f"Ping: {ping_time} ms"
    )
    return server_info

async def send_to_telegram():
    bot = Bot(token=BOT_TOKEN)
    while True:
        message = await get_server_info()
        await bot.send_message(chat_id=CHANNEL_ID, text=message, parse_mode="Markdown")
        await asyncio.sleep(600)  # Kirim setiap 600 detik (10 menit)

if __name__ == "__main__":
    asyncio.run(send_to_telegram())
