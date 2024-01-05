import ROOT
from ROOT import TColor
from Sample import Sample, SampleType
from Legend import Legend
from Histogram import Histogram, Histogram2D
from HistogramNormalizer import NormalizationType

base_path = "/Users/jeremi/Documents/Physics/DESY/hgcal/data.nosync/beamtest_ReReco_"

output_path = "../plots/pedestal/"

# data&signals must be listed after backgrounds for now
samples = (
  # Sample(
  #   name="Run_1695496516_physics_mu",
  #   file_path=f"{base_path}Oct24/Run1695496516_Run1695496516_Link2_File0000000000_NANO_hists.root", 
  #   type=SampleType.data,
  #   line_alpha=1.0,
  #   line_color=ROOT.kViolet,
  #   fill_color=41,
  #   fill_alpha=0.0,
  #   marker_size=1.0,
  #   legend_description="Physics #mu^{-}"
  # ),
  # Sample(
  #   name="Run_1695469681_sep26",
  #   file_path=f"{base_path}Sep26/Run1695469681_Run1695469681_Link2_File0000000000_NANO_hists.root",
  #   type=SampleType.data,
  #   line_alpha=1.0,
  #   line_color=ROOT.kCyan+1,
  #   fill_color=41,
  #   fill_alpha=0.0,
  #   marker_size=1.0,
  #   legend_description="Physics e^{-} (Sep26)"
  # ),
  
  # Sample(
  #   name="Run_1695469681_oct10",
  #   file_path=f"{base_path}Oct10/Run1695469681_Run1695469681_Link2_File0000000000_NANO_hists.root",
  #   type=SampleType.data,
  #   line_alpha=1.0,
  #   line_color=ROOT.kBlue,
  #   line_style=ROOT.kDashed,
  #   fill_color=41,
  #   fill_alpha=0.0,
  #   marker_size=1.0,
  #   legend_description="Physics e^{-} (Oct10)"
  # ),
  # Sample(
  #   name="Run_1695469681_physics_e",
  #   file_path=f"{base_path}Oct24/Run1695469681_Run1695469681_Link2_File0000000000_NANO_hists.root",
  #   type=SampleType.data,
  #   line_alpha=1.0,
  #   line_color=ROOT.kCyan+2,
  #   line_style=ROOT.kSolid,
  #   fill_color=41,
  #   fill_alpha=0.0,
  #   marker_size=1.0,
  #   legend_description="Physics e^{-}"
  # ),
  
  # Sample(
  #   name="Run_1695252306_technical_e",
  #   file_path=f"{base_path}Oct24/Run1695252306_Run1695252306_Link2_File0000000000_NANO_hists.root", 
  #   type=SampleType.data,
  #   line_alpha=1.0,
  #   line_color=ROOT.kBlue,
  #   fill_color=41,
  #   fill_alpha=0.0,
  #   marker_size=1.0,
  #   legend_description="Technical e^{-}"
  # ),
  
  # Sample(
  #   name="Run_1695472275_pedestal_doNothing",
  #   file_path=f"{base_path}Oct24/Run1695472275_Run1695472275_Link2_File0000000000_NANO_doNothing_hists.root", 
  #   type=SampleType.data,
  #   line_alpha=1.0,
  #   line_color=ROOT.kGreen,
  #   line_width=2,
  #   fill_color=41,
  #   fill_alpha=0.0,
  #   marker_size=1.0,
  #   legend_description="Pedestal (did nothing)"
  # ),
  # Sample(
  #   name="Run_1695472275_pedestal_pedestalSubtraction_Oct24",
  #   file_path=f"{base_path}Oct24/Run1695472275_Run1695472275_Link2_File0000000000_NANO_pedestalSubtraction_hists.root", 
  #   type=SampleType.background,
  #   line_alpha=1.0,
  #   line_color=ROOT.kBlue,
  #   line_width=2,
  #   fill_color=41,
  #   fill_alpha=0.0,
  #   marker_size=1.0,
  #   legend_description="Old pedestal"
  # ),
  
  # Sample(
  #   name="Run_1695472275_pedestal_doNothing",
  #   file_path=f"{base_path}Oct24/Run1695472275_Run1695472275_Link2_File0000000000_NANO_doNothing_hists.root", 
  #   type=SampleType.data,
  #   line_alpha=1.0,
  #   line_color=ROOT.kGreen,
  #   line_width=2,
  #   fill_color=41,
  #   fill_alpha=0.0,
  #   marker_size=1.0,
  #   legend_description="Pedestal (did nothing)"
  # ),
  Sample(
    name="Run_1695472275_pedestal_pedestalSubtraction_Nov22",
    file_path=f"{base_path}Nov22/Run1695472275_Run1695472275_Link2_File0000000000_NANO_pedestalSubtraction_hists.root", 
    type=SampleType.data,
    line_alpha=1.0,
    line_color=ROOT.kGreen+1,
    line_width=2,
    fill_color=41,
    fill_alpha=0.0,
    marker_size=1.0,
    legend_description="New pedestal"
  ),
  
  # Sample(
  #   name="Run_1695563152_physics_pi",
  #   file_path=f"{base_path}Oct24/Run1695563152_Run1695563152_Link1_File0000000000_NANO_hists.root", 
  #   type=SampleType.data,
  #   line_alpha=1.0,
  #   line_color=ROOT.kOrange+1,
  #   fill_color=41,
  #   fill_alpha=0.0,
  #   marker_size=0.0,
  #   legend_description="Physics #pi"
  # ),
)

