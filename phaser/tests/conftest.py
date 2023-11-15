# define pytest objects that are available in all tests!
# For example, dummy image A, B, and C
import pytest

@pytest.fixture
def shared_object():
    # This function will be called before each test that uses the 'shared_object' fixture
    list_of_files = ['test.png']
    return list_of_files