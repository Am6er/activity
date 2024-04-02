import becquerel as bq
import numpy as np
from scipy.constants import physical_constants

# weight in kg
mass = 4 * 55.91 / 1000.0

# constants
AMU = physical_constants['unified atomic mass unit'][0]
K = bq.Element('Potassium')
K40 = bq.Isotope('K-40')
Cl = bq.Element('Cl')

# calculate number of K and K-40 atoms in the sample
mass_K = mass * K.atomic_mass / (K.atomic_mass + Cl.atomic_mass)
n_K = mass_K / AMU / K.atomic_mass
n_K40 = n_K * K40.abundance.nominal_value / 100

# determine activity of K-40
# n(t) = n0 2^(-t / hl) = n0 exp(-t ln(2) / hl)
# dn/dt = -n0 ln(2) / hl exp(-t ln(2) / hl)
activity_Bq = n_K40 * np.log(2) / K40.half_life
activity_uCi = activity_Bq / 3.7e4

print('total mass: {:.4f} kg'.format(mass))
print('mass of K:  {:.4f} kg'.format(mass_K))
print('number of K nuclei: {:.4e}'.format(n_K))
print('number of K-40 nuclei: {:.4e}'.format(n_K40))
print('activity: {:.4f} Bq, {:.4f} uCi'.format(activity_Bq, activity_uCi))