histograms = [
#           name              title             logy   norm_type               rebin  xmin   xmax ymin   ymax   xlabel                        ylabel
  Histogram("HGC_adc",            "", True,  NormalizationType.none, 5,      -10,  1000 ,  -1,  -1,  "ADC Counts",                 "Counts"),
  # Histogram("HGC_adcm1",          "", True,  NormalizationType.none, 5,      -10,  1000 ,  -1,  -1,  "ADC_{-1} Counts",            "Counts"),
  # Histogram("HGC_captureBlock",   "", False, NormalizationType.none, 1,      -5 ,    5  ,  -1,  -1,  "Capture Block",              "Counts"),
  Histogram("HGC_chType",         "", True,  NormalizationType.none, 1,      -5 ,    5  ,  -1,  -1,  "Channel Type",               "Counts"),
  Histogram("HGC_detid",          "", False, NormalizationType.none, 1,     -100,   100 ,  -1,  -1,  "Detector ID",                "Counts"),
  Histogram("HGC_econdIdx",       "", False, NormalizationType.none, 1,      -5 ,    10 ,  -1,  -1,  "ECON-D Index",               "Counts"),
  Histogram("HGC_econdeRx",       "", True,  NormalizationType.none, 1,      -5 ,    10 ,  -1,  -1,  "ECON-D eRx",                 "Counts"),
  Histogram("HGC_eleid",          "", True,  NormalizationType.none, 1,     -100,  1000 ,  -1,  -1,  "Electronics ID",             "Counts"),
  Histogram("HGC_energy",         "", True,  NormalizationType.none, 1,   -500, 1000 ,  -1,  -1,  "Charge (fC)",               "Counts"),
  # Histogram("HGC_fedId",          "", False, NormalizationType.none, 1,      -5 ,    10 ,  -1,  -1,  "FED ID",                     "Counts"),
  # Histogram("HGC_flags",          "", False, NormalizationType.none, 1,      -10,    10 ,  -1,  -1,  "Flags",                      "Counts"),
  # Histogram("HGC_half",           "", False, NormalizationType.none, 1,      -10,    10 ,  -1,  -1,  "Half",                       "Counts"),
  # Histogram("HGC_halfrocChannel", "", True,  NormalizationType.none, 1,      -10,   200 ,  -1,  -1,  "Half ROC Channel",           "Counts"),
  # Histogram("HGC_isCM",           "", False, NormalizationType.none, 1,      -10,    10 ,  -1,  -1,  "is Common Mode",             "Counts"),
  # Histogram("HGC_isHD",           "", False, NormalizationType.none, 1,      -10,    10 ,  -1,  -1,  "is HD",                      "Counts"),
  Histogram("HGC_layer",          "", False, NormalizationType.none, 1,       -5,    10 ,  -1,  -1,  "Layer",                      "Counts"),
  # Histogram("HGC_roc",            "", False, NormalizationType.none, 1,       -5,    10 ,  -1,  -1,  "ROC",                        "Counts"),
  # Histogram("HGC_tctp",           "", True,  NormalizationType.none, 1,       -5,    10 ,  -1,  -1,  "TCTP",                       "Counts"),
  # Histogram("HGC_time",           "", True,  NormalizationType.none, 1,      -10,    30 ,  -1,  -1,  "Time (ns)",                  "Counts"),
  # Histogram("HGC_toa",            "", True,  NormalizationType.none, 2,      -10,   1050,  -1,  -1,  "Time of Arrival (ToA)",      "Counts"),
  Histogram("HGC_tot",            "", True,  NormalizationType.none, 2,      -10,   1000,  -1,  -1,  "Time over Threshold (ToT)",  "Counts"),
  # Histogram("HGC_u",              "", False, NormalizationType.none, 1,      -5,     20 ,  -1,  -1,  "U",                          "Counts"),
  # Histogram("HGC_v",              "", False, NormalizationType.none, 1,      -5,     20 ,  -1,  -1,  "V",                          "Counts"),
  # Histogram("HGC_waferU",         "", False, NormalizationType.none, 1,      -20,    20 ,  -1,  -1,  "Wafer U",                    "Counts"),
  # Histogram("HGC_waferV",         "", False, NormalizationType.none, 1,      -20,    20 ,  -1,  -1,  "Wafer V",                    "Counts"),
  # Histogram("HGC_x",              "", False, NormalizationType.none, 1,      -20,    20 ,  -1,  -1,  "x (cm)",                     "Counts"),
  # Histogram("HGC_y",              "", False, NormalizationType.none, 1,      -20,    20 ,  -1,  -1,  "y (cm)",                     "Counts"),
  # Histogram("HGC_zSide",          "", False, NormalizationType.none, 1,      -10,    10 ,  -1,  -1,  "Z-side",                     "Counts"), 
  
  # Histogram("HGC_eleid_2_chType_0_adc",            "", True,  NormalizationType.none, 5,      -10,  1000 ,  -1,  -1,  "ADC Counts",                 "Counts"),
  # Histogram("HGC_eleid_2_chType_1_adc",            "", True,  NormalizationType.none, 5,      -10,  1000 ,  -1,  -1,  "ADC Counts",                 "Counts"),
  # Histogram("HGC_eleid_2_chType_2_adc",            "", True,  NormalizationType.none, 5,      -10,  1000 ,  -1,  -1,  "ADC Counts",                 "Counts"),
  
  Histogram("HGC_chType_0_adc",            "", True,  NormalizationType.none, 5,      -10,  1000 ,  -1,  -1,  "ADC Counts",                 "Counts"),
  Histogram("HGC_chType_1_adc",            "", True,  NormalizationType.none, 5,      -10,  1000 ,  -1,  -1,  "ADC Counts",                 "Counts"),
  Histogram("HGC_chType_2_adc",            "", True,  NormalizationType.none, 5,      -10,  1000 ,  -1,  -1,  "ADC Counts",                 "Counts"),
  
  
  Histogram("GoodRecHits_adc",            "", True,  NormalizationType.none, 5,      -10,  1000 ,  -1,  -1,  "ADC Counts",                 "Counts"),
  Histogram("GoodRecHits_chType",         "", True,  NormalizationType.none, 1,      -5 ,    5  ,  -1,  -1,  "Channel Type",               "Counts"),
  Histogram("GoodRecHits_detid",          "", False, NormalizationType.none, 1,     -100,   100 ,  -1,  -1,  "Detector ID",                "Counts"),
  Histogram("GoodRecHits_eleid",          "", True,  NormalizationType.none, 1,     -100,  1000 ,  -1,  -1,  "Electronics ID",             "Counts"),
  Histogram("GoodRecHits_energy",         "", True,  NormalizationType.none, 1,   -500, 1000 ,  -1,  -1,  "Charge (fC)",               "Counts"),
]



