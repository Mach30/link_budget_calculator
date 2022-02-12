from pint import UnitRegistry

class LinkBudgetTestCaseDataset():

    def __init__(self, ureg):
        """
        Constructor for GS Mk3 link budget test case dataset
        
        The constructor will initialize values of multiple test cases described
        in the documentation.
        
        """
        self._ureg = ureg
        
        ## populatng data without using the LinkBudget class so that any errors with the class,
        ## or any of its methods, will be uncovered during test execution and not during dataset
        ## initialization

        self._datatable = []

		# ---------------------------------------------------------------------------------------
        # ------------------------------ first test case ----------------------------------------
		# ---------------------------------------------------------------------------------------
        data = self._Data()
        data.name = 'NOAA Weather Satellite'
        data.description = 'Standard link budget for the groundsphere Mk 3 setup. Includes      ' \
            'values for eggbeater antenna, NOAA 19 weather satellite, inclined orbit, and ' \
            '137.5 MHz APT data. Used as target link budget calculation.' \
            'Developed by Mach 30 team using known, researched system values. '
        data.reference = 'https://www.wmo-sat.info/oscar/satellites/view/341'
        # inputs
        data.altitude_ground_station = 400 * ureg.meter     # m
        data.altitude_satellite = 860 * ureg.kilometer      # km
        data.orbit_elevation_angle = 25 * ureg.degree       # deg
        data.downlink_frequency = 137.5 * ureg.megahertz    # Hz
        data.target_energy_noise_ratio = 20.0               # dB
        data.implementation_loss = -1.0                     # dB
        data.transmit_power = 5.0 * ureg.watt               # Watt
        data.transmit_losses = -1.0                         # dB 
        data.transmit_antenna_gain = 4.0                    # dB
        data.transmit_pointing_loss = -3.0                  # dB
        data.polarization_losses = 0.0                      # dB
        data.atmospheric_loss = -0.75                       # dB
        data.receive_antenna_gain = 5.4                     # dB
        data.receiving_pointing_loss = -3.0                 # dB 
        data.system_noise_figure = 5.0                      # dB
        data.noise_bandwidth = 34.0 * ureg.kilohertz        # Hz
        # intermediates
        data.downlink_wavelength = 2.180 * ureg.meter       # m
        data.link_distance = 1700 * ureg.kilometer          # km
        data.required_ebno = 21.0                           # dB
        data.transmit_power_dBm = 37.0                      # dBm
        data.transmit_eirp = 37.0                           # dBm
        data.downlink_path_loss = -140                      # dB
        # outputs
        data.received_power = -100                          # dBm
        data.minimum_detectable_signal = -124               # dBm
        data.energy_noise_ratio = 23                        # dB
        data.link_margin = 1.7                              # dB
        # add it to the data table
        self._datatable.append(data)
		
		# ---------------------------------------------------------------------------------------
        # ------------------------------ second test case ---------------------------------------
		# ---------------------------------------------------------------------------------------
        data = self._Data()
        data.name = 'Ground Sphere Mk. 3 High Elevation Angle'
        data.description = 'Modified link budget for the groundsphere Mk 3 setup with high elevation angle. Includes      ' \
            'values for eggbeater antenna, NOAA 19 weather satellite, inclined orbit, and ' \
            '137.5 MHz APT data. Used as target link budget calculation.' \
            'Developed by Mach 30 team using known, researched system values. '
        data.reference = 'https://www.wmo-sat.info/oscar/satellites/view/341'
        # inputs
        data.altitude_ground_station = 400 * ureg.meter     # m
        data.altitude_satellite = 860 * ureg.kilometer      # km
        data.orbit_elevation_angle = 90 * ureg.degree       # deg
        data.downlink_frequency = 137.5 * ureg.megahertz    # Hz
        data.target_energy_noise_ratio = 20.0               # dB
        data.implementation_loss = -1.0                     # dB
        data.transmit_power = 5.0 * ureg.watt               # Watt
        data.transmit_losses = -1.0                         # dB 
        data.transmit_antenna_gain = 4.0                    # dB
        data.transmit_pointing_loss = -3.0                  # dB
        data.polarization_losses = 0.0                      # dB
        data.atmospheric_loss = 0.0                         # dB
        data.receive_antenna_gain = 5.4                     # dB
        data.receiving_pointing_loss = 0.0                  # dB 
        data.system_noise_figure = 5.0                      # dB
        data.noise_bandwidth = 34.0 * ureg.kilohertz        # Hz
        # intermediates
        data.downlink_wavelength = 2.180 * ureg.meter       # m
        data.link_distance = 860 * ureg.kilometer           # km
        data.required_ebno = 21.0                           # dB
        data.transmit_power_dBm = 37.0                      # dBm
        data.transmit_eirp = 37.0                           # dBm
        data.downlink_path_loss = -130                      # dB
        # outputs
        data.received_power = -100                          # dBm
        data.minimum_detectable_signal = -124               # dBm
        data.energy_noise_ratio = 32                        # dB
        data.link_margin = 11.2                             # dB
        # add it to the data table
        self._datatable.append(data)
		
		# ---------------------------------------------------------------------------------------
        # ------------------------------ third test case ----------------------------------------
		# ---------------------------------------------------------------------------------------
        data = self._Data()
        data.name = 'Ground Sphere Mk. 3 Low Elevation Angle'
        data.description = 'Modified link budget for the groundsphere Mk 3 setup with low elevation angle. Includes      ' \
            'values for eggbeater antenna, NOAA 19 weather satellite, inclined orbit, and ' \
            '137.5 MHz APT data. Used as target link budget calculation.' \
            'Developed by Mach 30 team using known, researched system values. '
        data.reference = 'https://www.wmo-sat.info/oscar/satellites/view/341'
        # inputs
        data.altitude_ground_station = 400 * ureg.meter     # m
        data.altitude_satellite = 860 * ureg.kilometer      # km
        data.orbit_elevation_angle =  5 * ureg.degree       # deg
        data.downlink_frequency = 137.5 * ureg.megahertz    # Hz
        data.target_energy_noise_ratio = 20.0               # dB
        data.implementation_loss = -1.0                     # dB
        data.transmit_power = 5.0 * ureg.watt               # Watt
        data.transmit_losses = -1.0                         # dB 
        data.transmit_antenna_gain = 4.0                    # dB
        data.transmit_pointing_loss = -6.0                  # dB
        data.polarization_losses = 0.0                      # dB
        data.atmospheric_loss = -2.1                        # dB
        data.receive_antenna_gain = 5.4                     # dB
        data.receiving_pointing_loss = -3.0                 # dB 
        data.system_noise_figure = 5.0                      # dB
        data.noise_bandwidth = 34.0 * ureg.kilohertz        # Hz
        # intermediates
        data.downlink_wavelength = 2.180 * ureg.meter       # m
        data.link_distance = 2900 * ureg.kilometer          # km
        data.required_ebno = 21.0                           # dB
        data.transmit_power_dBm = 37.0                      # dBm
        data.transmit_eirp = 34.0                           # dBm
        data.downlink_path_loss = -140                      # dB
        # outputs
        data.received_power = -110                          # dBm
        data.minimum_detectable_signal = -124               # dBm
        data.energy_noise_ratio = 13                        # dB
        data.link_margin = -7.5                             # dB
        # add it to the data table
        self._datatable.append(data)
		
		# ---------------------------------------------------------------------------------------
        # ------------------------------ fourth test case ---------------------------------------
		# ---------------------------------------------------------------------------------------
        data = self._Data()
        data.name = 'Ground Sphere Mk. 3 High Gain Antenna with Tracking'
        data.description = 'Modified link budget for the groundsphere Mk 3 setup with high elevation angle. Includes      ' \
            'values for eggbeater antenna, NOAA 19 weather satellite, inclined orbit, and ' \
            '137.5 MHz APT data. Used as target link budget calculation.' \
            'Developed by Mach 30 team using known, researched system values. '
        data.reference = 'https://www.wmo-sat.info/oscar/satellites/view/341'
        # inputs
        data.altitude_ground_station = 400 * ureg.meter     # m
        data.altitude_satellite = 860 * ureg.kilometer      # km
        data.orbit_elevation_angle = 45 * ureg.degree       # deg
        data.downlink_frequency = 137.5 * ureg.megahertz    # Hz
        data.target_energy_noise_ratio = 20.0               # dB
        data.implementation_loss = -1.0                     # dB
        data.transmit_power = 5.0 * ureg.watt               # Watt
        data.transmit_losses = -1.0                         # dB 
        data.transmit_antenna_gain = 4.0                    # dB
        data.transmit_pointing_loss = -3.0                  # dB
        data.polarization_losses = 0.0                      # dB
        data.atmospheric_loss = -0.3                        # dB
        data.receive_antenna_gain = 24                      # dB
        data.receiving_pointing_loss = 0.0                 # dB 
        data.system_noise_figure = 5.0                      # dB
        data.noise_bandwidth = 34.0 * ureg.kilohertz        # Hz
        # intermediates
        data.downlink_wavelength = 2.180 * ureg.meter       # m
        data.link_distance = 1200 * ureg.kilometer          # km
        data.required_ebno = 21.0                           # dB
        data.transmit_power_dBm = 37.0                      # dBm
        data.transmit_eirp = 37.0                           # dBm
        data.downlink_path_loss = -140                      # dB
        # outputs
        data.received_power = -80                           # dBm
        data.minimum_detectable_signal = -124               # dBm
        data.energy_noise_ratio = 48                        # dB
        data.link_margin = 26.9                             # dB
        # add it to the data table
        self._datatable.append(data)
		
		# ---------------------------------------------------------------------------------------
        # ------------------------------ fifth test case ---------------------------------------
		# ---------------------------------------------------------------------------------------
        data = self._Data()
        data.name = 'Ground Sphere Mk. 3 High Gain antenna no tracking'
        data.description = 'Modified link budget for the groundsphere Mk 3 setup with high elevation angle. Includes      ' \
            'values for eggbeater antenna, NOAA 19 weather satellite, inclined orbit, and ' \
            '137.5 MHz APT data. Used as target link budget calculation.' \
            'Developed by Mach 30 team using known, researched system values. '
        data.reference = 'https://www.wmo-sat.info/oscar/satellites/view/341'
        # inputs
        data.altitude_ground_station = 400 * ureg.meter     # m
        data.altitude_satellite = 860 * ureg.kilometer      # km
        data.orbit_elevation_angle = 45 * ureg.degree       # deg
        data.downlink_frequency = 137.5 * ureg.megahertz    # Hz
        data.target_energy_noise_ratio = 20.0               # dB
        data.implementation_loss = -1.0                     # dB
        data.transmit_power = 5.0 * ureg.watt               # Watt
        data.transmit_losses = -1.0                         # dB 
        data.transmit_antenna_gain = 4.0                    # dB
        data.transmit_pointing_loss = -3.0                  # dB
        data.polarization_losses = 0.0                      # dB
        data.atmospheric_loss = -0.3                        # dB
        data.receive_antenna_gain = 24                      # dB
        data.receiving_pointing_loss = -30                  # dB 
        data.system_noise_figure = 5.0                      # dB
        data.noise_bandwidth = 34.0 * ureg.kilohertz        # Hz
        # intermediates
        data.downlink_wavelength = 2.180 * ureg.meter       # m
        data.link_distance = 1200 * ureg.kilometer          # km
        data.required_ebno = 21.0                           # dB
        data.transmit_power_dBm = 37.0                      # dBm
        data.transmit_eirp = 37.0                           # dBm
        data.downlink_path_loss = -140                      # dB
        # outputs
        data.received_power = -110                          # dBm
        data.minimum_detectable_signal = -124               # dBm
        data.energy_noise_ratio = 18                        # dB
        data.link_margin = -3.1                             # dB
        # add it to the data table
        self._datatable.append(data)
		
		# ---------------------------------------------------------------------------------------
        # ------------------------------ sixth test case ---------------------------------------
		# ---------------------------------------------------------------------------------------
        data = self._Data()
        data.name = 'Ground Sphere Mk. 3 Ground Plane Dipole Low Elevation Angle'
        data.description = 'Modified link budget for the groundsphere Mk 3 setup with high elevation angle. Includes      ' \
            'values for eggbeater antenna, NOAA 19 weather satellite, inclined orbit, and ' \
            '137.5 MHz APT data. Used as target link budget calculation.' \
            'Developed by Mach 30 team using known, researched system values. '
        data.reference = 'https://www.wmo-sat.info/oscar/satellites/view/341'
        # inputs
        data.altitude_ground_station = 400 * ureg.meter     # m
        data.altitude_satellite = 860 * ureg.kilometer      # km
        data.orbit_elevation_angle = 25 * ureg.degree       # deg
        data.downlink_frequency = 137.5 * ureg.megahertz    # Hz
        data.target_energy_noise_ratio = 20.0               # dB
        data.implementation_loss = -1.0                     # dB
        data.transmit_power = 5.0 * ureg.watt               # Watt
        data.transmit_losses = -1.0                         # dB 
        data.transmit_antenna_gain = 4.0                    # dB
        data.transmit_pointing_loss = -3.0                  # dB
        data.polarization_losses = -3.0                     # dB
        data.atmospheric_loss = -0.75                       # dB
        data.receive_antenna_gain = 2.1                     # dB
        data.receiving_pointing_loss = 0.0                  # dB 
        data.system_noise_figure = 5.0                      # dB
        data.noise_bandwidth = 34.0 * ureg.kilohertz        # Hz
        # intermediates
        data.downlink_wavelength = 2.180 * ureg.meter       # m
        data.link_distance = 1700 * ureg.kilometer          # km
        data.required_ebno = 21.0                           # dB
        data.transmit_power_dBm = 37.0                      # dBm
        data.transmit_eirp = 37.0                           # dBm
        data.downlink_path_loss = -140                      # dB
        # outputs
        data.received_power = -100                          # dBm
        data.minimum_detectable_signal = -124               # dBm
        data.energy_noise_ratio = 19                        # dB
        data.link_margin = -1.6                             # dB
        # add it to the data table
        self._datatable.append(data)
		
		# ---------------------------------------------------------------------------------------
        # ------------------------------ seventh test case --------------------------------------
		# ---------------------------------------------------------------------------------------
        data = self._Data()
        data.name = 'Ground Sphere Mk. 3 Ground Plane Dipole High Elevation Angle'
        data.description = 'Modified link budget for the groundsphere Mk 3 setup with high elevation angle. Includes      ' \
            'values for eggbeater antenna, NOAA 19 weather satellite, inclined orbit, and ' \
            '137.5 MHz APT data. Used as target link budget calculation.' \
            'Developed by Mach 30 team using known, researched system values. '
        data.reference = 'https://www.wmo-sat.info/oscar/satellites/view/341'
        # inputs
        data.altitude_ground_station = 400 * ureg.meter     # m
        data.altitude_satellite = 860 * ureg.kilometer      # km
        data.orbit_elevation_angle = 90 * ureg.degree       # deg
        data.downlink_frequency = 137.5 * ureg.megahertz    # Hz
        data.target_energy_noise_ratio = 20.0               # dB
        data.implementation_loss = -1.0                     # dB
        data.transmit_power = 5.0 * ureg.watt               # Watt
        data.transmit_losses = -1.0                         # dB 
        data.transmit_antenna_gain = 4.0                    # dB
        data.transmit_pointing_loss = -3.0                  # dB
        data.polarization_losses = -3.0                     # dB
        data.atmospheric_loss = 0.0                         # dB
        data.receive_antenna_gain = 2.1                     # dB
        data.receiving_pointing_loss = -12.0                # dB 
        data.system_noise_figure = 5.0                      # dB
        data.noise_bandwidth = 34.0 * ureg.kilohertz        # Hz
        # intermediates
        data.downlink_wavelength = 2.180 * ureg.meter       # m
        data.link_distance = 860 * ureg.kilometer           # km
        data.required_ebno = 21.0                           # dB
        data.transmit_power_dBm = 37.0                      # dBm
        data.transmit_eirp = 37.0                           # dBm
        data.downlink_path_loss = -130                      # dB
        # outputs
        data.received_power = -106                          # dBm
        data.minimum_detectable_signal = -124               # dBm
        data.energy_noise_ratio = 14                        # dB
        data.link_margin = -7.1                             # dB
        # add it to the data table
        self._datatable.append(data)
		
		# ---------------------------------------------------------------------------------------
        # ------------------------------ eigth test case --------------------------------------
		# ---------------------------------------------------------------------------------------
        data = self._Data()
        data.name = 'AMSAT IARU Link Budget'
        data.description = 'Modified link budget for the groundsphere Mk 3 setup with high elevation angle. Includes      ' \
            'values for eggbeater antenna, NOAA 19 weather satellite, inclined orbit, and ' \
            '137.5 MHz APT data. Used as target link budget calculation.' \
            'Developed by Mach 30 team using known, researched system values. '
        data.reference = 'https://www.wmo-sat.info/oscar/satellites/view/341'
        # inputs
        data.altitude_ground_station = 400 * ureg.meter     # m
        data.altitude_satellite = 800 * ureg.kilometer      # km
        data.orbit_elevation_angle = 5 * ureg.degree       # deg
        data.downlink_frequency = 437.45 * ureg.megahertz    # Hz
        data.target_energy_noise_ratio = 18.0               # dB
        data.implementation_loss = 0                     # dB
        data.transmit_power = 3.0 * ureg.watt               # Watt
        data.transmit_losses = -1.0                         # dB 
        data.transmit_antenna_gain = 2.0                    # dB
        data.transmit_pointing_loss = 0.0                  # dB
        data.polarization_losses = 0                     # dB
        data.atmospheric_loss = -2.4                         # dB
        data.receive_antenna_gain = 13.5                     # dB
        data.receiving_pointing_loss = -2.0                # dB 
        data.system_noise_figure = 2.9                    # dB
        data.noise_bandwidth = 10 * ureg.kilohertz        # Hz
        # intermediates
        data.downlink_wavelength = 0.685 * ureg.meter       # m
        data.link_distance = 2780 * ureg.kilometer           # km
        data.required_ebno = 18.0                           # dB
        data.transmit_power_dBm = 34.8                      # dBm
        data.transmit_eirp = 35.8                           # dBm
        data.downlink_path_loss = -154                      # dB
        # outputs
        data.received_power = -113                          # dBm
        data.minimum_detectable_signal = -131               # dBm
        data.energy_noise_ratio = 22                        # dB
        data.link_margin = 3.8                             # dB
        # add it to the data table
        self._datatable.append(data)
        		
		# ---------------------------------------------------------------------------------------
        # ------------------------------ ninth test case --------------------------------------
		# ---------------------------------------------------------------------------------------
        data = self._Data()
        data.name = 'Cornell KickSat Link Budget'
        data.description = 'Modified link budget for the groundsphere Mk 3 setup with high elevation angle. Includes      ' \
            'values for eggbeater antenna, NOAA 19 weather satellite, inclined orbit, and ' \
            '137.5 MHz APT data. Used as target link budget calculation.' \
            'Developed by Mach 30 team using known, researched system values. '
        data.reference = 'https://www.wmo-sat.info/oscar/satellites/view/341'
        # inputs
        data.altitude_ground_station = 400 * ureg.meter     # m
        data.altitude_satellite = 845 * ureg.kilometer      # km
        data.orbit_elevation_angle = 60 * ureg.degree       # deg
        data.downlink_frequency = 138 * ureg.megahertz    # Hz
        data.target_energy_noise_ratio = 10.0               # dB
        data.implementation_loss = 0                     # dB
        data.transmit_power = 5.0 * ureg.watt               # Watt
        data.transmit_losses = 0                         # dB 
        data.transmit_antenna_gain = 3.0                    # dB
        data.transmit_pointing_loss = -0.5                  # dB
        data.polarization_losses = -3.0                     # dB
        data.atmospheric_loss = -0.8                         # dB
        data.receive_antenna_gain = 5.3                     # dB
        data.receiving_pointing_loss = 0                # dB 
        data.system_noise_figure = 3.5                      # dB
        data.noise_bandwidth = 17.0 * ureg.kilohertz        # Hz
        # intermediates
        data.downlink_wavelength = 2.172 * ureg.meter       # m
        data.link_distance = 960 * ureg.kilometer           # km
        data.required_ebno = 10.0                           # dB
        data.transmit_power_dBm = 37.0                      # dBm
        data.transmit_eirp = 39.5                           # dBm
        data.downlink_path_loss = -135                      # dB
        # outputs
        data.received_power = -93                          # dBm
        data.minimum_detectable_signal = -128               # dBm
        data.energy_noise_ratio = 34                        # dB
        data.link_margin = 24.3                             # dB
        # add it to the data table
        self._datatable.append(data)
        		
		# ---------------------------------------------------------------------------------------
        # ------------------------------ tenth test case --------------------------------------
		# ---------------------------------------------------------------------------------------
        data = self._Data()
        data.name = 'GPS Link Budget'
        data.description = 'Modified link budget for the groundsphere Mk 3 setup with high elevation angle. Includes      ' \
            'values for eggbeater antenna, NOAA 19 weather satellite, inclined orbit, and ' \
            '137.5 MHz APT data. Used as target link budget calculation.' \
            'Developed by Mach 30 team using known, researched system values. '
        data.reference = 'https://www.wmo-sat.info/oscar/satellites/view/341'
        # inputs
        data.altitude_ground_station = 400 * ureg.meter     # m
        data.altitude_satellite = 20200 * ureg.kilometer      # km
        data.orbit_elevation_angle = 90 * ureg.degree       # deg
        data.downlink_frequency = 1575.42 * ureg.megahertz    # Hz
        data.target_energy_noise_ratio = 25.0               # dB
        data.implementation_loss = 0                     # dB
        data.transmit_power = 25.6 * ureg.watt               # Watt
        data.transmit_losses = -1.0                         # dB 
        data.transmit_antenna_gain = 13.0                    # dB
        data.transmit_pointing_loss = 0                  # dB
        data.polarization_losses = 0                     # dB
        data.atmospheric_loss = -3.0                         # dB
        data.receive_antenna_gain = 15                     # dB
        data.receiving_pointing_loss = -2.0                # dB 
        data.system_noise_figure = 3.0                      # dB
        data.noise_bandwidth = 1023.0 * ureg.kilohertz        # Hz
        # intermediates
        data.downlink_wavelength = 0.190 * ureg.meter       # m
        data.link_distance = 20200 * ureg.kilometer           # km
        data.required_ebno = 25.0                           # dB
        data.transmit_power_dBm = 44.1                      # dBm
        data.transmit_eirp = 56.1                           # dBm
        data.downlink_path_loss = -183                      # dB
        # outputs
        data.received_power = -117                          # dBm
        data.minimum_detectable_signal = -111              # dBm
        data.energy_noise_ratio = -6                        # dB
        data.link_margin = -30.5                              # dB
        # add it to the data table
        self._datatable.append(data)
        		
		# ---------------------------------------------------------------------------------------
        # ------------------------------ eleventh test case --------------------------------------
		# ---------------------------------------------------------------------------------------
        data = self._Data()
        data.name = 'GS Mk. 3 Unrealistic Elevation Angle'
        data.description = 'Modified link budget for the groundsphere Mk 3 setup with high elevation angle. Includes      ' \
            'values for eggbeater antenna, NOAA 19 weather satellite, inclined orbit, and ' \
            '137.5 MHz APT data. Used as target link budget calculation.' \
            'Developed by Mach 30 team using known, researched system values. '
        data.reference = 'https://www.wmo-sat.info/oscar/satellites/view/341'
        # inputs
        data.altitude_ground_station = 400 * ureg.meter     # m
        data.altitude_satellite = 860 * ureg.kilometer      # km
        data.orbit_elevation_angle = -10 * ureg.degree       # deg
        data.downlink_frequency = 137.5 * ureg.megahertz    # Hz
        data.target_energy_noise_ratio = 20.0               # dB
        data.implementation_loss = -1.0                     # dB
        data.transmit_power = 5.0 * ureg.watt               # Watt
        data.transmit_losses = -1.0                         # dB 
        data.transmit_antenna_gain = 4.0                    # dB
        data.transmit_pointing_loss = -3.0                  # dB
        data.polarization_losses = -3.0                     # dB
        data.atmospheric_loss = 0.0                         # dB
        data.receive_antenna_gain = 5.4                     # dB
        data.receiving_pointing_loss = -9.0                # dB 
        data.system_noise_figure = 5.0                      # dB
        data.noise_bandwidth = 34.0 * ureg.kilohertz        # Hz
        # intermediates
        data.downlink_wavelength = 2.180 * ureg.meter       # m
        data.link_distance = 4700 * ureg.kilometer           # km
        data.required_ebno = 21.0                           # dB
        data.transmit_power_dBm = 37.0                      # dBm
        data.transmit_eirp = 37.0                           # dBm
        data.downlink_path_loss = -150                      # dB
        # outputs
        data.received_power = 0                         # dBm
        data.minimum_detectable_signal = -124               # dBm
        data.energy_noise_ratio = 0                        # dB
        data.link_margin = 0                            # dB
        # add it to the data table
        self._datatable.append(data)
        		
		# ---------------------------------------------------------------------------------------
        # ------------------------------ twelfth test case --------------------------------------
		# ---------------------------------------------------------------------------------------
        data = self._Data()
        data.name = 'GS Mk. 3 Unrealistic Frequency'
        data.description = 'Modified link budget for the groundsphere Mk 3 setup with high elevation angle. Includes      ' \
            'values for eggbeater antenna, NOAA 19 weather satellite, inclined orbit, and ' \
            '137.5 MHz APT data. Used as target link budget calculation.' \
            'Developed by Mach 30 team using known, researched system values. '
        data.reference = 'https://www.wmo-sat.info/oscar/satellites/view/341'
        # inputs
        data.altitude_ground_station = 400 * ureg.meter     # m
        data.altitude_satellite = 860 * ureg.kilometer      # km
        data.orbit_elevation_angle = 90 * ureg.degree       # deg
        data.downlink_frequency = 0 * ureg.megahertz    # Hz
        data.target_energy_noise_ratio = 20.0               # dB
        data.implementation_loss = -1.0                     # dB
        data.transmit_power = 5.0 * ureg.watt               # Watt
        data.transmit_losses = -1.0                         # dB 
        data.transmit_antenna_gain = 4.0                    # dB
        data.transmit_pointing_loss = -3.0                  # dB
        data.polarization_losses = -3.0                     # dB
        data.atmospheric_loss = 0.0                         # dB
        data.receive_antenna_gain = 5.4                     # dB
        data.receiving_pointing_loss = 0                # dB 
        data.system_noise_figure = 5.0                      # dB
        data.noise_bandwidth = 34.0 * ureg.kilohertz        # Hz
        # intermediates
        data.downlink_wavelength = 0 * ureg.meter       # m
        data.link_distance = 860 * ureg.kilometer           # km
        data.required_ebno = 21.0                           # dB
        data.transmit_power_dBm = 37.0                      # dBm
        data.transmit_eirp = 37.0                           # dBm
        data.downlink_path_loss = -150                      # dB
        # outputs
        data.received_power = 0                          # dBm
        data.minimum_detectable_signal = -124               # dBm
        data.energy_noise_ratio = 0                        # dB
        data.link_margin = 0                            # dB
        # add it to the data table
        self._datatable.append(data)
        		
		# ---------------------------------------------------------------------------------------
        # ------------------------------ thirteenth test case --------------------------------------
		# ---------------------------------------------------------------------------------------
        data = self._Data()
        data.name = 'GS Mk. 3 Unrealistic Loss Values'
        data.description = 'Modified link budget for the groundsphere Mk 3 setup with high elevation angle. Includes      ' \
            'values for eggbeater antenna, NOAA 19 weather satellite, inclined orbit, and ' \
            '137.5 MHz APT data. Used as target link budget calculation.' \
            'Developed by Mach 30 team using known, researched system values. '
        data.reference = 'https://www.wmo-sat.info/oscar/satellites/view/341'
        # inputs
        data.altitude_ground_station = 400 * ureg.meter     # m
        data.altitude_satellite = 860 * ureg.kilometer      # km
        data.orbit_elevation_angle = 25 * ureg.degree       # deg
        data.downlink_frequency = 137.5 * ureg.megahertz    # Hz
        data.target_energy_noise_ratio = 20.0               # dB
        data.implementation_loss = -1.0                     # dB
        data.transmit_power = 5.0 * ureg.watt               # Watt
        data.transmit_losses = -1.0                         # dB 
        data.transmit_antenna_gain = 4.0                    # dB
        data.transmit_pointing_loss = 3.0                  # dB
        data.polarization_losses = 0                     # dB
        data.atmospheric_loss = 0.75                         # dB
        data.receive_antenna_gain = 5.4                     # dB
        data.receiving_pointing_loss = 0                # dB 
        data.system_noise_figure = 5.0                      # dB
        data.noise_bandwidth = 34.0 * ureg.kilohertz        # Hz
        # intermediates
        data.downlink_wavelength = 2.180 * ureg.meter       # m
        data.link_distance = 1700 * ureg.kilometer           # km
        data.required_ebno = 21.0                           # dB
        data.transmit_power_dBm = 37.0                      # dBm
        data.transmit_eirp = 45.0                           # dBm
        data.downlink_path_loss = -140                      # dB
        # outputs
        data.received_power = 0                          # dBm
        data.minimum_detectable_signal = -124               # dBm
        data.energy_noise_ratio = 0                        # dB
        data.link_margin = 0                             # dB
        # add it to the data table
        self._datatable.append(data)
        		
		# ---------------------------------------------------------------------------------------
        # ------------------------------ fourteenth test case --------------------------------------
		# ---------------------------------------------------------------------------------------
        data = self._Data()
        data.name = 'GS Mk. 3 Unrealistic Gain Values'
        data.description = 'Modified link budget for the groundsphere Mk 3 setup with high elevation angle. Includes      ' \
            'values for eggbeater antenna, NOAA 19 weather satellite, inclined orbit, and ' \
            '137.5 MHz APT data. Used as target link budget calculation.' \
            'Developed by Mach 30 team using known, researched system values. '
        data.reference = 'https://www.wmo-sat.info/oscar/satellites/view/341'
        # inputs
        data.altitude_ground_station = 400 * ureg.meter     # m
        data.altitude_satellite = 860 * ureg.kilometer      # km
        data.orbit_elevation_angle = 90 * ureg.degree       # deg
        data.downlink_frequency = 137.5 * ureg.megahertz    # Hz
        data.target_energy_noise_ratio = 20.0               # dB
        data.implementation_loss = -1.0                     # dB
        data.transmit_power = 5.0 * ureg.watt               # Watt
        data.transmit_losses = -1.0                         # dB 
        data.transmit_antenna_gain = -4.0                   # dB
        data.transmit_pointing_loss = 0.0                   # dB
        data.polarization_losses = 0.0                      # dB
        data.atmospheric_loss = 0.0                         # dB
        data.receive_antenna_gain = -5.4                    # dB
        data.receiving_pointing_loss = 0                    # dB 
        data.system_noise_figure = 5.0                      # dB
        data.noise_bandwidth = 34.0 * ureg.kilohertz        # Hz
        # intermediates
        data.downlink_wavelength = 2.180 * ureg.meter       # m
        data.link_distance = 860 * ureg.kilometer           # km
        data.required_ebno = 21.0                           # dB
        data.transmit_power_dBm = 37.0                      # dBm
        data.transmit_eirp = 32.0                           # dBm
        data.downlink_path_loss = -130                      # dB
        # outputs
        data.received_power = -110                         # dBm
        data.minimum_detectable_signal = -124               # dBm
        data.energy_noise_ratio = 16                        # dB
        data.link_margin = -4.6                             # dB
        # add it to the data table
        self._datatable.append(data)
        		
		# ---------------------------------------------------------------------------------------
        # ------------------------------ fifthteenth test case --------------------------------------
		# ---------------------------------------------------------------------------------------
        data = self._Data()
        data.name = 'GS Mk. 3 Unrealistic Distance'
        data.description = 'Modified link budget for the groundsphere Mk 3 setup with high elevation angle. Includes      ' \
            'values for eggbeater antenna, NOAA 19 weather satellite, inclined orbit, and ' \
            '137.5 MHz APT data. Used as target link budget calculation.' \
            'Developed by Mach 30 team using known, researched system values. '
        data.reference = 'https://www.wmo-sat.info/oscar/satellites/view/341'
        # inputs
        data.altitude_ground_station = 400 * ureg.meter     # m
        data.altitude_satellite = -860 * ureg.kilometer      # km
        data.orbit_elevation_angle = 90 * ureg.degree       # deg
        data.downlink_frequency = 137.5 * ureg.megahertz    # Hz
        data.target_energy_noise_ratio = 20.0               # dB
        data.implementation_loss = -1.0                     # dB
        data.transmit_power = 5.0 * ureg.watt               # Watt
        data.transmit_losses = -1.0                         # dB 
        data.transmit_antenna_gain = 4.0                    # dB
        data.transmit_pointing_loss = 0                  # dB
        data.polarization_losses = 0                     # dB
        data.atmospheric_loss = 0.0                         # dB
        data.receive_antenna_gain = 5.4                     # dB
        data.receiving_pointing_loss = 0                # dB 
        data.system_noise_figure = 5.0                      # dB
        data.noise_bandwidth = 34.0 * ureg.kilohertz        # Hz
        # intermediates
        data.downlink_wavelength = 2.180 * ureg.meter       # m
        data.link_distance = 0 * ureg.kilometer           # km
        data.required_ebno = 21.0                           # dB
        data.transmit_power_dBm = 37.0                      # dBm
        data.transmit_eirp = 37.0                           # dBm
        data.downlink_path_loss = -130                      # dB
        # outputs
        data.received_power = 0                          # dBm
        data.minimum_detectable_signal = -124               # dBm
        data.energy_noise_ratio = 0                        # dB
        data.link_margin = 0                            # dB
        # add it to the data table
        self._datatable.append(data)
        		
		# ---------------------------------------------------------------------------------------
        # ------------------------------ sixteenth test case --------------------------------------
		# ---------------------------------------------------------------------------------------
        data = self._Data()
        data.name = 'GS Mk. 3 Unrealistic Noise Figure'
        data.description = 'Modified link budget for the groundsphere Mk 3 setup with high elevation angle. Includes      ' \
            'values for eggbeater antenna, NOAA 19 weather satellite, inclined orbit, and ' \
            '137.5 MHz APT data. Used as target link budget calculation.' \
            'Developed by Mach 30 team using known, researched system values. '
        data.reference = 'https://www.wmo-sat.info/oscar/satellites/view/341'
        # inputs
        data.altitude_ground_station = 400 * ureg.meter     # m
        data.altitude_satellite = 860 * ureg.kilometer      # km
        data.orbit_elevation_angle = 90 * ureg.degree       # deg
        data.downlink_frequency = 137.5 * ureg.megahertz    # Hz
        data.target_energy_noise_ratio = 20.0               # dB
        data.implementation_loss = -1.0                     # dB
        data.transmit_power = 5.0 * ureg.watt               # Watt
        data.transmit_losses = -1.0                         # dB 
        data.transmit_antenna_gain = 4.0                    # dB
        data.transmit_pointing_loss = -3.0                  # dB
        data.polarization_losses = 0                        # dB
        data.atmospheric_loss = 0.0                         # dB
        data.receive_antenna_gain = 5.4                     # dB
        data.receiving_pointing_loss = 0                    # dB 
        data.system_noise_figure = -5.0                      # dB
        data.noise_bandwidth = 34.0 * ureg.kilohertz        # Hz
        # intermediates
        data.downlink_wavelength = 2.180 * ureg.meter       # m
        data.link_distance = 860 * ureg.kilometer           # km
        data.required_ebno = 21.0                           # dB
        data.transmit_power_dBm = 37.0                      # dBm
        data.transmit_eirp = 37.0                           # dBm
        data.downlink_path_loss = -130                      # dB
        # outputs
        data.received_power = 0                          # dBm
        data.minimum_detectable_signal = 0               # dBm
        data.energy_noise_ratio = 0                        # dB
        data.link_margin = 0                             # dB
        # add it to the data table
        self._datatable.append(data)
        		
		# ---------------------------------------------------------------------------------------
        # ------------------------------ seventeenth test case --------------------------------------
		# ---------------------------------------------------------------------------------------
        data = self._Data()
        data.name = 'GS Mk. 3 Unrealistic Signal Bandwidth'
        data.description = 'Modified link budget for the groundsphere Mk 3 setup with high elevation angle. Includes      ' \
            'values for eggbeater antenna, NOAA 19 weather satellite, inclined orbit, and ' \
            '137.5 MHz APT data. Used as target link budget calculation.' \
            'Developed by Mach 30 team using known, researched system values. '
        data.reference = 'https://www.wmo-sat.info/oscar/satellites/view/341'
        # inputs
        data.altitude_ground_station = 400 * ureg.meter     # m
        data.altitude_satellite = 860 * ureg.kilometer      # km
        data.orbit_elevation_angle = 90 * ureg.degree       # deg
        data.downlink_frequency = 137.5 * ureg.megahertz    # Hz
        data.target_energy_noise_ratio = 20.0               # dB
        data.implementation_loss = -1.0                     # dB
        data.transmit_power = 5.0 * ureg.watt               # Watt
        data.transmit_losses = -1.0                         # dB 
        data.transmit_antenna_gain = 4.0                    # dB
        data.transmit_pointing_loss = 0                  # dB
        data.polarization_losses = 0                     # dB
        data.atmospheric_loss = 0.0                         # dB
        data.receive_antenna_gain = 5.4                     # dB
        data.receiving_pointing_loss = 0.0                # dB 
        data.system_noise_figure = 5.0                      # dB
        data.noise_bandwidth = 0 * ureg.kilohertz        # Hz
        # intermediates
        data.downlink_wavelength = 2.180 * ureg.meter       # m
        data.link_distance = 860 * ureg.kilometer           # km
        data.required_ebno = 21.0                           # dB
        data.transmit_power_dBm = 37.0                      # dBm
        data.transmit_eirp = 37.0                           # dBm
        data.downlink_path_loss = -130                      # dB
        # outputs
        data.received_power = 0                          # dBm
        data.minimum_detectable_signal = 0               # dBm
        data.energy_noise_ratio = 0                        # dB
        data.link_margin = 0                             # dB
        # add it to the data table
        self._datatable.append(data)
        
    def __getitem__(self, key):
        data = self._datatable[key]
        # TODO: make this return a LinkBudgetTestCase, which extends a LinkBudget class. 
        return data

    def __len__(self):
        return len(self._datatable)

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        return self.next()

    def next(self):
        result = None
        try:
            result = self[self.__index]
        except IndexError:
            raise StopIteration
        self.__index += 1
        return result

    class _Data:
        def __str__(self):
            return self.name

