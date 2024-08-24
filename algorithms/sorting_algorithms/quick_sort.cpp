#include <vector>
#include <utility>

std::vector<std::vector<int>> quick_sort(std::vector<int>& arr, int low, int high) {
    std::vector<std::vector<int>> states;

    if (low < high) {
        int pi = partition(arr, low, high, states);
        auto left_states = quick_sort(arr, low, pi - 1);
        auto right_states = quick_sort(arr, pi + 1, high);

        states.insert(states.end(), left_states.begin(), left_states.end());
        states.insert(states.end(), right_states.begin(), right_states.end());
    }

    return states;
}

int partition(std::vector<int>& arr, int low, int high, std::vector<std::vector<int>>& states) {
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            std::swap(arr[i], arr[j]);
            states.push_back(arr);  // Capture the array state
        }
    }

    std::swap(arr[i + 1], arr[high]);
    states.push_back(arr);  // Capture the final array state after pivot swap

    return i + 1;
}
