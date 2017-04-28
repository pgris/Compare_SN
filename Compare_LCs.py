from astropy.table import vstack,Table
from astropy.io import ascii
import matplotlib.pyplot as plt
import numpy as np

def Plot_Filters(sela,selb,legx='',legy='',prefixa='LSST::',prefixb='LSSTPG::',title=''):
       
    fige, axe = plt.subplots(ncols=2, nrows=3, figsize=(14,10))
   
    fige.suptitle(title)
    for j,band in enumerate(['u','g','r','i','z','y']):
        selac=sela[np.where(np.logical_and(sela['filter']==prefixa+band,sela['e_per_sec']>0.))]
        selbc=selb[np.where(np.logical_and(selb['filter']==prefixb+band,selb['e_per_sec']>0.))]
        if j<2:
            k=0
        if j>= 2 and j < 4:
            k=1
        if j>=4:
            k=2

        axe[k][j%2].errorbar(selac['expMJD'],selac['e_per_sec'],yerr=selac['e_per_sec_err'],fmt='-',color = 'r')
        axe[k][j%2].errorbar(selbc['expMJD'],selbc['e_per_sec'],yerr=selbc['e_per_sec_err'],fmt='-',color = 'b')
        axe[k][j%2].set_xlabel(r''+legx,{'fontsize': 15.})
        axe[k][j%2].set_ylabel(r''+legy,{'fontsize': 15.})
        axe[k][j%2].set_title(band,loc='left')
        """
        axe[k][j%2].plot(sela[whata[0]],sela[whatb[0]]-sela[whatb[1]],'k.')
       
        axe[k][j%2].text(dict_posd[band][0], dict_posd[band][1], band, style='italic',
                         bbox={'facecolor':'yellow', 'alpha':0.5, 'pad':10})
        """

def Plot_Filters_Hists(sela,what=[],legx='',legy='',prefixa='LSST::',prefixb='LSSTPG::',title='',therange=[]):
       
    fige, axe = plt.subplots(ncols=2, nrows=3, figsize=(14,10))
   
    fige.suptitle(title)
    for j,band in enumerate(['u','g','r','i','z','y']):
        selac=sela[np.where(np.logical_and(sela['filter']==prefixa+band,sela['e_per_sec_cosmo']>0.))]
        if j<2:
            k=0
        if j>= 2 and j < 4:
            k=1
        if j>=4:
            k=2
        if len(therange) == 0:
            axe[k][j%2].hist(selac[what[0]]-selac[what[1]],bins=40)
        else:
            axe[k][j%2].hist(selac[what[0]]-selac[what[1]],bins=40,range=therange)

        axe[k][j%2].set_xlabel(r''+legx,{'fontsize': 15.})
        axe[k][j%2].set_ylabel(r''+legy,{'fontsize': 15.})
        axe[k][j%2].set_title(band,loc='left')
        """
        axe[k][j%2].plot(sela[whata[0]],sela[whatb[0]]-sela[whatb[1]],'k.')
       
        axe[k][j%2].text(dict_posd[band][0], dict_posd[band][1], band, style='italic',
                         bbox={'facecolor':'yellow', 'alpha':0.5, 'pad':10})
        """

def Plot_Filters_vs(sela,what=[],xaxis='',legx='',legy='',prefixa='LSST::',prefixb='LSSTPG::',title='',ymin=-999.):
       
    fige, axe = plt.subplots(ncols=2, nrows=3, figsize=(14,10))
   
    fige.suptitle(title)
    for j,band in enumerate(['u','g','r','i','z','y']):
        selac=sela[np.where(np.logical_and(sela['filter']==prefixa+band,sela['e_per_sec_cosmo']>0.))]
        if j<2:
            k=0
        if j>= 2 and j < 4:
            k=1
        if j>=4:
            k=2
        
        axe[k][j%2].scatter(selac[xaxis],selac[what[0]]-selac[what[1]],color='k')
        
        axe[k][j%2].set_xlabel(r''+legx,{'fontsize': 12.})
        axe[k][j%2].set_ylabel(r''+legy,{'fontsize': 12.})
        axe[k][j%2].set_title(band,loc='left')
        if ymin > -0.5:
            axe[k][j%2].set_ylim(ymin,)
       
def Plot_Filters_Hists_percent(sela,what=[],legx='',legy='',prefixa='LSST::',prefixb='LSSTPG::',title='',therange=[]):
       
    fige, axe = plt.subplots(ncols=2, nrows=3, figsize=(14,10))
   
    fige.suptitle(title)
    for j,band in enumerate(['u','g','r','i','z','y']):
        selac=sela[np.where(np.logical_and(sela['filter']==prefixa+band,sela['e_per_sec_cosmo']>0.))]
        if j<2:
            k=0
        if j>= 2 and j < 4:
            k=1
        if j>=4:
            k=2

        if len(therange) == 0:
            axe[k][j%2].hist((selac[what[0]]-selac[what[1]])/selac[what[0]],bins=40)
        else:
            axe[k][j%2].hist((selac[what[0]]-selac[what[1]])/selac[what[0]],bins=40,range=therange)

        axe[k][j%2].set_xlabel(r''+legx,{'fontsize': 15.})
        axe[k][j%2].set_ylabel(r''+legy,{'fontsize': 15.})
        axe[k][j%2].set_title(band,loc='left')
                   
        
