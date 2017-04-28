from astropy.table import vstack,Table
from astropy.io import ascii
import matplotlib.pyplot as plt
import numpy as np

def Plot_Filters_vs(sela,xaxis='',yaxis='',legx='',legy='',title=''):
       
    fige, axe = plt.subplots(ncols=2, nrows=3, figsize=(14,10))
   
    fige.suptitle(title)
    for j,band in enumerate(['u','g','r','i','z','y']):
        selac=sela[np.where(sela['filter']=='LSST::'+band)]
        if j<2:
            k=0
        if j>= 2 and j < 4:
            k=1
        if j>=4:
            k=2
        
        axe[k][j%2].scatter(selac[xaxis],selac[yaxis],color='k')
        
        axe[k][j%2].set_xlabel(r''+legx,{'fontsize': 12.})
        axe[k][j%2].set_ylabel(r''+legy,{'fontsize': 12.})
        axe[k][j%2].set_title(band,loc='left')
       

bands=['u','g','r','i','z','y']

#Load parameters
dir_sncosmo='LC_sncosmo'
dir_snsim='lc4pg'

table_params=ascii.read(dir_snsim+'/sample.ntuple',fast_reader=False)

for i,name in enumerate(['z','dL','DayMax','X1','Color','ra','dec']):
    table_params.rename_column('col'+str(i+1),name)
for num in range(len(table_params)):

        file_name='lc_'+str(num).zfill(4)

        if num == 0:
            table_match = ascii.read('LC_sncosmo/'+file_name+'.txt',fast_reader=False)
        else:
            table_n=ascii.read('LC_sncosmo/'+file_name+'.txt',fast_reader=False)
            table_match=vstack([table_match,table_n])

print table_match

nbins=15

for band in bands:
    sel=table_match[np.where(table_match['filter']=='LSST::'+band)]
    print 'Filter',band
    for val in ['rawSeeing','finSeeing','FWHMeff']:
        print val,np.mean(sel[val]),np.std(sel[val]),np.median(sel[val])

plt.hist(table_match['rawSeeing'],bins=nbins,color='b', fc='none', histtype='step',label='rawSeeing')
plt.hist(table_match['finSeeing'],bins=nbins,color='r', fc='none', histtype='step',label='finSeeing')
plt.hist(table_match['FWHMeff'],bins=nbins,color='g', fc='none', histtype='step',label='FWHMeff')
plt.legend(loc='upper right')


Plot_Filters_vs(table_match,xaxis='airmass',yaxis='rawSeeing')

plt.show()
