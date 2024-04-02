import becquerel as bq
import numpy as np
from scipy.constants import physical_constants

# weight in kg
mass = 20 / 1000.0

# constants
AMU = physical_constants['unified atomic mass unit'][0]
Lu = bq.Element('Lutetium')
Lu176 = bq.Isotope('Lu-176')
O = bq.Element('O')

# calculate number of Lu and Lu-176 atoms in the sample
mass_Lu = mass * 2 * Lu.atomic_mass / (2 * Lu.atomic_mass + 3 * O.atomic_mass)
n_Lu = mass_Lu / AMU / Lu.atomic_mass
n_Lu176 = n_Lu * Lu176.abundance.nominal_value / 100

# determine activity of Lu-176
# n(t) = n0 2^(-t / hl) = n0 exp(-t ln(2) / hl)
# dn/dt = -n0 ln(2) / hl exp(-t ln(2) / hl)
activity_Bq = n_Lu176 * np.log(2) / Lu176.half_life
activity_uCi = activity_Bq / 3.7e4

print('total mass: {:.4f} kg'.format(mass))
print('mass of Lu:  {:.4f} kg'.format(mass_Lu))
print('number of Lu nuclei: {:.4e}'.format(n_Lu))
print('number of Lu-176 nuclei: {:.4e}'.format(n_Lu176))
print('activity: {:.4f} Bq, {:.4f} uCi'.format(activity_Bq, activity_uCi))
