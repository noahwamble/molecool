"""
    This function tests the measure module.
"""
#imports
import molecool
import numpy as np

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
