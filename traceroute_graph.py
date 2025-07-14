import matplotlib.pyplot as plt

# Replace with actual traceroute data if needed
hops = ["Your PC", "Router", "ISP Gateway", "Google"]
latencies = [2, 10, 25, 30]

plt.plot(hops, latencies, marker='o', color='green')
plt.title("Traceroute Hop Latency")
plt.xlabel("Hop")
plt.ylabel("Latency (ms)")
plt.grid(True)
plt.tight_layout()
plt.show() 