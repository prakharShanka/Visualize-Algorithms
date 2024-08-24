import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.selection_sort import selection_sort
from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick_sort

def visualize_sorting(algorithm, array_size=20, speed=1.0):
    array = [random.randint(1, 100) for _ in range(array_size)]

    if algorithm == 'Bubble Sort':
        generator = bubble_sort(array)
    elif algorithm == 'Insertion Sort':
        generator = insertion_sort(array)
    elif algorithm == 'Selection Sort':
        generator = selection_sort(array)
    elif algorithm == 'Merge Sort':
        generator = merge_sort(array)
    elif algorithm == 'Quick Sort':
        generator = quick_sort(array)

    fig, ax = plt.subplots()
    ax.set_title(algorithm)

    bar_rects = ax.bar(range(len(array)), array, align="edge")
    ax.set_xlim(0, len(array))
    ax.set_ylim(0, int(1.1 * max(array)))

    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]

    def update_fig(array, rects, iteration):
        for rect, val in zip(rects, array):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f"Iterations: {iteration[0]}")

    anim = animation.FuncAnimation(
        fig, func=update_fig,
        fargs=(bar_rects, iteration), frames=generator, repeat=False, blit=False,
        interval=1000/speed  # Adjust the speed of the animation
    )
    plt.show()
