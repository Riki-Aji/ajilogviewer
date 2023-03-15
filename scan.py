import re
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

# Inisialisasi colorama
colorama.init(autoreset=True)

# Baca variabel xss, sql, dan lfi dari file eksternal
with open('regex.txt', 'r') as f:
    xss = f.readline().strip()
    sql = f.readline().strip()
    lfi = f.readline().strip()
    cmdi = f.readline().strip()

# Buat objek regex untuk mencari karakter yang match dengan regex xss, sql, dan lfi
pattern_xss = re.compile(xss)

# Fungsi untuk mengganti karakter yang match dengan regex xss dengan versi yang diwarnai
def replace_xss(match_obj):
    return Fore.BLUE + match_obj.group(0) + Fore.RED

# Baca file log dan cari serangan
with open('log.txt', 'r') as file:
    for line in file:
        # Mewarnai karakter yang match dengan regex xss menjadi biru
        line = pattern_xss.sub(replace_xss, line)
        
        # Mengecek jenis serangan dan menampilkan pesan yang sesuai
        if re.search(xss, line):
            print(Fore.RED + "XSS Detected: " + line.strip())
        elif re.search(sql, line):
            print(Fore.YELLOW + "SQL Injection Detected: " + line.strip())
        elif re.search(lfi, line):
            print(Fore.GREEN + "Local File Inclusion Detected: " + line.strip())
        elif re.search(cmdi, line):
            print(Fore.MAGENTA + "Command Injection Detected: " + line.strip())
