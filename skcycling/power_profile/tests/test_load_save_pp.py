""" Test the loading and saving using pickles. """

import os

from numpy.testing import assert_array_equal
from numpy.testing import assert_equal

from skcycling.power_profile import RidePowerProfile
from skcycling.power_profile import RecordPowerProfile


def test_save_load_ride_pp():
    """ Test the routine to save the object RidePowerProfile. """
    # Create the path to read the npy file
    currdir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(currdir, 'data', 'fit_files',
                            '2014-05-07-14-26-22.fit')

    my_ride_rpp = RidePowerProfile(max_duration_profile=1)
    my_ride_rpp.fit(filename)

    # Save the object
    store_filename = os.path.join(currdir, 'data', 'ride_rpp.p')
    my_ride_rpp.save_to_pickles(store_filename)

    # Try to load the file
    obj = RidePowerProfile(max_duration_profile=1)
    obj = obj.load_from_pickles(store_filename)

    # Check that the object have the same values
    assert_array_equal(my_ride_rpp.data_, obj.data_)
    assert_equal(my_ride_rpp.data_norm_, obj.data_norm_)
    assert_equal(my_ride_rpp.cyclist_weight_, obj.cyclist_weight_)
    assert_equal(my_ride_rpp.max_duration_profile_,
                 obj.max_duration_profile_)
    assert_equal(my_ride_rpp.date_profile_, obj.date_profile_)
    assert_equal(my_ride_rpp.filename_, obj.filename_)