from astropy.table import vstack,Table
from astropy.io import ascii
import matplotlib.pyplot as plt
import numpy as np

def Plot_Filters(sela,what_x='',what_y=[],ratio_x=False,ratio_y=False,legx='',legy='',prefixa='LSST::',title=''):
       
    fige, axe = plt.subplots(ncols=2, nrows=3, figsize=(14,10))
   
    fige.suptitle(title)
    for j,band in enumerate(['u','g','r','i','z','y']):
        selac=sela[np.where(np.logical_and(sela['filter']==prefixa+band,sela['e_per_sec']/sela['e_per_sec_err']>=5.))]
        if j<2:
            k=0
        if j>= 2 and j < 4:
            k=1
        if j>=4:
            k=2

        if not ratio_x:
            if not ratio_y:
                drawx=selac[what_x]
                drawy_1=selac[what_y[0]]-selac[what_y[1]]
                drawy_2=selac[what_y[0]]-selac[what_y[2]]
               
            else:

                drawx=selac[what_x]
                if what_y[1] != 'filtSkyBrightness':
                    drawy_1=selac[what_y[1]]/selac[what_y[0]]
                    drawy_2=selac[what_y[2]]/selac[what_y[0]]
                else:
                    drawy_1=0.5*(selac[what_y[1]]-21.)/selac[what_y[0]]
                    drawy_2=0.5*(selac[what_y[2]]-21.)/selac[what_y[0]]
                

        else:
            if not ratio_y:
                axe[k][j%2].plot(selac[what_x],selac[what_y[0]]-selac[what_y[1]],'k.')
                axe[k][j%2].plot(selac[what_x],selac[what_y[0]]-selac[what_y[2]],'r.')
            else:
                drawx=selac[what_x]/selac[what_y[0]]
                drawy_1=selac[what_x]/selac[what_y[0]]-selac[what_x]/selac[what_y[1]]
                drawy_2=selac[what_x]/selac[what_y[0]]-selac[what_x]/selac[what_y[2]]

        axe[k][j%2].plot(drawx,drawy_1,'k.')
        axe[k][j%2].plot(drawx,drawy_2,'r.')
        axe[k][j%2].set_xlabel(r''+legx,{'fontsize': 12.})
        axe[k][j%2].set_ylabel(r''+legy,{'fontsize': 12.})
        axe[k][j%2].set_title(band,loc='left')

def Plot_Multiple(sela,what_x='',what_y=[],ratio_x=False,ratio_y=False,legx='',legy='',prefixa='LSST::',title=''):
       
    fige, axe = plt.subplots(ncols=2, nrows=3, figsize=(14,10))
    colors=['b','g','r','m','c']
    fige.suptitle(title)
    for j,band in enumerate(['u','g','r','i','z','y']):
        selac=sela[np.where(np.logical_and(sela['filter']==prefixa+band,sela['e_per_sec']/sela['e_per_sec_err']>=5.))]
        if j<2:
            k=0
        if j>= 2 and j < 4:
            k=1
        if j>=4:
            k=2
    
        for i in range(1,6,1):
            drawx=selac[what_x]
            drawy_1=selac[what_y[0]]-selac[what_y[1]+'_'+str(i)]
            drawy_2=selac[what_y[0]]-selac[what_y[2]+'_'+str(i)]
            axe[k][j%2].plot(drawx,drawy_1,colors[i-1]+'*',label='$m_{sky}-'+str(0.1*i)+'$')
            axe[k][j%2].plot(drawx,drawy_2,colors[i-1]+'o',label='$m_{sky}+'+str(0.1*i)+'$')

        axe[k][j%2].set_xlabel(r''+legx,{'fontsize': 12.})
        axe[k][j%2].set_ylabel(r''+legy,{'fontsize': 12.})
        axe[k][j%2].set_title(band,loc='left')
        axe[k][j%2].legend(loc='upper left',fontsize=5)

