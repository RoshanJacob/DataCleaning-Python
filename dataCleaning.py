import csv
import pandas as pd
from pandas.core.groupby.generic import DataFrameGroupBy

dataFrame = pd.read_csv('FinalPreprocessedData.csv')

print(dataFrame.shape)

del dataFrame['hyperlink']
del dataFrame['duplicate_date']
del dataFrame['Planet_Mass']
del dataFrame['pl_letter']
del dataFrame['pl_name']
del dataFrame['pl_controvflag']
del dataFrame['pl_pnum']
del dataFrame['pl_orbper']
del dataFrame['pl_orbpererr1']
del dataFrame['pl_orbpererr2']
del dataFrame['pl_orbperlim']
del dataFrame['pl_orbsmax']
del dataFrame['pl_orbsmaxerr1']
del dataFrame['pl_orbsmaxerr2']
del dataFrame['pl_orbsmaxlim']
del dataFrame['pl_orbeccen']
del dataFrame['pl_orbeccenerr1']
del dataFrame['pl_orbeccenerr2']
del dataFrame['pl_orbeccenlim']
del dataFrame['pl_orbinclerr1']
del dataFrame['pl_orbinclerr2']
del dataFrame['pl_orbincllim']
del dataFrame['pl_bmassj']
del dataFrame['pl_bmassjerr1']
del dataFrame['pl_bmassjerr2']
del dataFrame['pl_bmassjlim']
del dataFrame['pl_bmassprov']
del dataFrame['pl_radj']
del dataFrame['pl_radjerr1']
del dataFrame['pl_radjerr2']
del dataFrame['pl_radjlim']
del dataFrame['pl_denserr1']
del dataFrame['pl_denserr2']
del dataFrame['pl_denslim']
del dataFrame['pl_ttvflag']
del dataFrame['pl_kepflag']
del dataFrame['pl_k2flag']
del dataFrame['pl_nnotes']
del dataFrame['st_dist']
del dataFrame['st_disterr1']
del dataFrame['st_disterr2']
del dataFrame['st_distlim']
del dataFrame['gaia_dist']
del dataFrame['gaia_disterr1']
del dataFrame['gaia_disterr2']
del dataFrame['gaia_distlim']
del dataFrame['st_optmag']
del dataFrame['st_optmagerr']
del dataFrame['st_optmaglim']
del dataFrame['gaia_gmag']
del dataFrame['gaia_gmagerr']
del dataFrame['gaia_gmaglim']
del dataFrame['st_tefferr1']
del dataFrame['st_tefferr2']
del dataFrame['st_tefflim']
del dataFrame['st_masserr1']
del dataFrame['st_masserr2']
del dataFrame['st_masslim']
del dataFrame['st_raderr1']
del dataFrame['st_raderr2']
del dataFrame['st_radlim']
del dataFrame['rowupdate']
del dataFrame['ra']
del dataFrame['pl_facility']
del dataFrame['dec']
del dataFrame['st_optband']

dataFrame = dataFrame.rename({
    'pl_hostname': 'Solar_System_Name',
    'pl_discmethod': 'Planet_DiscoveryMethod',
    'pl_orbincl': 'Planet_OrbitalInclination',
    'pl_dens': 'Planet_Density',
    'ra_str': 'Right_Ascension',
    'dec_str': 'Declination',
    'st_teff': 'HostPlanet_Temperature',
    'st_mass': 'HostMass',
    'st_rad': 'HostRadius',
}, axis='columns')

dataFrame.to_csv('CleanedData.csv')
print(dataFrame.shape)
