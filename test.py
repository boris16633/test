import pytest
from new_file import my_sum

@pytest.mark.parametrize("a, b", [
    [1, 2, 3],
    ["1", "2", "12"],
    [[1], [2], [1, 2]]
])
def test_sum(a, b, sum_ab):
    ans = my_sum(a, b)
    assert ans == sum_ab