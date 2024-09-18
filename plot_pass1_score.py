import matplotlib.pyplot as plt

def plot_pass1_score(models, scores, temperature=1):
    """
    Function to plot the pass@1 score for different models, display the value at the edge of each column,
    and add a comment indicating the temperature used.

    :param models: List of model names to be displayed on the x-axis.
    :param scores: List of pass@1 scores corresponding to the models.
    :param temperature: The temperature value to be displayed as a comment.
    """
    # Define custom colors for specific models
    colors = []
    for model in models:
        if model == "Gemini-1.5-pro":
            colors.append('blue')
        elif model == "GPT-4o":
            colors.append('red')
        else:
            colors.append('skyblue')  # Default color for other models
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(models, scores, color=colors, width=0.4)  # Adjust width to make columns narrower
    plt.xlabel('Model')
    plt.ylabel('pass@1 Score')
    plt.title('Pass@1 Score for Different Models with Temperature = 1.2')
    plt.ylim(0, 1)  # Setting y-axis limits from 0 to 1

    # Add value labels on top of each bar
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, f'{yval:.3f}', ha='center', va='bottom')

    plt.show()

if __name__ == "__main__":
    # Plotting the pass_1_score
    models = ["Gemini-1.5-pro", "GPT-4o"]  # List of model names
    scores = [0.778, 0.833]  # List of corresponding pass_1_scores
    plot_pass1_score(models, scores, temperature=1)  # Call the plotting function with temperature