def Plot_Filters_Hists_snr(sela,whata=[],whatb=[],legx='',legy='',prefixa='LSST::',prefixb='LSSTPG::',title='',therangea=[],therangeb=[]):
       
    fige, axe = plt.subplots(ncols=2, nrows=3, figsize=(14,10))
   
    fige.suptitle(title)
    for j,band in enumerate(['u','g','r','i','z','y']):
        selac=sela[np.where(np.logical_and(sela['filter']==prefixa+band,sela['e_per_sec_cosmo']>0.))]
        if j<2:
            k=0
        if j>= 2 and j < 4:
            k=1
        if j>=4:
            k=2

        if len(therangea) == 0:
            axe[k][j%2].hist(selac[whata[0]]/selac[whata[1]],bins=40,color='r', fc='none', histtype='step',label='sncosmo')
        else:
           axe[k][j%2].hist(selac[whata[0]]/selac[whata[1]],bins=40,range=therangea,color='r', fc='none', histtype='step',label='sncosmo')
           
        if len(therangeb) == 0:
            axe[k][j%2].hist(selac[whatb[0]]/selac[whatb[1]],bins=40,color='b', fc='none', histtype='step',label='snsim')
        else:
           axe[k][j%2].hist(selac[whatb[0]]/selac[whatb[1]],bins=40,range=therangeb,color='b', fc='none', histtype='step',label='snsim')   

        axe[k][j%2].set_xlabel(r''+legx,{'fontsize': 15.})
        axe[k][j%2].set_ylabel(r''+legy,{'fontsize': 15.})
        axe[k][j%2].set_title(band,loc='left')
        axe[k][j%2].legend(loc='upper right')     

def Plot_Filters_Hists_snr_vs(sela,whata=[],whatb=[],legx='',legy='',prefixa='LSST::',prefixb='LSSTPG::',title='',therangea=[],therangeb=[]):
       
    fige, axe = plt.subplots(ncols=2, nrows=3, figsize=(14,10))
   
    fige.suptitle(title)
    for j,band in enumerate(['u','g','r','i','z','y']):
        selac=sela[np.where(np.logical_and(sela['filter']==prefixa+band,sela['e_per_sec_cosmo']>0.))]
        if j<2:
            k=0
        if j>= 2 and j < 4:
            k=1
        if j>=4:
            k=2

       
        axe[k][j%2].scatter(selac[whata[0]],selac[whata[0]]/selac[whata[1]],color='r',label='sncosmo')
        axe[k][j%2].scatter(selac[whatb[0]],selac[whatb[0]]/selac[whatb[1]],color='b',label='snsim')
        
        
        axe[k][j%2].set_xlabel(r''+legx,{'fontsize': 15.})
        axe[k][j%2].set_ylabel(r''+legy,{'fontsize': 15.})
        axe[k][j%2].set_title(band,loc='left')
        axe[k][j%2].legend(loc='upper left')  
        axe[k][j%2].set_xlim(0,)

Process_Matching=True
Compare_LC=True

bands=['u','g','r','i','z','y']

#Load parameters
dir_sncosmo='LC_sncosmo'
dir_snsim='lc4pg'

table_params=ascii.read(dir_snsim+'/sample.ntuple',fast_reader=False)

for i,name in enumerate(['z','dL','DayMax','X1','Color','ra','dec']):
    table_params.rename_column('col'+str(i+1),name)

