import sys
from random import randrange

# setting path
sys.path.append("../")

# importing
from main import diff



# test
def test_diff():

	assert diff("123", "321") == (1, 2)
	assert diff("459", "849") == (1, 1)
	assert diff("001", "100") == (1, 2)
	assert diff("984", "321") == (0, 0)
	assert diff("649", "105") == (0, 0)
	assert diff("414", "141") == (0, 3)
	assert diff("515", "115") == (2, 1)
	assert diff("879", "879") == (3, 0)
	assert diff("648", "489") == (0, 2)
	assert diff("123", "121") == (2, 0)
