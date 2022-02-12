import pint
import math
import logging
import warnings

class LinkBudgetCalculator():
    """
    Calculator for link budgets
    
    Steps to use this class:
        1) Instantiate a calculator with a valid pint unit registry
        2) Change input variables to match desired link budget values
        3) Use the run function to update outputs
        4) Use getters to access output and intermediate values
    
    """

    def __init__(self, ureg):
        """
        LinkBudgetCalculator Constructor
        
        @type  ureg: pint Unit Registry
        @param ureg: pint unit registry for calculations and conversions
        
        """
        # set the unit registry to given pint registry
        self._ureg = ureg

        # inputs
        self._altitude_ground_station =   0 * ureg.meter        # m
        self._altitude_satellite =        0 * ureg.meter        # m
        self._orbit_elevation_angle =     0 * ureg.degree       # deg
        self._downlink_frequency =        0 * ureg.hertz        # Hz
        self._target_energy_noise_ratio = 0.0                   # dB
        self._implementation_loss =       0.0                   # dB
        self._transmit_power =            0 * ureg.watt         # Watt
        self._transmit_losses =           0.0                   # dB 
        self._transmit_antenna_gain =     0.0                   # dB
        self._transmit_pointing_loss =    0.0                   # dB
        self._polarization_losses =       0.0                   # dB
        self._atmospheric_loss =          0.0                   # dB
        self._receive_antenna_gain =      0.0                   # dB
        self._receiving_pointing_loss =   0.0                   # dB 
        self._system_noise_figure =       0.0                   # dB
        self._noise_bandwidth =           0 * ureg.hertz        # Hz
        # intermediates
        self._downlink_wavelength =       0 * ureg.meter        # m
        self._link_distance =             0 * ureg.meter        # m
        self._required_ebno =             0.0                   # dB
        self._transmit_power_dBm =        0.0                   # dBm
        self._transmit_eirp =             0.0                   # dBm
        self._downlink_path_loss =        0                     # dB
        # outputs
        self._received_power =            0.0                   # dBm
        self._minimum_detectable_signal = 0.0                   # dBm
        self._energy_noise_ratio =        0.0                   # dB
        self._link_margin =               0.0                   # dB
        
        self._is_valid =                  False                 # bool
        
        # constants
        self.c = 2.9979*pow(10,8) * ureg.meter / ureg.second    # Speed of Light
        self.Re = 6371 * ureg.kilometers    # Average Earth Radius
    
    # ---------------- altitude_ground_station ----------------
    @property
    def altitude_ground_station(self):
        """
        Get the altitude of the ground station
        
        @rtype:  pint length
        @return: altitude of ground station relative to sea level
        
        """
        return self._altitude_ground_station
    
    @altitude_ground_station.setter
    def altitude_ground_station(self, value):
        """
        Change the altitude of the ground station
        
        @type  value: pint length
        @param value: altitude of ground station relative to sea level
        
        """
        if not value.check('[length]'):
            raise TypeError('altitude_ground_station expected Pint length, received %s' % str(value))
        self._altitude_ground_station = value
        
    # ---------------- altitude_satellite ----------------
    @property
    def altitude_satellite(self):
        """
        Get the average altitude of the satellite
        
        @rtype:  pint length
        @return: average altitude of satellite relative to sea level
        
        """
        return self._altitude_satellite
    
    @altitude_satellite.setter
    def altitude_satellite(self, value):
        """
        Change the altitude of the satellite
        
        @type  value: pint length
        @param value: altitude of satellite relative to sea level
        
        """
        if not value.check('[length]'):
            raise TypeError('altitude_satellite expected Pint length, received %s' % str(value))
        self._altitude_satellite = value

    # ---------------- orbit_elevation_angle ----------------
    @property
    def orbit_elevation_angle(self):
        """
        Get the elevation angle of the satellite relative to gs
        
        @rtype:  pint angle (degrees)
        @return: orbit_elevation_angle of satellite relative to gs
        
        """
        return self._orbit_elevation_angle
    
    @orbit_elevation_angle.setter
    def orbit_elevation_angle(self, value):
        """
        Change the elevation angle of satellite relative to gs
        
        @type  value: pint angle (degrees)
        @param value: elevation angle of satellite
        
        """
        if not value.check('degree'):
            raise TypeError('orbit_elevation_angle expected Pint degree, received %s' % str(value))
        self._orbit_elevation_angle = value
        
    # ---------------- downlink_frequency ----------------
    @property
    def downlink_frequency(self):
        """
        Get the downlink frequency in Hertz
        
        @rtype:  pint frequency
        @return: frequency of downlink signal in Hertz
        
        """
        return self._downlink_frequency
    
    @downlink_frequency.setter
    def downlink_frequency(self, value):
        """
        Change the downlink signal frequency in Hertz
        
        @type  value: pint frequency
        @param value: desired downlink signal frequency in Hertz
        
        """
        if not value.check('[frequency]'):
            raise TypeError('downlink_frequency expected Pint frequency, received %s' % str(value))
        self._downlink_frequency = value
        
    # ---------------- target_energy_noise_ratio ----------------
    @property
    def target_energy_noise_ratio(self):
        """
        Get the target eb/no in dB
        
        @rtype:  number
        @return: target eb/no in dB
        
        """
        return self._target_energy_noise_ratio
    
    @target_energy_noise_ratio.setter
    def target_energy_noise_ratio(self, value):
        """
        Change the target eb/no in dB
        
        @type  value: number
        @param value: desired target eb/no in dB
        
        """
        self._target_energy_noise_ratio = value
        
    # ---------------- implementation_loss ----------------
    @property
    def implementation_loss(self):
        """
        Get the implementation_loss in dB
        
        @rtype:  number
        @return: implementation_loss in dB
        
        """
        return self._implementation_loss
    
    @implementation_loss.setter
    def implementation_loss(self, value):
        """
        Change the implementation_loss in dB
        
        @type  value: number
        @param value: desired implementation_loss in dB
        
        """
        self._implementation_loss = value
        
    # ---------------- transmit_power ----------------
    @property
    def transmit_power(self):
        """
        Get the transmit power in Watts
        
        @rtype:  pint power
        @return: transmit power in Watts
        
        """
        return self._transmit_power
    
    @transmit_power.setter
    def transmit_power(self, value):
        """
        Change the transmit power in Watts
        
        @type  value: pint power
        @param value: desired transmit power in Watts
        
        """
        if not value.check('[power]'):
            raise TypeError('transmit_power expected Pint power, received %s' % str(value))
        self._transmit_power = value
        
    # ---------------- transmit_losses ----------------
    @property
    def transmit_losses(self):
        """
        Get the transmit_losses in dB
        
        @rtype:  number
        @return: transmit_losses in dB
        
        """
        return self._transmit_losses
    
    @transmit_losses.setter
    def transmit_losses(self, value):
        """
        Change the transmit_losses in dB
        
        @type  value: number
        @param value: desired transmit_losses in dB
        
        """
        self._transmit_losses = value
        
    # ---------------- transmit_antenna_gain ----------------
    @property
    def transmit_antenna_gain(self):
        """
        Get the transmit_antenna_gain in dB
        
        @rtype:  number
        @return: transmit_antenna_gain in dB
        
        """
        return self._transmit_antenna_gain
    
    @transmit_antenna_gain.setter
    def transmit_antenna_gain(self, value):
        """
        Change the transmit_antenna_gain in dB
        
        @type  value: number
        @param value: desired transmit_antenna_gain in dB
        
        """
        self._transmit_antenna_gain = value
        
    # ---------------- transmit_pointing_loss ----------------
    @property
    def transmit_pointing_loss(self):
        """
        Get the transmit_pointing_loss in dB
        
        @rtype:  number
        @return: transmit_pointing_loss in dB
        
        """
        return self._transmit_pointing_loss
    
    @transmit_pointing_loss.setter
    def transmit_pointing_loss(self, value):
        """
        Change the transmit_pointing_loss in dB
        
        @type  value: number
        @param value: desired transmit_pointing_loss in dB
        
        """
        self._transmit_pointing_loss = value
        
    # ---------------- polarization_losses ----------------
    @property
    def polarization_losses(self):
        """
        Get the polarization_losses in dB
        
        @rtype:  number
        @return: polarization_losses in dB
        
        """
        return self._polarization_losses
    
    @polarization_losses.setter
    def polarization_losses(self, value):
        """
        Change the polarization_losses in dB
        
        @type  value: number
        @param value: desired polarization_losses in dB
        
        """
        self._polarization_losses = value
        
    # ---------------- atmospheric_loss ----------------
    @property
    def atmospheric_loss(self):
        """
        Get the atmospheric_loss in dB
        
        @rtype:  number
        @return: atmospheric_loss in dB
        
        """
        return self._atmospheric_loss
    
    @atmospheric_loss.setter
    def atmospheric_loss(self, value):
        """
        Change the atmospheric_loss in dB
        
        @type  value: number
        @param value: desired atmospheric_loss in dB
        
        """
        self._atmospheric_loss = value
        
    # ---------------- receive_antenna_gain ----------------
    @property
    def receive_antenna_gain(self):
        """
        Get the receive_antenna_gain in dB
        
        @rtype:  number
        @return: receive_antenna_gain in dB
        
        """
        return self._receive_antenna_gain
    
    @receive_antenna_gain.setter
    def receive_antenna_gain(self, value):
        """
        Change the receive_antenna_gain in dB
        
        @type  value: number
        @param value: desired receive_antenna_gain in dB
        
        """
        self._receive_antenna_gain = value
        
    # ---------------- receiving_pointing_loss ----------------
    @property
    def receiving_pointing_loss(self):
        """
        Get the receiving_pointing_loss in dB
        
        @rtype:  number
        @return: receiving_pointing_loss in dB
        
        """
        return self._receiving_pointing_loss
    
    @receiving_pointing_loss.setter
    def receiving_pointing_loss(self, value):
        """
        Change the receiving_pointing_loss in dB
        
        @type  value: number
        @param value: desired receiving_pointing_loss in dB
        
        """
        self._receiving_pointing_loss = value
        
    # ---------------- system_noise_figure ----------------
    @property
    def system_noise_figure(self):
        """
        Get the system_noise_figure in dB
        
        @rtype:  number
        @return: system_noise_figure in dB
        
        """
        return self._system_noise_figure
    
    @system_noise_figure.setter
    def system_noise_figure(self, value):
        """
        Change the system_noise_figure in dB
        
        @type  value: number
        @param value: desired system_noise_figure in dB
        
        """
        self._system_noise_figure = value
        
    # ---------------- noise_bandwidth ----------------
    @property
    def noise_bandwidth(self):
        """
        Get the noise_bandwidth in Hertz
        
        @rtype:  pint frequency
        @return: noise_bandwidth in Hertz
        
        """
        return self._noise_bandwidth
    
    @noise_bandwidth.setter
    def noise_bandwidth(self, value):
        """
        Change the noise_bandwidth in Hertz
        
        @type  value: pint frequency
        @param value: desired noise_bandwidth in Hertz
        
        """
        if not value.check('[frequency]'):
            raise TypeError('noise_bandwidth expected Pint frequency, received %s' % str(value))
        self._noise_bandwidth = value
        
    # ------------------------------------------------
    # ----------------    outputs     ----------------
    # ------------------------------------------------
    
    # ---------------- downlink_wavelength ----------------
    @property
    def downlink_wavelength(self):
        """
        Get the downlink_wavelength in meters
        
        @rtype:  pint length
        @return: downlink_wavelength in meters
        
        """
        return self._downlink_wavelength
        
    # ---------------- link_distance ----------------
    @property
    def link_distance(self):
        """
        Get the link_distance in meters
        
        @rtype:  pint length
        @return: link_distance in meters
        
        """
        return self._link_distance
        
    # ---------------- required_ebno ----------------
    @property
    def required_ebno(self):
        """
        Get the required_ebno in dB
        
        @rtype:  number
        @return: required_ebno in dB
        
        """
        return self._required_ebno
        
    # ---------------- transmit_power_dBm ----------------
    @property
    def transmit_power_dBm(self):
        """
        Get the transmit_power_dBm in dBm
        
        @rtype:  number
        @return: transmit_power_dBm in dBm
        
        """
        return self._transmit_power_dBm
        
    # ---------------- transmit_eirp ----------------
    @property
    def transmit_eirp(self):
        """
        Get the transmit_eirp in dBm
        
        @rtype:  number
        @return: transmit_eirp in dBm
        
        """
        return self._transmit_eirp
        
    # ---------------- downlink_path_loss ----------------
    @property
    def downlink_path_loss(self):
        """
        Get the downlink_path_loss in dB
        
        @rtype:  number
        @return: downlink_path_loss in dB
        
        """
        return self._downlink_path_loss
        
    # ---------------- received_power ----------------
    @property
    def received_power(self):
        """
        Get the received_power in dBm
        
        @rtype:  number
        @return: received_power in dBm
        
        """
        return self._received_power
        
    # ---------------- minimum_detectable_signal ----------------
    @property
    def minimum_detectable_signal(self):
        """
        Get the mds in dBm
        
        @rtype:  number
        @return: mds in dBm
        
        """
        return self._minimum_detectable_signal
        
    # ---------------- energy_noise_ratio ----------------
    @property
    def energy_noise_ratio(self):
        """
        Get the energy_noise_ratio in dB
        
        @rtype:  number
        @return: energy_noise_ratio in dB
        
        """
        return self._energy_noise_ratio
        
    # ---------------- link_margin ----------------
    @property
    def link_margin(self):
        """
        Get the link_margin in dB
        
        @rtype:  number
        @return: link_margin in dB
        
        """
        return self._link_margin
    
    # ---------------- other variables ----------------
    @property
    def is_valid(self):
        """
        Get the is_valid flag to determine if the run() function
        successfully calculated a link margin
        
        @rtype:  bool
        @return: validity of output variables
        
        """
        return self._is_valid
    
    # --------------------------------------------------
    # ----------------    functions     ----------------
    # --------------------------------------------------
    
    def run(self):
        """
        Run function to perform calculations necessary to determine outputs
        of link budget calculation
        
        is_valid will result in True if calculations were successful
        
    `    """
        # set is_valid to false every time a run is initiated
        self._is_valid = False
        
        # raise exceptions for any errors
        if (self._downlink_frequency.magnitude <= 0):
            raise ValueError('Invalid Frequency')
        if (self._altitude_satellite.magnitude <= 0):
            raise ValueError('Invalid Satellite Altitude')
        if (self._orbit_elevation_angle.magnitude <= 0):
            raise ValueError('Invalid elevation angle')
        if (self._system_noise_figure < 0):
            raise ValueError('System Noise Figure is negative')
        if (self._atmospheric_loss > 0):
            raise ValueError('Atmospheric Loss is positive')
        if (self._implementation_loss > 0):
            raise ValueError('Implementation loss is positive')        
        if (self._polarization_losses > 0):
            raise ValueError('Polarization Loss is positive')
        if (self._receiving_pointing_loss > 0):
            raise ValueError('Receive Pointing Loss is positive')
        if (self._transmit_losses > 0):
            raise ValueError('Transmit Loss is positive')
        if (self._transmit_pointing_loss > 0):
            raise ValueError('Transmit Pointing Loss is positive')
        if (self._noise_bandwidth.magnitude <= 0):
            raise ValueError('Noise Bandwidth is negative')
        if (self._system_noise_figure < 0):
            raise ValueError('System Noise Figure is negative')
    
        # Downlink Wavelength m
        self._downlink_wavelength = self.c / self._downlink_frequency.to('1 / second')
        
        # logging setup
        logger = logging.getLogger()
        logger.addHandler(logging.NullHandler())
        logging.debug('wavelength: {}'.format(self._downlink_wavelength))
        
        # Link Distance m
        if (self._orbit_elevation_angle.magnitude == 90):
            self._link_distance = self._altitude_satellite - self._altitude_ground_station
        else:
            orbit_elevation_angle_rad = math.radians(self._orbit_elevation_angle.magnitude)
            beta = orbit_elevation_angle_rad + (math.pi / 2)
            alpha = math.asin(((self._altitude_ground_station + self.Re) / (self._altitude_satellite + self.Re)) * math.sin(beta))
            theta = math.pi - alpha - beta
            self._link_distance = math.sin(theta) * (self._altitude_satellite + self.Re) / math.sin(beta)
        
        # LOG
        logging.debug('link_distance: {}'.format(self._link_distance))
        
        # Transmit Power dBm
        self._transmit_power_dBm = self.power_to_dBm(self._transmit_power)
        
        # LOG
        logging.debug('Tx power dBm: {}'.format(self._transmit_power_dBm))
        
        # Transmit EIRP dBm
        self._transmit_eirp = self._transmit_power_dBm + self._transmit_losses + self._transmit_antenna_gain + self._transmit_pointing_loss
        
        # LOG
        logging.debug('Tx EIRP: {}'.format(self._transmit_eirp))
    
        # Downlink Path Loss dB
        self._downlink_path_loss = -20 * math.log10(4 * math.pi * self._link_distance / self._downlink_wavelength)
        
        # LOG
        logging.debug('Path Loss : {}'.format(self._downlink_path_loss))
        
        # Required Eb/N0 dB
        self._required_ebno = self._target_energy_noise_ratio - self._implementation_loss
        
        # LOG
        logging.debug('Req Eb/N0 : {}'.format(self._required_ebno))
        
        # Recieved Power dBm
        self._received_power = self._transmit_eirp + self._downlink_path_loss + self._polarization_losses + self._atmospheric_loss + self._receive_antenna_gain + self._receiving_pointing_loss
        
        # LOG
        logging.debug('Rx Power : {}'.format(self._received_power))
        
        # MDS dBm
        self._minimum_detectable_signal = -174 + 10 * math.log10(self._noise_bandwidth.to('hertz').magnitude) + self._system_noise_figure
        
        # LOG
        logging.debug('MDS : {}'.format(self._minimum_detectable_signal))
        
        # Eb/N0 Receieved dB
        self._energy_noise_ratio = self._received_power - self._minimum_detectable_signal
        
        # LOG
        logging.debug('Eb/N0 : {}'.format(self._energy_noise_ratio))
    
        # Link Margin dB
        self._link_margin = self._energy_noise_ratio - self._required_ebno
        
        # LOG
        logging.debug('Margin : {}'.format(self._link_margin))
        
        self._is_valid = True
    
    def power_to_dBm(self, val_power):
        """
        Output the dBm value of a pint power input
        
        @type  val_power: pint power
        @param val_power: value to convert to raw dBm
        
        @rtype:  number
        @return: result of conversion in dBm
        """
        if not val_power.check('[power]'):
            raise TypeError('val_power expected Pint power, received %s' % str(val_power))
        val_mW = val_power.to(self._ureg.mW)
        val_power_dBm = 10 * math.log10(val_mW.magnitude)
        return val_power_dBm
    
    
    def dBm_to_string(self, val_dBm):
        """
        Return a string with the formatted dBm value
        
        @type  val_dBm: number
        @param val_dBm: value to add in dBm
        
        @rtype:  string
        @return: string representation of value in dBm
        
        """
        return '{} dBm'.format(val_dBm)

    def __str__(self):
        val = ' ---------------- inputs ---------------- \n'
        val = val + 'Ground Station Altitude:\t {}\n'.format(str(self._altitude_ground_station))
        val = val + 'Orbit Elevation Angle:\t\t {}\n'.format(str(self._orbit_elevation_angle))
        val = val + 'Satellite Altitude:\t\t {}\n'.format(str(self._altitude_satellite))
        val = val + 'Downlink Frequency:\t\t {}\n'.format(str(self._downlink_frequency))
        val = val + 'Target Eb/N0:\t\t\t {} dB\n'.format(str(self._target_energy_noise_ratio))
        val = val + 'Implementation Loss:\t\t {} dB\n'.format(str(self._implementation_loss))
        val = val + 'Atmospheric Loss:\t\t {} dB\n'.format(str(self._atmospheric_loss))
        val = val + 'Transmit Power:\t\t\t {}\n'.format(str(self._transmit_power))
        val = val + 'Transmit Losses:\t\t {} dB\n'.format(str(self._transmit_losses))
        val = val + 'Transmit Antenna Gain:\t\t {} dB\n'.format(str(self._transmit_antenna_gain))
        val = val + 'Transmit Pointing Loss:\t\t {} dB\n'.format(str(self._transmit_pointing_loss))
        val = val + 'Polarization Losses:\t\t {} dB\n'.format(str(self._polarization_losses))
        val = val + 'Receive Antenna Gain:\t\t {} dB\n'.format(str(self._receive_antenna_gain))
        val = val + 'Receive Pointing Loss:\t\t {} dB\n'.format(str(self._receiving_pointing_loss))
        val = val + 'System Noise Figure:\t\t {} dB\n'.format(str(self._system_noise_figure))
        val = val + 'Noise Bandwidth:\t\t {}\n'.format(str(self._noise_bandwidth))
        val = val + '---------------- intermediates ----------------\n'
        val = val + 'Downlink Wavelength:\t\t {}\n'.format(str(self._downlink_wavelength))
        val = val + 'Link Distance:\t\t\t {}\n'.format(str(self._link_distance))
        val = val + 'Required Eb/N0:\t\t\t {} dB\n'.format(str(self._required_ebno))
        val = val + 'Transmit Power (dBm):\t\t {} dBm\n'.format(str(self._transmit_power_dBm))
        val = val + 'Transmit EIRP:\t\t\t {} dBm\n'.format(str(self._transmit_eirp))
        val = val + 'Downlink Path Link:\t\t {} dB\n'.format(str(self._downlink_path_loss))
        val = val + '---------------- outputs ----------------\n'
        val = val + 'Receieved Power:\t\t {} dBm\n'.format(str(self._received_power))
        val = val + 'Minimum Detectable Signal:\t {} dBm\n'.format(str(self._minimum_detectable_signal))
        val = val + 'Energy to Noise Ratio:\t\t {} dB\n'.format(str(self._energy_noise_ratio))
        val = val + 'Link Margin:\t\t\t {} dBm\n'.format(str(self._link_margin))
        val = val + '\n'
        val = val + 'Valid Calculation:\t\t {}\n'.format(str(self._is_valid))
        
        return val
    
    
    
    
    
    
    
    
    
    
    




