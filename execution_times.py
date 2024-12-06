import os
import pandas as pd
import matplotlib.pyplot as plt

# Directory containing the files
directory = r"C:\Users\Asus\Desktop\GPT-4o-and-Gemini-API-Prompt\excution time"

# Initialize dictionaries to store data
data_gpt4 = {}
data_gemini = {}
data_human = {}

# Process each file in the directory
for filename in os.listdir(directory):
    if filename.endswith("_GPT-4o.txt"):
        model = "GPT-4o"
    elif filename.endswith("_Gemini.txt"):
        model = "Gemini"
    elif filename.endswith("_Human.txt"):
        model = "Human"
    else:
        continue  # Skip files that don't match

    filepath = os.path.join(directory, filename)

    # Read the file and accumulate data
    with open(filepath, 'r') as file:
        next(file)  # Skip the header line
        for line_number, line in enumerate(file, start=2):  # Start at 2 because of the skipped header
            try:
                problem, time = line.strip().split(', ')
                problem = int(problem)  # Ensure problem is an integer
                time = float(time)  # Ensure time is a float

                if model == "GPT-4o":
                    if problem not in data_gpt4:
                        data_gpt4[problem] = []
                    data_gpt4[problem].append(time)
                elif model == "Gemini":
                    if problem not in data_gemini:
                        data_gemini[problem] = []
                    data_gemini[problem].append(time)
                elif model == "Human":
                    if problem not in data_human:
                        data_human[problem] = []
                    data_human[problem].append(time)
            except ValueError:
                # Skip lines that don't match the expected format
                print(f"Skipping invalid line {line_number} in {filename}: {line.strip()}")

# Calculate averages
avg_gpt4 = {problem: sum(times) / len(times) for problem, times in data_gpt4.items()}
avg_gemini = {problem: sum(times) / len(times) for problem, times in data_gemini.items()}
avg_human = {problem: sum(times) / len(times) for problem, times in data_human.items()}

# Combine all problems
all_problems = list(set(data_gpt4.keys()) | set(data_gemini.keys()) | set(data_human.keys()))

# Create a DataFrame to store averages and calculate best times
df = pd.DataFrame({
    'Problem': all_problems,
    'Avg_GPT4': [avg_gpt4.get(problem, float('inf')) for problem in all_problems],
    'Avg_Gemini': [avg_gemini.get(problem, float('inf')) for problem in all_problems],
    'Avg_Human': [avg_human.get(problem, float('inf')) for problem in all_problems]
})
df['Best_Time'] = df[['Avg_GPT4', 'Avg_Gemini', 'Avg_Human']].min(axis=1)

# Calculate distances from best times
df['Dist_GPT4'] = (df['Avg_GPT4'] / df['Best_Time'])
df['Dist_Gemini'] = (df['Avg_Gemini'] / df['Best_Time'])
df['Dist_Human'] = (df['Avg_Human'] / df['Best_Time'])

# Calculate average distances for each group
avg_distances = {
    'GPT-4o': df['Dist_GPT4'].mean(),
    'Gemini': df['Dist_Gemini'].mean(),
    'Human': df['Dist_Human'].mean()
}

# Display the results in the terminal with three decimal places
print("Average Distances from Best Times:")
for model, avg_dist in avg_distances.items():
    print(f"{model}: {avg_dist:.3f}")

# Save averages and best time to a tab-delimited text file
output_file = r"C:\Users\Asus\Desktop\execution_time_results.txt"
df[['Problem', 'Avg_GPT4', 'Avg_Gemini', 'Avg_Human', 'Best_Time']].to_csv(
    output_file, sep='\t', index=False, float_format='%.3f'  # Save with 3 decimal places
)
print(f"Results saved to {output_file}")

# Sort the problems to ensure proper order
df.sort_values('Problem', inplace=True)

# Create evenly spaced indices for the x-axis
x_positions = range(len(df['Problem']))

# Plot the data
plt.figure(figsize=(12, 8))
plt.plot(
    x_positions, df['Avg_GPT4'], label="GPT-4o", marker='o', linestyle='--', linewidth=2
)
plt.plot(
    x_positions, df['Avg_Gemini'], label="Gemini", marker='s', linestyle='--', linewidth=2
)
plt.plot(
    x_positions, df['Avg_Human'], label="Human", marker='^', linestyle='--', linewidth=2
)
plt.plot(
    x_positions, df['Best_Time'], label="Best Time", marker='x', linestyle='-', linewidth=2, color='black'
)

# Set x-axis ticks to correspond to the problem names
plt.xticks(x_positions, labels=df['Problem'], fontsize=10, rotation=45)
plt.xlabel("Problem Number IDs", fontsize=14)
plt.ylabel("Execution Time (ms)", fontsize=14)
plt.title("Execution Time per Problem for GPT-4o, Gemini, and Humans", fontsize=16)
plt.legend(fontsize=12)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()