from astropy.table import vstack,Table
import cPickle as pkl
from astropy.io import ascii
import numpy as np
from Simul_Fit_SN import *
import matplotlib.pyplot as plt

def Plot_Filters(sela,legx='',legy='',prefix='LSST::',title=''):
       
    fige, axe = plt.subplots(ncols=2, nrows=3, figsize=(14,10))
   
    fige.suptitle(title)
    for j,band in enumerate(['u','g','r','i','z','y']):
        selac=sela[np.where(np.logical_and(sela['filter']==prefix+band,sela['e_per_sec']>0.))]
        if j<2:
            k=0
        if j>= 2 and j < 4:
            k=1
        if j>=4:
            k=2

        axe[k][j%2].errorbar(selac['expMJD'],selac['e_per_sec'],yerr=selac['e_per_sec_err'],fmt='-',color = 'r')
        #axe[k][j%2].errorbar(selbc['expMJD'],selbc['e_per_sec'],yerr=selbc['e_per_sec_err'],fmt='-',color = 'b')
        axe[k][j%2].set_xlabel(r''+legx,{'fontsize': 15.})
        axe[k][j%2].set_ylabel(r''+legy,{'fontsize': 15.})
        axe[k][j%2].set_title(band,loc='left')

table_obs=ascii.read('Observations_DD_290.txt',fast_reader=False)
 
names=['band','mjd','exptime','rawSeeing','FWHMeff','moon_frac','sky','kAtm','airmass','FWHMgeom','FWHMeff ','m5sigmadepth','Nexp','Ra','Dec']

for i,val in enumerate(table_obs.colnames):
    if val.count('#') >= 1:
        table_obs.rename_column(val, val[1:])

print table_obs

nvals=70
bands=['u','g','r','i','z','y']
for band in bands:
    sel=table_obs[np.where(table_obs['band']=='LSST::'+band)]
    #print band,len(sel),sel[:10]
    if band == 'u':
        table_extract=sel[:nvals]
    else:
        table_extract=vstack((table_extract,sel[:nvals]))

#print 'hello',len(table_extract)
T0=60000
shift=0.

for band in bands:
    sel=table_extract[np.where(table_extract['band']=='LSST::'+band)]
    for i in range(len(sel)):
        time=T0-50.+2*i+shift
        sel[i]['mjd']=time
    if band == 'u':
        table_fake=sel
    else:
        table_fake=vstack((table_fake,sel))
    shift+=0.2

ascii.write(table_fake,'Marvelous_Obs.txt')
#print 'hello',len(table_fake),table_fake

table_fit=Table(names=('z','DayMax','X1','err_X1','Color','err_Color','ra','dec'), dtype=('f8', 'f8','f8','f8','f8','f8','f8','f8'))

x1=0
color=0
isn=-1
what='c'

for zval in np.arange(0.01,1.2,0.01):
    z=zval
    if zval==0.:
        z=0.01
    isn+=1
    mySN=Simul_Fit_SN(T0,color,x1,z,table_fake,ra=table_fake['Ra'][0],dec=table_fake['Dec'][0])

    lc_name='LC_perfect/lc_'+str(isn).zfill(4)+'.txt'
    ascii.write(mySN.table_LC,lc_name)
    #Plot_Filters(mySN.table_LC)
    thedict=mySN.outdict
    if thedict['status']=='try_fit':
        dict_fit=thedict['fit']
        for val in ['error_coadd_through']:
            dict_tag=dict_fit[val]
            if dict_tag['fit_status'] == 'ok':
                resfit=dict_tag['sncosmo_res']
                corr={}
                for i,pal in enumerate(dict_tag['sncosmo_res']['vparam_names']):
                    corr[pal]=i
                sigma_color= np.sqrt(dict_tag['sncosmo_res']['covariance'][corr['c']][corr['c']])
                color=dict_tag['sncosmo_fitted']['c']
                sigma_x1= np.sqrt(dict_tag['sncosmo_res']['covariance'][corr['x1']][corr['x1']])
                x1=dict_tag['sncosmo_fitted']['x1']
                T0_fitted=dict_tag['sncosmo_fitted']['t0']
                table_fit.add_row((z,T0_fitted,x1,sigma_x1,color,sigma_color,table_fake['Ra'][0],table_fake['Dec'][0]))
                print resfit.chisq,resfit.ndof,dict_tag['sncosmo_fitted'][what],thedict[what],np.sqrt(dict_tag['sncosmo_res']['covariance'][corr[what]][corr[what]])
            else:
                table_fit.add_row((z,-1,-1,-1,-1,-1,table_fake['Ra'][0],table_fake['Dec'][0])) 

    else:
        table_fit.add_row((z,-1,-1,-1,-1,-1,table_fake['Ra'][0],table_fake['Dec'][0]))   

    #break
ascii.write(table_fit,'Fitted_Values.txt')

plt.show()
