import re
import collections
import matplotlib.pyplot as plt
import requests
import folium

# Step 1: Extract IPs from cowrie.log
ip_pattern = re.compile(r'from (\d+\.\d+\.\d+\.\d+)')
with open("cowrie.log", "r") as f:
    ips = ip_pattern.findall(f.read())

# Step 2: Count frequency of each IP
counter = collections.Counter(ips)
top_ips = counter.most_common(5)

# Step 3: Bar Graph - Most Frequent Attackers
ip_labels, ip_counts = zip(*top_ips)
plt.figure(figsize=(8, 5))
plt.bar(ip_labels, ip_counts, color='skyblue')
plt.title("Top Attacking IPs")
plt.xlabel("IP Address")
plt.ylabel("Attempt Count")
plt.tight_layout()
plt.savefig("bar_graph_ips.png")
plt.close()

# Step 4: Geo-map using Folium
m = folium.Map(location=[0, 0], zoom_start=2)
for ip, _ in top_ips:
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        loc = data.get("loc", "")
        if loc:
            lat, lon = map(float, loc.split(","))
            folium.Marker(location=[lat, lon], popup=ip).add_to(m)
    except Exception as e:
        print(f"Failed to locate {ip}: {e}")

m.save("geo_map.html")
print("✔ Bar chart saved as bar_graph_ips.png")
print("✔ Geo map saved as geo_map.html")
