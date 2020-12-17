"""
    This function tests the measure module.
"""
#imports
import molecool
import numpy as np
import pytest

#test the calculate_distance function
def test_calculate_distance():
    """
        This function will test calculate_distance and ensure that it is doing what
        I expect.
    """
    #define two points
    r1= np.array([0,0,0])
    r2= np.array([0,1,0])

    #define expected value
    expected= 1
    calculated_distance= molecool.calculate_distance(r1,r2)

    #now perform the test
    assert calculated_distance == expected

def test_calculate_angle():
   """Test the calculate_angle function"""

   r1 = np.array([1, 0, 0])
   r2 = np.array([0, 0, 0])
   r3 = np.array([0, 1, 0])

   expected_value = 90

   calculated_value = molecool.calculate_angle(r1, r2, r3, degrees=True)
   assert expected_value == calculated_value

def test_molecular_mass():
    symbols = ['C', 'H', 'H', 'H', 'H']

    calculated_mass = molecool.calculate_molecular_mass(symbols)

    actual_mass = 16.04

    assert pytest.approx(actual_mass, abs=1e-2) == calculated_mass

@pytest.mark.parametrize("p1, p2, p3, expected_angle",[
    (np.array([np.sqrt(2)/2, np.sqrt(2)/2, 0]), np.array([0,0,0]), np.array([1,0,0]), 45),
    (np.array([0,0,-1]), np.array([0,1,0]), np.array([1,0,0]), 60)

])
def test_calculate_angle_many(p1,p2,p3,expected_angle):
    """
        Calculated
    """
    calculated_value= molecool.calculate_angle(p1,p2,p3, degrees=True)

    assert pytest.approx(expected_angle) == calculated_value
