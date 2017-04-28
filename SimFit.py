from Simul_Fit_SN import *
from astropy.table import vstack,Table
import cPickle as pkl
from astropy.io import ascii

#load observations

observations=Table(names=('filter','expMJD','visitExpTime','rawSeeing','moon_frac','filtSkyBrightness','kAtm','airmass','FWHMgeom','FWHMeff','fiveSigmaDepth','Nexp'), dtype=('S1','f8', 'f8','f8','f8', 'f8','f8','f8','f8','f8', 'f8','i8'))

file_obs_name='Observations_DD_290.txt'

for line in open(file_obs_name, 'r').readlines():
    if line[0] != '#':
        thesplit=line.split(' ')
        therow=[]
        for j,val in enumerate(thesplit):
            if j !=0:
                therow.append(float(val))
            else:
                valspl=val.split('::')
                therow.append(valspl[1])
            
        observations.add_row(therow)

print observations

#Load parameters for SN generation+fit

simul_params=Table(names=('z','dL','DayMax','X1','Color','ra','dec'), dtype=('f8', 'f8','f8','f8', 'f8','f8','f8'))

file_params_name='lc4pg/sample.ntuple'

for line in open(file_params_name, 'r').readlines():
    if line[0] != '#' and line !='':
        thesplit=line.split('  ')
        therow=[]
        for val in thesplit:
            if val != '\n':
                therow.append(float(val))
        if len(therow) > 0:
            simul_params.add_row(therow)


#Now Simulate and Fit SN LC

name_for_pkl='LC.pkl'
       
pkl_file = open(name_for_pkl,'wb')
            
            
for ip in range(len(simul_params)):
    print 'Simulating ',simul_params[ip]['DayMax'],simul_params[ip]['Color'],simul_params[ip]['X1'],simul_params[ip]['z']
    mySN=Simul_Fit_SN(simul_params[ip]['DayMax'],simul_params[ip]['Color'],simul_params[ip]['X1'],simul_params[ip]['z'],observations)
    pkl.dump(mySN.outdict, pkl_file)
    lc_name='LC_sncosmo/lc_'+str(ip).zfill(4)+'.txt'
    ascii.write(mySN.table_LC,lc_name)
    #break
        
pkl_file.close()
   
