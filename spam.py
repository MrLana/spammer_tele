from telethon.sync import TelegramClient
from telethon.tl.functions.messages import SendMessageRequest
import time

# Konfigurasi
api_id = 24851732  # Dapatkan dari my.telegram.org
api_hash = '7b910a141e9d0a997ca07b208bfd8621'  # Dapatkan dari my.telegram.org
phone_number = '+6285966576582'  # Nomor Telegram Anda
target_username = 'novanathaliaa'  # Ganti dengan username/ID penipu
message = "⚠ WARNING! SCAMMER ALERT! ⚠\nOrang ini adalah penipu, jangan percaya!"  # Pesan spam
jumlah_pesan = 100  # Jumlah pesan yang dikirim
delay = 2  # Jeda antar pesan (detik)

# Inisialisasi client
client = TelegramClient('session_name', api_id, api_hash)

async def spam_penipu():
    await client.start(phone_number)
    print("Login berhasil!")
    
    try:
        target = await client.get_entity(target_username)
    except Exception as e:
        print(f"Error: {e}")
        return
    
    for i in range(jumlah_pesan):
        try:
            await client.send_message(target, f"{message} ({i+1}/{jumlah_pesan})")
            print(f"[+] Pesan {i+1} terkirim!")
            time.sleep(delay)
        except Exception as e:
            print(f"[!] Gagal mengirim pesan: {e}")
            time.sleep(5)  # Tunggu jika ada error
    
    print("Spam selesai!")
    await client.disconnect()

with client:
    client.loop.run_until_complete(spam_penipu())
