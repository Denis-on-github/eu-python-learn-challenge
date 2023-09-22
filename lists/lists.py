class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.

        :param input_list: Исходный список
        :return: Список с замененными элементами
        """

        if not input_list:
            return []

        max_value = input_list[0]
        for x in input_list:
            if x > max_value:
                max_value = x

        final_list = [max_value if x > 0 else x for x in input_list]

        return final_list

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента

        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """
        left = 0
        right = len(input_list) - 1

        def binary_search(left: int, right: int) -> int:
            if left <= right:
                mid = (left + right) // 2
                if input_list[mid] == query:
                    return mid
                elif input_list[mid] < query:
                    return binary_search(mid + 1, right)
                else:
                    return binary_search(left, mid - 1)
            else:
                return -1

        return binary_search(left, right)
