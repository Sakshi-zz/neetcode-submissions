from typing import List

class Solution:
    def insertionSort(self, pairs: List['Pair']) -> List[List['Pair']]:
        if not pairs:
            return []

        arr = pairs[:]
        states = [arr[:]]        # initial state

        for i in range(1, len(arr)):
            current = arr[i]
            j = i - 1

            while j >= 0 and arr[j].key > current.key:
                arr[j + 1] = arr[j]
                j -= 1

            arr[j + 1] = current
            states.append(arr[:])

        return states