if Process_Matching:
    #print table_params

    for num in range(len(table_params)):

        file_name='lc_'+str(num).zfill(4)

        table_sncosmo = ascii.read(dir_sncosmo+'/'+file_name+'.txt',fast_reader=False)
        table_snsim=ascii.read(dir_snsim+'/'+file_name+'.ntuple',fast_reader=False)

    #print table_sncosmo

        for i,val in enumerate(table_sncosmo.colnames):
            table_snsim.rename_column('col'+str(i+1), val)

    #print table_snsim

        prefixa='LSST::'
        prefixb='LSSTPG::'

    #print 'hello',table_sncosmo.colnames,table_sncosmo.dtype
        table_match=Table(names=('filter','expMJD','visitExpTime','FWHMeff','moon_frac','filtSkyBrightness','kAtm','airmass','fiveSigmaDepth','Nexp','e_per_sec_cosmo','e_per_sec_err_cosmo','e_per_sec_sim','e_per_sec_err_sim'), dtype=('S7','f8', 'f8','f8','f8', 'f8','f8','i8','f8','f8','f8','f8','f8','f8'))
        #table_match=Table(names=('filter','expMJD','visitExpTime','rawSeeing','moon_frac','filtSkyBrightness','kAtm','airmass','fiveSigmaDepth','Nexp','e_per_sec_cosmo','e_per_sec_err_cosmo','e_per_sec_sim','e_per_sec_err_sim'), dtype=('S7','f8', 'f8','f8','f8', 'f8','f8','f8', 'f8','i8','f8','f8','f8','f8'))
        #table_match=Table(names=('filter','expMJD','visitExpTime','rawSeeing','moon_frac','filtSkyBrightness','kAtm','airmass','fiveSigmaDepth','Nexp','finSeeing','FWHMeff','e_per_sec','e_per_sec_err','e_per_sec_sim','e_per_sec_err_sim'), dtype=('S7','f8', 'f8','f8','f8', 'f8','f8','f8', 'f8','i8','f8','f8','f8','f8','f8','f8'))


        for band in bands:
            sela=table_sncosmo[np.where(np.logical_and(table_sncosmo['filter']==prefixa+band,table_sncosmo['e_per_sec']>=-999.))]
            selb=table_snsim[np.where(np.logical_and(table_snsim['filter']==prefixb+band,table_snsim['e_per_sec']>=-999.))]
        

            for val in sela:
                selc=selb[np.where(selb['expMJD']==val['expMJD'])]
                if len(selc)>0:
                #print 'yes found',val['e_per_sec'],val['e_per_sec_err'],selc[0]['e_per_sec'],selc[0]['e_per_sec_err']
                    resu=[]
                    for name in sela.colnames:
                        resu.append(val[name])
                    resu.append(selc[0]['e_per_sec'])
                    resu.append(selc[0]['e_per_sec_err'])
                #print resu
                    table_match.add_row(tuple(resu))

        ascii.write(table_match,'Match_LC/'+file_name+'.txt')
    #print table_match

#Plot_Filters(table_sncosmo,table_snsim,legx='expMJD',legy='e$^{-}$/s',prefixa=prefixa,prefixb=prefixb,title='DayMax='+str(table_params[num]['DayMax']))
#plt.show()

if Compare_LC:
    

    for num in range(len(table_params)):

        file_name='lc_'+str(num).zfill(4)

        if num == 0:
            table_match = ascii.read('Match_LC/'+file_name+'.txt',fast_reader=False)
        else:
            table_n=ascii.read('Match_LC/'+file_name+'.txt',fast_reader=False)
            table_match=vstack([table_match,table_n])
            #print num,len(table_match),len(table_n)

        #if num > 10:
            #break

    print table_match
    
    Plot_Filters_Hists(table_match,what=['e_per_sec_cosmo','e_per_sec_sim'],legx='$\Delta$ e$^{-}$/sec (sncosmo-snsim)',legy='Number of Entries',therange=[-10,10])
    Plot_Filters_vs(table_match,what=['e_per_sec_cosmo','e_per_sec_sim'],xaxis='e_per_sec_cosmo',legx='e$^{-}$/sec',legy='$\Delta$ e$^{-}$/sec (sncosmo-snsim)')

    #Plot_Filters_Hists_percent(table_match,what=['e_per_sec_cosmo','e_per_sec_sim'],legx='$\Delta$ e$^{-}$/sec',legy='Number of Entries',therange=[-10,10])

    Plot_Filters_Hists(table_match,what=['e_per_sec_err_cosmo','e_per_sec_err_sim'],legx='$\Delta \sigma_{e^{-}/sec}$',legy='Number of Entries')
    #Plot_Filters_Hists_percent(table_match,what=['e_per_sec_err_cosmo','e_per_sec_err_sim'],legx='$\Delta \sigma_{e^{-}/sec}$',legy='Number of Entries')
    Plot_Filters_vs(table_match,what=['e_per_sec_err_cosmo','e_per_sec_err_sim'],xaxis='e_per_sec_cosmo',legx='e$^{-}$/sec',legy='$\Delta \sigma_{e^{-}/sec}$ (sncosmo-snsim)')
    Plot_Filters_Hists_snr(table_match,whata=['e_per_sec_cosmo','e_per_sec_err_cosmo'],whatb=['e_per_sec_sim','e_per_sec_err_sim'],legx='SNR',legy='Number of Entries',prefixa='LSST::',prefixb='LSSTPG::',title='SNR',therangea=[0,50.],therangeb=[0,50.])

    Plot_Filters_Hists_snr_vs(table_match,whata=['e_per_sec_cosmo','e_per_sec_err_cosmo'],whatb=['e_per_sec_sim','e_per_sec_err_sim'],legx='e$^{-}$/sec',legy='SNR',prefixa='LSST::',prefixb='LSSTPG::',title='')

    plt.show()  
