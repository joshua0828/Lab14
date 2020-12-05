# test_retirement_age.py
import pytest
from retirement import *

#def test_valid_birth_month_and_year:
    #assert calculate_retirement_date(1937, 3, )

# scenario 1

#Scenario: Valid Birth month and year

#Given: the input information of the user in PyCharm

#When: birth month between 1 - 12 is entered

#And: birth year is between 1937 to present

#Then: The results of full retirements age and year is shown.


@pytest.mark.parametrize("input_year,expected_year,expected_month", [(1939, 65,4), (1940, 65, 6), (1941, 65, 8)])
def test_parameterized_year(input_year,expected_year,expected_month):
    assert calculate_retirement_age(input_year) == (expected_year, expected_month)


# scenario 2
#Scenario: test birth year 1939

#Given: the birth year and birth month of the user.

#When: the birth month and birth year is entered between 1939 and prior.

#Then: The results of the full retirement age of the user is shown which will be at the age of 65
# and it will also show the year and the month in which they will retire.

@pytest.mark.parametrize("birth_year, birth_month, age_years, age_months, expected_year, expected_month",
                         [(1938, 1, 66,0, 2004, 1), (1939, 2, 65, 4, 2004, 6)])
def test_parameterized_date(birth_year, birth_month, age_years, age_months, expected_year, expected_month):
    assert calculate_retirement_date(birth_year, birth_month, age_years, age_months) == (expected_year, expected_month)

