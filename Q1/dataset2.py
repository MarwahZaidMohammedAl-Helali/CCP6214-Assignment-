import random
import math

# Sum of group members' IDs
member1 = 1221301995
member2 = 1211307919
max_value = member1 + member2

# Initialize random seed with the current system time or other entropy source
random.seed()

# Number of stars and edges
num_stars = 20
num_edges = 54
min_connections_per_star = 3

# Define a smaller range for coordinates
coord_max_value = 100

# Generate star data
stars = []
star_names = [f"Star {chr(65 + i)}" for i in range(num_stars)]

for name in star_names:
    x = random.randint(0, coord_max_value)
    y = random.randint(0, coord_max_value)
    z = random.randint(0, coord_max_value)
    weight = random.randint(1, 100)  # Keep weight within 1 to 100
    profit = random.randint(1, 100)  # Keep profit within 1 to 100
    stars.append((name, x, y, z, weight, profit))

# Generate edges ensuring each star connects to at least 3 other stars
edges = []
connections = {star: set() for star in star_names}

# Ensure minimum connections
for star in star_names:
    while len(connections[star]) < min_connections_per_star:
        other_star = random.choice(star_names)
        if other_star != star and other_star not in connections[star]:
            connections[star].add(other_star)
            connections[other_star].add(star)
            edges.append((star, other_star))

# Add remaining edges randomly
while len(edges) < num_edges:
    star1, star2 = random.sample(star_names, 2)
    if star2 not in connections[star1]:
        connections[star1].add(star2)
        connections[star2].add(star1)
        edges.append((star1, star2))

# Calculate distances
def calculate_distance(x1, y1, z1, x2, y2, z2):
    return int(math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2))

distances = []
for star1, star2 in edges:
    star1_data = next(star for star in stars if star[0] == star1)
    star2_data = next(star for star in stars if star[0] == star2)
    distance = calculate_distance(star1_data[1], star1_data[2], star1_data[3], star2_data[1], star2_data[2], star2_data[3])
    distances.append((star1, star2, distance))

# Write dataset to a text file
with open("dataset2.txt", "w") as file:
    file.write("Name x y z weight profit\n")
    for star in stars:
        file.write(f"{star[0]} {star[1]} {star[2]} {star[3]} {star[4]} {star[5]}\n")
    
    file.write("\nEdges with distances:\n")
    file.write("Star1 Star2 Distance\n")
    for star1, star2, distance in distances:
        file.write(f"{star1} {star2} {distance}\n")

print("Dataset generated and saved to dataset2.txt")
