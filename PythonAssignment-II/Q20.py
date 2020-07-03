# Write a Python class to find the three elements that sum to zero from a list of n real numbers.
# Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
# Output : [[-10, 2, 8], [-7, -3, 10]]

class Realsum:
    def sum_to_zero(self, number):
        number = sorted(number)
        result = []
        i = 0
        while i < len(number) - 2:
            j, k = i + 1, len(number) - 1
            while j < k:
                if number[i] + number[j] + number[k] < 0:
                    j += 1
                elif number[i] + number[j] + number[k] > 0:
                    k -= 1
                else:
                    result.append([number[i], number[j], number[k]])
                    j ,k = j + 1, k - 1
                    while j < k and number[j] == number[j - 1]:
                        j += 1
                    while j < k and number[k] == number[k + 1]:
                        k -= 1
            i += 1
            while i < len(number) - 2 and number[i] == number[i - 1]:
                i += 1
        return result


print(Realsum().sum_to_zero([-25, -10, -7, -3, 2, 4, 8, 10]))