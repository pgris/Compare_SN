from Simul_Fit_SN import *
from astropy.table import vstack,Table
import cPickle as pkl
from astropy.io import ascii

file_obs_name='Observations_DD_290.txt'

table_obs=ascii.read(file_obs_name,fast_reader=False)
 
names=['band','mjd','exptime','rawSeeing','FWHMeff','moon_frac','sky','kAtm','airmass','FWHMgeom','FWHMeff ','m5sigmadepth','Nexp','Ra','Dec']

for i,val in enumerate(table_obs.colnames):
    if val.count('#') >= 1:
        table_obs.rename_column(val, val[1:])

print table_obs

dir_snsim='lc4pg'
table_params=ascii.read(dir_snsim+'/sample.ntuple',fast_reader=False)

for i,name in enumerate(['z','dL','DayMax','X1','Color','ra','dec']):
    table_params.rename_column('col'+str(i+1),name)

for num in range(len(table_params)):

    file_name='LC_systes/lc_'+str(num).zfill(4)+'.txt'

    mySN=Simul_Fit_SN(table_params[num]['DayMax'],table_params[num]['Color'],table_params[num]['X1'],table_params[num]['z'],table_obs,syste=True)

    ascii.write(mySN.table_LC_syste,file_name)

    #break
