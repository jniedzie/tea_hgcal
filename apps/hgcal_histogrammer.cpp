#include "ConfigManager.hpp"
#include "CutFlowManager.hpp"
#include "Event.hpp"
#include "EventReader.hpp"
#include "EventWriter.hpp"
#include "ExtensionsHelpers.hpp"
#include "HGCalHistogramFiller.hpp"
#include "HistogramsHandler.hpp"
#include "HistogramsFiller.hpp"
#include "Logger.hpp"

using namespace std;

void CheckArgs(int argc, char **argv) {
  if (argc != 2) {
    fatal() << "Usage: " << argv[0] << " config_path\n";
    exit(1);
  }
}

int main(int argc, char **argv) {
  CheckArgs(argc, argv);
  ConfigManager::Initialize(argv[1]);
  
  auto eventReader = make_shared<EventReader>();
  auto histogramsHandler = make_shared<HistogramsHandler>();
  auto histogramFiller = make_unique<HistogramsFiller>(histogramsHandler);
  auto hgCalHistogramFiller = make_unique<HGCalHistogramFiller>(histogramsHandler);

  for (int iEvent = 0; iEvent < eventReader->GetNevents(); iEvent++) {
    auto event = eventReader->GetEvent(iEvent);

    histogramFiller->FillDefaultVariables(event);
    hgCalHistogramFiller->Fill(event);
  }

  histogramsHandler->SaveHistograms();

  auto &logger = Logger::GetInstance();
  logger.Print();

  return 0;
}