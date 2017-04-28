import cPickle as pkl
import numpy as np
import matplotlib.pyplot as plt

all_obs=[]

filenames=['LC.pkl']

for filename in filenames:
    print 'opening',filename
    pkl_file = open(filename,'r')
    objs = []
    while 1:
        try:
            objs.append(pkl.load(pkl_file))
        except EOFError:
            break
    all_obs.append(objs)
    

sigma_c=[]
redshift=[]
delta_c=[]

what='c'
print 'hello',len(all_obs)
for oob in all_obs:
    for i,obj in enumerate(oob):
        print 'num',i,obj['status']
        if obj['status']=='try_fit':
            dict_fit=obj['fit']
            for val in ['error_coadd_through']:
                dict_tag=dict_fit[val]
                if dict_tag['fit_status'] == 'ok':
                    resfit=dict_tag['sncosmo_res']
                    corr={}
                    for i,pal in enumerate(dict_tag['sncosmo_res']['vparam_names']):
                        corr[pal]=i
                    print resfit.chisq,resfit.ndof,dict_tag['sncosmo_fitted'][what],obj[what],np.sqrt(dict_tag['sncosmo_res']['covariance'][corr[what]][corr[what]])
                    delta_c.append(obj[what]-dict_tag['sncosmo_fitted'][what])
                    sigma_c.append(np.sqrt(dict_tag['sncosmo_res']['covariance'][corr[what]][corr[what]]))
                    
                    redshift.append(dict_tag['sncosmo_fitted']['z'])


fige, axe = plt.subplots(ncols=1, nrows=1, figsize=(10,8))
axe.plot(redshift,sigma_c,'b.')
axe.set_ylim([0.,0.20])
axe.set_xlim([0.0,1.2])
axe.set_xlabel('z')
axe.set_ylabel('$\sigma_C$')

figa, axa = plt.subplots(ncols=1, nrows=1, figsize=(10,8))
axa.hist(delta_c,bins=40,range=[-0.2,0.2])
axa.set_xlabel('$\Delta c = c_{sim}-c_{fit}$')
axa.set_ylabel('Number of Entries')
#axa.set_xlim([-0.2,0.5])

plt.show()

            
