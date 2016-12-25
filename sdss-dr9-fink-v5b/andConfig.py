filters = "ugriz"
root.magColumnMap = dict([(f,f) for f in filters])
root.magErrorColumnMap = dict([(f, f + '_err') for f in filters])
root.indexFiles = ["sdss-dr9-fink-v5b_and_90_0.fits",
                   "sdss-dr9-fink-v5b_and_90_1.fits",
                   "sdss-dr9-fink-v5b_and_90_2.fits",
                   "sdss-dr9-fink-v5b_and_424_0.fits",
                   "sdss-dr9-fink-v5b_and_424_1.fits",
                   "sdss-dr9-fink-v5b_and_424_2.fits"
                   ]
