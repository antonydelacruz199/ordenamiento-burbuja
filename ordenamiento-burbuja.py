class BubbleSorter:
    def __init__(self, data):
        self.data = data

    def _swap(self, left_pos, right_pos):
        temp = self.data[left_pos]
        self.data[left_pos] = self.data[right_pos]
        self.data[right_pos] = temp

    def sort(self):
        n = len(self.data)
        for _ in range(n):
            for idx in range(n - 1):
                if self.data[idx] > self.data[idx + 1]:
                    self._swap(idx, idx + 1)
        return self.data

def usar_bubble_sort():
    numeros = [64, 34, 25, 12, 22, 11, 9, 1]
    sorter = BubbleSorter(numeros)

    print("Lista original:")
    print(numeros)

    sorter.sort()

    print("Lista ordenada:")
    print(numeros)

if __name__ == "__main__":
    usar_bubble_sort()
