import unittest
import pint
import logging
from .link_budget_test_case_dataset import LinkBudgetTestCaseDataset
from lib.calculator import LinkBudgetCalculator

class TestLinkBudget(unittest.TestCase):

    NUM_TEST_CASES = 17

    def setUp(self):
        self.ureg = pint.UnitRegistry()
        self.test_case_dataset = LinkBudgetTestCaseDataset(self.ureg)
        
    def test_iterable(self):
        count = 0
        for item in self.test_case_dataset:
            count += 1
        self.assertEqual(self.NUM_TEST_CASES, count)

    def test_len(self):
        self.assertEqual(self.NUM_TEST_CASES, len(self.test_case_dataset))

    def test_lb1(self):
        self._test_dataset_item(0)
		
    def test_lb2(self):
        self._test_dataset_item(1)
		
    def test_lb3(self):
        self._test_dataset_item(2)
		
    def test_lb4(self):
        self._test_dataset_item(3)
		
    def test_lb5(self):
        self._test_dataset_item(4)
		
    def test_lb6(self):
        self._test_dataset_item(5)
		
    def test_lb7(self):
        self._test_dataset_item(6)
		
    def test_lb8(self):
        self._test_dataset_item(7)
		
    def test_lb9(self):
        self._test_dataset_item(8)
		
    def test_lb10(self):
        self._test_dataset_item(9)
		
    def test_lb11(self):
        with self.assertRaises(ValueError):
            self._test_dataset_item(10)
		
    def test_lb12(self):
        with self.assertRaises(ValueError):
            self._test_dataset_item(11)
		
    def test_lb13(self):
        with self.assertRaises(ValueError):
            self._test_dataset_item(12)
		
    def test_lb14(self):
        self._test_dataset_item(13)
		
    def test_lb15(self):
        with self.assertRaises(ValueError):
            self._test_dataset_item(14)
		
    def test_lb16(self):
         with self.assertRaises(ValueError):
            self._test_dataset_item(15)
		
    def test_lb17(self):
        with self.assertRaises(ValueError):
            self._test_dataset_item(16)
    
    def test_default_init(self):
        lb_calc = LinkBudgetCalculator(self.ureg)
        
		# ensure default values are correct
        self.assertEqual(lb_calc.altitude_ground_station, 0 * self.ureg.meter)
        self.assertEqual(lb_calc.altitude_satellite, 0 * self.ureg.meter)
        self.assertEqual(lb_calc.orbit_elevation_angle, 0 * self.ureg.degree)
        self.assertEqual(lb_calc.downlink_frequency, 0 * self.ureg.hertz)
        self.assertEqual(lb_calc.target_energy_noise_ratio, 0)
        self.assertEqual(lb_calc.implementation_loss, 0)
        self.assertEqual(lb_calc.transmit_power, 0 * self.ureg.watt)
        self.assertEqual(lb_calc.transmit_losses, 0)
        self.assertEqual(lb_calc.transmit_antenna_gain, 0)
        self.assertEqual(lb_calc.transmit_pointing_loss, 0)
        self.assertEqual(lb_calc.polarization_losses, 0)
        self.assertEqual(lb_calc.atmospheric_loss, 0)
        self.assertEqual(lb_calc.receive_antenna_gain, 0)
        self.assertEqual(lb_calc.system_noise_figure, 0)
        self.assertEqual(lb_calc.noise_bandwidth, 0 * self.ureg.hertz)

    def _test_dataset_item(self, item_number):        
        # get the test case data
        tc_data = self.test_case_dataset[item_number]

        # make sure all of the inputs are set
        self.assertIsNotNone(tc_data.name)
        self.assertIsNotNone(tc_data.description)
        self.assertIsNotNone(tc_data.reference)
        self.assertIsNotNone(tc_data.altitude_ground_station)
        self.assertIsNotNone(tc_data.altitude_satellite)
        self.assertIsNotNone(tc_data.orbit_elevation_angle)
        self.assertIsNotNone(tc_data.downlink_frequency)
        self.assertIsNotNone(tc_data.target_energy_noise_ratio)
        self.assertIsNotNone(tc_data.implementation_loss)
        self.assertIsNotNone(tc_data.transmit_power)
        self.assertIsNotNone(tc_data.transmit_losses)
        self.assertIsNotNone(tc_data.transmit_antenna_gain)
        self.assertIsNotNone(tc_data.transmit_pointing_loss)
        self.assertIsNotNone(tc_data.polarization_losses)
        self.assertIsNotNone(tc_data.atmospheric_loss)
        self.assertIsNotNone(tc_data.receive_antenna_gain)
        self.assertIsNotNone(tc_data.receiving_pointing_loss)
        self.assertIsNotNone(tc_data.system_noise_figure)
        self.assertIsNotNone(tc_data.noise_bandwidth)

        # make sure all the expected output values are present. not testing for None because a 
        # None would be used when the test case should not be able to produce results, such as in
        # an error condition
        # intermediates also have a calculated value, and can be tested
        # intermediates
        self.assertTrue(hasattr(tc_data, 'downlink_wavelength'))
        self.assertTrue(hasattr(tc_data, 'link_distance'))
        self.assertTrue(hasattr(tc_data, 'required_ebno'))
        self.assertTrue(hasattr(tc_data, 'transmit_power_dBm'))
        self.assertTrue(hasattr(tc_data, 'transmit_eirp'))
        self.assertTrue(hasattr(tc_data, 'downlink_path_loss'))
        # outputs
        self.assertTrue(hasattr(tc_data, 'received_power'))
        self.assertTrue(hasattr(tc_data, 'minimum_detectable_signal'))
        self.assertTrue(hasattr(tc_data, 'energy_noise_ratio'))
        self.assertTrue(hasattr(tc_data, 'link_margin'))
        
        # create the calculator
        lb_calc = LinkBudgetCalculator(self.ureg)
        
        # load the data
        lb_calc.altitude_ground_station   = tc_data.altitude_ground_station
        lb_calc.altitude_satellite        = tc_data.altitude_satellite
        lb_calc.orbit_elevation_angle     = tc_data.orbit_elevation_angle
        lb_calc.downlink_frequency        = tc_data.downlink_frequency
        lb_calc.target_energy_noise_ratio = tc_data.target_energy_noise_ratio
        lb_calc.implementation_loss       = tc_data.implementation_loss
        lb_calc.transmit_power            = tc_data.transmit_power
        lb_calc.transmit_losses           = tc_data.transmit_losses
        lb_calc.transmit_antenna_gain     = tc_data.transmit_antenna_gain
        lb_calc.transmit_pointing_loss    = tc_data.transmit_pointing_loss
        lb_calc.polarization_losses       = tc_data.polarization_losses
        lb_calc.atmospheric_loss          = tc_data.atmospheric_loss
        lb_calc.receive_antenna_gain      = tc_data.receive_antenna_gain
        lb_calc.receiving_pointing_loss   = tc_data.receiving_pointing_loss
        lb_calc.system_noise_figure       = tc_data.system_noise_figure
        lb_calc.noise_bandwidth           = tc_data.noise_bandwidth
        
        # test for equality
        self.assertEqual(lb_calc.altitude_ground_station, tc_data.altitude_ground_station)
        self.assertEqual(lb_calc.altitude_satellite, tc_data.altitude_satellite)
        self.assertEqual(lb_calc.orbit_elevation_angle, tc_data.orbit_elevation_angle)
        self.assertEqual(lb_calc.downlink_frequency, tc_data.downlink_frequency)
        self.assertEqual(lb_calc.target_energy_noise_ratio, tc_data.target_energy_noise_ratio)
        self.assertEqual(lb_calc.implementation_loss, tc_data.implementation_loss)
        self.assertEqual(lb_calc.transmit_power, tc_data.transmit_power)
        self.assertEqual(lb_calc.transmit_losses, tc_data.transmit_losses)
        self.assertEqual(lb_calc.transmit_antenna_gain, tc_data.transmit_antenna_gain)
        self.assertEqual(lb_calc.transmit_pointing_loss, tc_data.transmit_pointing_loss)
        self.assertEqual(lb_calc.polarization_losses, tc_data.polarization_losses)
        self.assertEqual(lb_calc.atmospheric_loss, tc_data.atmospheric_loss)
        self.assertEqual(lb_calc.receive_antenna_gain, tc_data.receive_antenna_gain)
        self.assertEqual(lb_calc.system_noise_figure, tc_data.system_noise_figure)
        self.assertEqual(lb_calc.noise_bandwidth, tc_data.noise_bandwidth)
        
        # turn logging off for now
        logging.basicConfig(level=logging.INFO)
		
        # run the calculations
        lb_calc.run()
        
        # test that the output is valid
        self.assertEqual(lb_calc.is_valid, True)
        
        # test for equality
        self.assertAlmostEqual(lb_calc.downlink_wavelength.magnitude, tc_data.downlink_wavelength.magnitude, 3)
        self.assertAlmostEqual(lb_calc.link_distance.magnitude, tc_data.link_distance.magnitude, -2)
        self.assertAlmostEqual(lb_calc.required_ebno, tc_data.required_ebno, 1)
        self.assertAlmostEqual(lb_calc.transmit_power_dBm, tc_data.transmit_power_dBm, 1)
        self.assertAlmostEqual(lb_calc.transmit_eirp, tc_data.transmit_eirp, 1)
        self.assertAlmostEqual(lb_calc.downlink_path_loss, tc_data.downlink_path_loss, -1)
        self.assertAlmostEqual(lb_calc.received_power, tc_data.received_power, -2)
        self.assertAlmostEqual(lb_calc.minimum_detectable_signal, tc_data.minimum_detectable_signal, 0)
        self.assertAlmostEqual(lb_calc.energy_noise_ratio, tc_data.energy_noise_ratio, 0)
        self.assertAlmostEqual(lb_calc.link_margin, tc_data.link_margin, 1)
		
if __name__ == '__main__':
    unittest.main()