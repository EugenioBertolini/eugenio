import numpy as np
import matplotlib

matplotlib.use("TkAgg")  # Use TkAgg backend
import matplotlib.pyplot as plt
from enum import Enum


# Define an Enum class for colors
class Color(Enum):
    BLUE = "#1f77b4"
    ORANGE = "#ff7f0e"
    GREEN = "#2ca02c"
    RED = "#d62728"
    PURPLE = "#9467bd"


# Main function to plot a "Happy Birthday" graph
def main():

    x = np.linspace(-10, 10, 1001)
    s = np.sinc(x)

    # Create a figure and axis with specified figure size
    fig, ax = plt.subplots(figsize=(10, 6))

    # Hide the axes
    ax.axis("off")

    # Add some decorative elements
    for i, color in enumerate(Color, start=1):
        # Adjust the line positions so they are visible in the plot
        ax.plot(
            [i * 5 - 10, i * 5 + 10],
            [abs(i * 0.2), abs(i * 0.2)],
            color=color.value,
            linewidth=4,
        )

    # Set the title using text, ensure it is within the figure bounds
    ax.text(
        0.5,
        0.75,
        "Happy Birthday!",
        fontsize=25,
        color=Color.GREEN.value,
        ha="center",
        va="center",
        transform=ax.transAxes,
    )

    ax.plot(x, s, "--b", linewidth=5)

    # Display the plot
    plt.show()


if __name__ == "__main__":
    main()