def Plot_Multiple_SNR(sela,what_x='',what_y=[],ratio_x=False,ratio_y=False,legx='',legy='',prefixa='LSST::',title=''):
       
    fige, axe = plt.subplots(ncols=2, nrows=3, figsize=(14,10))
    colors=['b','g','r','m','c']
    fige.suptitle(title)
    for j,band in enumerate(['u','g','r','i','z','y']):
        selac=sela[np.where(np.logical_and(sela['filter']==prefixa+band,sela['e_per_sec']/sela['e_per_sec_err']>=5.))]
        if j<2:
            k=0
        if j>= 2 and j < 4:
            k=1
        if j>=4:
            k=2
    
        for i in range(1,6,1):
            drawx=selac[what_x]
            drawy_1=selac[what_x]/selac[what_y[1]+'_'+str(i)]
            drawy_2=selac[what_x]/selac[what_y[2]+'_'+str(i)]
            axe[k][j%2].plot(drawx,drawy_1,colors[i-1]+'*',label='$m_{sky}-'+str(0.1*i)+'$')
            axe[k][j%2].plot(drawx,drawy_2,colors[i-1]+'o',label='$m_{sky}+'+str(0.1*i)+'$')
            axe[k][j%2].plot([18, 26], [5.,5.], color='r', linestyle='-', linewidth=1)
            #axe[k][j%2].set_yscale('log')
            axe[k][j%2].set_ylim([0.,50.])
        axe[k][j%2].set_xlabel(r''+legx,{'fontsize': 12.})
        axe[k][j%2].set_ylabel(r''+legy,{'fontsize': 12.})
        axe[k][j%2].set_title(band,loc='left')
        axe[k][j%2].legend(loc='upper left',fontsize=5)

dir_snsim='lc4pg'
table_params=ascii.read(dir_snsim+'/sample.ntuple',fast_reader=False)

for i,name in enumerate(['z','dL','DayMax','X1','Color','ra','dec']):
    table_params.rename_column('col'+str(i+1),name)

for num in range(len(table_params)):

    file_name='LC_systes/lc_'+str(num).zfill(4)+'.txt'
    
    if num == 0:
        table_syste = ascii.read(file_name,fast_reader=False)
    else:
        table_n = ascii.read(file_name,fast_reader=False)
        table_syste=vstack([table_syste,table_n])
            #print num,len(table_match),len(table_n)
        
        #if num >=100:
            #break

print table_syste

Plot_Filters(table_syste,what_x='mag',what_y=['err_mag','err_mag_minus_5','err_mag_plus_5'])
Plot_Filters(table_syste,what_x='mag',what_y=['err_mag','err_mag_minus_5','err_mag_plus_5'],ratio_y=True)
Plot_Filters(table_syste,what_x='mag',what_y=['err_mag','err_mag_minus_5','err_mag_plus_5'],ratio_x=True,ratio_y=True)
Plot_Filters(table_syste,what_x='fiveSigmaDepth',what_y=['fiveSigmaDepth','fiveSigmaThrough','fiveSigmaThrough'],legx='$m_5^{OpSim}$',legy='$m_5^{OpSim}-m_5^{throughput}$')
#Plot_Filters(table_syste,what_x='fiveSigmaThrough',what_y=['fiveSigmaThrough','fiveSigmaThrough_plus','fiveSigmaThrough_minus'],legx='$m_5^{throughput}$',legy='$\Delta m_5$')
Plot_Filters(table_syste,what_x='fiveSigmaDepth',what_y=['fiveSigmaDepth','filtSkyBrightness','filtSkyBrightness'],ratio_y=True)

Plot_Multiple(table_syste,what_x='fiveSigmaThrough',what_y=['fiveSigmaThrough','fiveSigmaThrough_plus','fiveSigmaThrough_minus'],legx='$m_5^{throughput}$',legy='$\Delta m_5$')

Plot_Multiple(table_syste,what_x='mag',what_y=['err_mag','err_mag_minus','err_mag_plus'],legx='SN mag',legy='$\Delta \sigma=\sigma_{nom}-\sigma_{sky var.}$ [mag]')

Plot_Multiple(table_syste,what_x='mag',what_y=['err_mag','err_mag_minus','err_mag_plus'],legx='SN mag',legy='$\Delta \sigma=\sigma_{nom}-\sigma_{sky var.}$ [mag]')

Plot_Multiple_SNR(table_syste,what_x='mag',what_y=['err_mag','err_mag_minus','err_mag_plus'],legx='SN mag',legy='SNR')

plt.show()
