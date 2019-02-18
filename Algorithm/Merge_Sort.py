# Merge sort in python:  O(n log(n))
class solution():

    def mergeSort(self,arr):
        if len(arr) > 1:
            left,right=0,len(arr)

            mid = left+(right-left)//2  # Finding the mid of the array
            L = arr[:mid]  # Dividing the array elements
            R = arr[mid:]  # into 2 halves


            self.mergeSort(L)  # Sorting the first half
            self.mergeSort(R)  # Sorting the second half

            i = j = k = 0

            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            # Checking if any element was left
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

        return arr


test=[5,8,6,3]
print(solution().mergeSort(test))


