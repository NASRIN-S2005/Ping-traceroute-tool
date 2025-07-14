from ping3 import ping
import matplotlib.pyplot as plt

host = input("Enter host to ping (e.g., google.com): ")
count = int(input("How many pings?: "))

rtts = []

for i in range(count):
    delay = ping(host)
    if delay:
        rtt_ms = round(delay * 1000, 2)
        print(f"Reply from {host}: time={rtt_ms}ms")
        rtts.append(rtt_ms)
    else:
        print(f"Request timed out.")
        rtts.append(0)

# Plot RTTs
plt.figure(figsize=(8, 4))
plt.plot(range(1, count + 1), rtts, marker='o', color='blue', label="RTT")
plt.title(f"Ping Results to {host}")
plt.xlabel("Ping Attempt")
plt.ylabel("Latency (ms)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show() 