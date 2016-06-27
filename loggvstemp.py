import BDdb

ma_db = BDdb.get_db('/Users/EileenGonzales/Dropbox/BDNYC/BDNYCdb_copy/model_atmospheres.db')
from matplotlib import pyplot as plt

model = ma_db.dict("select teff,logg from morley_2012").fetchall()
print(model)
teff = [s['teff']for s in model] #turns dictionary output to list
logg = [s['logg']for s in model]
zip(teff,logg) #puts coloums together

f=open('morley.txt', 'w') #open file for data
#writing data to an outputfile as two coulums
for i,j in zip(teff,logg):
    txt = '{0}\t{1}\n'.format(i,j) #\t for tab \n for new line {0} is i and {1} is j
    f.write(txt)
f.close()

#Making plots
plt.scatter(teff,logg)
plt.title("Morley")
plt.ylabel('Log(g)')
plt.xlabel('Effective Temperature (K)')
plt.xlim(300,1400) # shows xrange
plt.ylim(3.9,5.6) # shows yrange
#plt.show()
plt.savefig('morley')