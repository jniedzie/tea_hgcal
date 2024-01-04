#ifndef HGCalHistogramFiller_hpp
#define HGCalHistogramFiller_hpp

#include "Event.hpp"
#include "EventProcessor.hpp"
#include "Helpers.hpp"
#include "HistogramsHandler.hpp"

class HGCalHistogramFiller {
 public:
  HGCalHistogramFiller(std::shared_ptr<HistogramsHandler> histogramsHandler_);
  ~HGCalHistogramFiller();

  void Fill(const std::shared_ptr<Event> event);

 private:
  std::shared_ptr<HistogramsHandler> histogramsHandler;
  std::unique_ptr<EventProcessor> eventProcessor;
};

#endif /* HGCalHistogramFiller_hpp */
