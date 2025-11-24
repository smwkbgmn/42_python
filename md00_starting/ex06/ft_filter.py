from typing import Callable, Iterable, List, TypeVar

T = TypeVar('T')


def filter(predicate: Callable[[T], bool], iterable: Iterable[T]) -> List[T]:
    """
    EAGER VERSION (IMMEDIATE EVALUATION) USING LIST COMPREHENSION
    Return a list of those items of iterable for which predicate(item) is true.
    If predicate is None, return the items that are true.

    :param predicate: Description
    :type predicate: Callable[[T], bool]
    :param iterable: Description
    :type iterable: Iterable[T]
    :return: Description
    :rtype: List[T]
    """
    return [element for element in iterable if predicate(element)]


# It works like below c++ code

# template<typename T>
# std::vector<T> ft_filter(std::function<bool(T)> predicate,
#                          std::vector<T> iterable) {
#     std::vector<T> result;
#     for (const auto& element : iterable) {
#         if (predicate(element)) {
#             result.push_back(element);
#         }
#     }
#     return result;
# }

# YILED VERSION (LAZY EVALUATION)
# def ft_filter(predicate: Callable[[T], bool], iterable: Iterable[T]) -> Iterator[T]:
#     for element in iterable:
#         if predicate(element):
#             yield element
