#include "HGCalHistogramFiller.hpp"

#include "ConfigManager.hpp"
#include "ExtensionsHelpers.hpp"

using namespace std;

HGCalHistogramFiller::HGCalHistogramFiller(shared_ptr<HistogramsHandler> histogramsHandler_)
    : histogramsHandler(histogramsHandler_) {
  // Here you can get some parameters from the config file
  // map<string, vector<string>> triggerSets;
  // _config->GetMap("triggerSets", triggerSets);

  eventProcessor = make_unique<EventProcessor>();
}

HGCalHistogramFiller::~HGCalHistogramFiller() {}

void HGCalHistogramFiller::Fill(const std::shared_ptr<Event> event) {
  float weight = 1;
  
  auto recHits = event->GetCollection("HGC");
  for (auto recHit : *recHits) {
    float x = recHit->Get("x");
    float y = recHit->Get("y");
    
    histogramsHandler->Fill("hit_xy", x, y, weight);

    float energy = recHit->Get("energy");
    UShort_t adc = recHit->Get("adc");

    histogramsHandler->Fill("energy_vs_adc", energy, adc, weight);

    UShort_t adcm1 = recHit->Get("adcm1");

    histogramsHandler->Fill("energy_vs_adcm1", energy, adcm1, weight);

    UShort_t tot = recHit->Get("tot");

    histogramsHandler->Fill("energy_vs_tot", energy, tot, weight);

    float time = recHit->Get("time");
    UShort_t toa = recHit->Get("toa");

    histogramsHandler->Fill("time_vs_toa", time, toa, weight);
  }
}