histograms2D = (
# 2D histograms
#           name              title    rebin  xmin    xmax       ymin   ymax     zmin zmax xlabel               ylabel                        zlabel
  Histogram2D("hit_xy",         ""    , 1, 1, -15     , 15      , -15   , 15    , 0,  1e5, "x"             , "y"                         , "Counts"),
  Histogram2D("energy_vs_adc",  ""    , 1, 1, -10000  , 10000   , -10   , 1000  , 0,  100, "Charge (fC)"  , "ADC Counts"                , "Counts"),
  Histogram2D("energy_vs_adcm1",""    , 1, 1, -10000  , 10000   , -10   , 1000  , 0,  100, "Charge (fC)"  , "ADC_{-1} Counts"           , "Counts"),
  Histogram2D("energy_vs_tot",  ""    , 1, 1, -10000  , 10000   , -10   , 1000  , 0,  100, "Charge (fC)"  , "Time over Threshold (ToT)" , "Counts"),
  Histogram2D("time_vs_toa",    ""    , 1, 1, -10     , 100     , -10   , 2000  , 0,  1e3, "Time (ns)"     , "Time of Arrival (ToA)"     , "Counts"),
)

legends = {
  SampleType.background: Legend(0.60, 0.7, 0.89, 0.85, "l"),
  SampleType.data: Legend(0.60, 0.7, 0.7, 0.85, "l"),
}

plotting_options = {
  SampleType.background: "hist",
  SampleType.signal: "nostack e",
  SampleType.data: "nostack hist",
}

canvas_size = (800, 600)
show_ratio_plots = True
ratio_limits = (0.0, 2.0)

# CMS labels settings
show_cms_labels = False
extraText = "Preliminary"
