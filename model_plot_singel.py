import BDdb
#from astrodbkit import astrodb  # do every session, loads packages- database

ma_db = BDdb.get_db('/Users/EileenGonzales/Dropbox/BDNYC/BDNYCdb_copy/model_atmospheres.db')
#db = astrodb.Database('/Users/EileenGonzales/Dropbox/BDNYC/BDNYCdb_copy/BDNYCv1.0.db')

from matplotlib import pyplot as plt
import numpy as np
import utilities as u
#from pylab import rcParams

#rcParams['figure.figsize'] = 8, 10 #sets particular figure size

def modelparameters(model, teff, logg, f_sed=False):  # to plot just one temp remove min and max and just put teff
    """plot all models from any specified model grid"""
    k = 0  # used to shift models up to fit multiple in one plot
    if model == 'bt_settl_2011':  # update names
        models = ma_db.dict(
            "select * from {} where logg={}".format(model, logg)).fetchall()  # if it doesn't work try fetchone()
        # This pulls out all of the temps at one specific gravity
        # elif model == 'morley':#this grid also has f_Sed


        for d in models:
            if d['teff']== teff and d['logg']==logg: #>= teffmin and d['teff'] <= teffmax:  # remove < and >  to plot one spectra d['teff']== number, to pick a log g do same as teff
                teff, w, f = d['teff'], d['wavelength'], d['flux']
                print teff
                f = f / max(f)  # normalizes flux
                #unc = np.ones(len(f))  #uncertainties
                #spec = [w,f,unc]
                #speck = u.rebin_spec(spec,wavnew)  #bining down
                #w = speck[0].value
                #f = speck[1].value
                plt.plot(w, f + k)  # remove k since not shifting to fit multiple on one plot
                plt.title("Bt-Settl 2011 Teff 2000K, logg(3.5)")
                #plt.annotate(teff, xy=(2.41, k),
                             #annotation_clip=False)  # legend in any spot aka text box, could switch to legend
            # k = k+1
            plt.xlim(0,5) # shows xrange
            plt.ylabel('Normalized Flux')
            plt.xlabel('Wavelength (microns)')
            plt.savefig('bt_settel_2011_2000_35')
            #plt.clf()
            plt.show()
