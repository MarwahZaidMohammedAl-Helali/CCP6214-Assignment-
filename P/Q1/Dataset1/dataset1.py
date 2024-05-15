import random
import time

# Group leader's ID and extracting its unique digits
group_leader_id = "1211307415"
unique_digits = list(set(group_leader_id))

# Function to generate datasets
def generate_dataset(size, digits, filename, max_length=3):
    dataset = [int(''.join(random.choices(digits, k=random.randint(1, max_length)))) for _ in range(size)]
    with open(filename, 'w') as file:
        for number in dataset:
            file.write(f"{number}\n")

# Sizes of the datasets
dataset_sizes = [100, 1000, 10000, 100000, 500000, 1000000]
filenames = [f"Set{i+1}.txt" for i in range(len(dataset_sizes))]

# Seed the random number generator with the current time
random.seed(time.time())

# Generate and save datasets
for size, filename in zip(dataset_sizes, filenames):
    generate_dataset(size, unique_digits, filename)

print("Datasets generated and saved to text files successfully.")
