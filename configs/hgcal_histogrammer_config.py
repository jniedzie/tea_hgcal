nEvents = 1000
printEveryNevents = 100

base_path = "/Users/jeremi/Documents/Physics/DESY/hgcal/data.nosync/"

# reco_campaign = "Sep26"
# reco_campaign = "Oct10"
# reco_campaign = "Oct24"
reco_campaign = "Nov22"

# specify input/output paths 
# inputFilePath = f"{base_path}beamtest_ReReco_{reco_campaign}/Run1695252306_Run1695252306_Link2_File0000000000_NANO.root"
# histogramsOutputFilePath = f"{base_path}beamtest_ReReco_{reco_campaign}/Run1695252306_Run1695252306_Link2_File0000000000_NANO_hists.root"

# inputFilePath = f"{base_path}beamtest_ReReco_{reco_campaign}/Run1695469681_Run1695469681_Link2_File0000000000_NANO.root"
# histogramsOutputFilePath = f"{base_path}beamtest_ReReco_{reco_campaign}/Run1695469681_Run1695469681_Link2_File0000000000_NANO_hists.root"

# inputFilePath = f"{base_path}beamtest_ReReco_{reco_campaign}/Run1695496516_Run1695496516_Link2_File0000000000_NANO.root"
# histogramsOutputFilePath = f"{base_path}beamtest_ReReco_{reco_campaign}/Run1695496516_Run1695496516_Link2_File0000000000_NANO_hists.root"

# pedestal
# suffix = ""
suffix = "_pedestalSubtraction"
# suffix = "_doNothing"
inputFilePath = f"{base_path}beamtest_ReReco_{reco_campaign}/Run1695472275_Run1695472275_Link2_File0000000000_NANO{suffix}.root"
histogramsOutputFilePath = f"{base_path}beamtest_ReReco_{reco_campaign}/Run1695472275_Run1695472275_Link2_File0000000000_NANO{suffix}_hists.root"

# inputFilePath = f"{base_path}beamtest_ReReco_{reco_campaign}/Run1695563152_Run1695563152_Link1_File0000000000_NANO.root"
# histogramsOutputFilePath = f"{base_path}beamtest_ReReco_{reco_campaign}/Run1695563152_Run1695563152_Link1_File0000000000_NANO_hists.root"

extraEventCollections = {
    "HGC_eleid_1": {
      "inputCollections": ("HGC",),
      "eleid": (0, 50),
    },
    "HGC_eleid_2": {
      "inputCollections": ("HGC",),
      "eleid": (50, 110),
    },
    "HGC_eleid_3": {
      "inputCollections": ("HGC",),
      "eleid": (110, 170),
    },
    "HGC_eleid_4": {
      "inputCollections": ("HGC",),
      "eleid": (170, 250),
    },
    "HGC_eleid_5": {
      "inputCollections": ("HGC",),
      "eleid": (250, 300),
    },
    "HGC_eleid_6": {
      "inputCollections": ("HGC",),
      "eleid": (300, 400),
    },
    "HGC_eleid_7": {
      "inputCollections": ("HGC",),
      "eleid": (400, 999999),
    },
        
    "HGC_chType_0": {
      "inputCollections": ("HGC",),
      "chType": (-1.5, -0.5),
    },
    "HGC_chType_1": {
      "inputCollections": ("HGC",),
      "chType": (-0.5, 0.5),
    },
    "HGC_chType_2": {
      "inputCollections": ("HGC",),
      "chType": (0.5, 1.5),
    },
    
    
    "GoodRecHits": {
      "inputCollections": ("HGC",),
      "eleid": (0, 400),
      "chType": (-9999., 0.5),
    },
}

# define default histograms (can be filled automatically with HistogramsFiller, based on collection and variable names)
defaultHistParams = (
#  collection      variable          bins    xmin   xmax    dir
  ("HGC",          "adc"           , 1010 , -10   , 1000  , ""),
  ("HGC",          "adcm1"         , 1010 , -10   , 1000  , ""),
  ("HGC",          "captureBlock"  , 100  , -10   , 10    , ""),
  ("HGC",          "chType"        , 20   , -10   , 10    , ""),
  ("HGC",          "detid"         , 100  , -100  , 100   , ""),
  ("HGC",          "econdIdx"      , 200  , -100  , 100   , ""),
  ("HGC",          "econdeRx"      , 20   , -10   , 10    , ""),
  ("HGC",          "eleid"         , 1010 , -10   , 1000  , ""),
  ("HGC",          "energy"        , 1000 , -1000 , 1000  , ""),
  ("HGC",          "fedId"         , 20   , -10   , 10    , ""),
  ("HGC",          "flags"         , 100  , -100  , 100   , ""),
  ("HGC",          "half"          , 20   , -10   , 10    , ""),
  ("HGC",          "halfrocChannel", 210  , -10   , 200   , ""),
  ("HGC",          "isCM"          , 20   , -10   , 10    , ""),
  ("HGC",          "isHD"          , 20   , -10   , 10    , ""),
  ("HGC",          "layer"         , 20   , -10   , 10    , ""),
  ("HGC",          "roc"           , 20   , -10   , 10    , ""),
  ("HGC",          "tctp"          , 20   , -10   , 10    , ""),
  ("HGC",          "time"          , 110  , -10   , 100   , ""),
  ("HGC",          "toa"           , 2010 , -10   , 2000  , ""),
  ("HGC",          "tot"           , 1010 , -10   , 1000  , ""),
  ("HGC",          "u"             , 100  , -20   , 20    , ""),
  ("HGC",          "v"             , 100  , -20   , 20    , ""),
  ("HGC",          "waferU"        , 40   , -20   , 20    , ""),
  ("HGC",          "waferV"        , 40   , -20   , 20    , ""),
  ("HGC",          "x"             , 40   , -20   , 20    , ""),
  ("HGC",          "y"             , 40   , -20   , 20    , ""),
  ("HGC",          "zSide"         , 20   , -10   , 10    , ""),
  
  ("HGC_chType_0", "adc"           , 1010 , -10   , 1000  , ""),
  ("HGC_chType_1", "adc"           , 1010 , -10   , 1000  , ""),
  ("HGC_chType_2", "adc"           , 1010 , -10   , 1000  , ""),
)

for i in range(7):
  defaultHistParams += (
    (f"HGC_eleid_{i+1}",  "adc"    , 1010 , -10   , 1000  , ""),
    (f"HGC_eleid_{i+1}",  "eleid"  , 1010 , -10   , 1000  , ""),
    (f"HGC_eleid_{i+1}",  "energy" , 1000 , -1000 , 1000  , ""),
  )

for hist in defaultHistParams:
  if hist[0] == "HGC":
    newHist = ("GoodRecHits",) + hist[1:]
    defaultHistParams += (newHist, )

# define histograms
# title: (n_bins, min, max, "output_directory")
histParams = (
  ("hit_x", 100, -20, 20, ""),
  ("hit_y", 100, -20, 20, ""),
)

# define 2D histograms
histParams2D = (
#  title              bins_x, min_x, max_x,  bins_y, min_y, max_y,  dir
  ("hit_xy",          40   , -20   , 20    , 40    , -20   , 20     , ""),
  ("energy_vs_adc",   1000 , -10000, 20000 , 1010  , -10   , 1000   , ""),
  ("energy_vs_adcm1", 1000 , -10000, 20000 , 1010  , -10   , 1000   , ""),
  ("energy_vs_tot",   1000 , -10000, 20000 , 1010  , -10   , 1000   , ""),
  ("time_vs_toa",     110  , -10   , 100   , 2010  , -10   , 2000   , ""),
)
