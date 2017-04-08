from lsst.obs.mosaic.mosaicPreprocessedIsr import MosaicPreprocessedIsrTask
import lsst.log
config.isr.retarget(MosaicPreprocessedIsrTask)
config.doCalibrate=True
from lsst.pipe.tasks.colorterms import Colorterm, ColortermDict
# this is the slope, then intercept
#B-u u-g [-0.90417674  0.33454352]
#Z-z r-i [-0.07042533  0.0785718 ]
#R-r r-i [-0.40320333 -0.15006839]
#V-g g-r [-0.63255469  0.04661562]
#new B-u u-g [-0.9272604   0.37629437]

config.calibrate.photoCal.colorterms.data = {
    "sdss-dr9-fink-v5b": ColortermDict(data={
        "B": Colorterm(primary="u", secondary="g", c1=-0.927360, c0=0.2863),  #this is in terms of Bab = Bvega+.09
        "V": Colorterm(primary="r", secondary="i", c1=-0.632555, c0=0.466156),
        "R": Colorterm(primary="r", secondary="i", c1=-0.393659, c0=0.06930),
        #"z": Colorterm(primary="z", secondary="i", c1=0, c0=0),
    }),
}
config.calibrate.photoCal.photoCatName='sdss-dr9-fink-v5b'
config.calibrate.photoCal.applyColorTerms=True
config.calibrate.astromRefObjLoader.filterMap = { 'R': 'r', 'V': 'g', 'B': 'u', 'z': 'z'}   # but this only works for 'R'
config.calibrate.photoRefObjLoader.filterMap = { 'R': 'r', 'V': 'g', 'B': 'u', 'z': 'z'}   # but this only works for 'R'
config.calibrate.photoCal.fluxField = 'base_PsfFlux_flux'
#log = lsst.log.Log.getLogger("processCcd.charImage.measurement.base_SdssShape")
#log.setLevel(lsst.log.INFO)
