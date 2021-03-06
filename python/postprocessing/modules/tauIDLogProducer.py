import math
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

def logId(id_):
  '''Converts bitmask
        0, 1, 3, 7, 15, 31, 63, ...
      to a sequence of integers
        0, 1, 2, 3, 4, 5, 6, ...
  '''
  if id_ > 0:
    return int(math.log(id_ + 1, 2))
  return id_

class tauIDLogProducer(Module):

  def __init__(self):
    self.tauBr_base = "Tau"
    self.tauBr_n    = "n%s" % self.tauBr_base
    self.tauBr_ids  = {
      tauBr_id : '%s_%s_log' % (self.tauBr_base, tauBr_id) \
      for tauBr_id in ['idAntiMu', 'idAntiEle', 'idMVAnewDM', 'idMVAoldDM', 'idMVAoldDMdR03']
    }

  def beginJob(self):
    pass

  def endJob(self):
    pass

  def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
    self.out = wrappedOutputTree
    for tauBr_id in self.tauBr_ids:
      self.out.branch(self.tauBr_ids[tauBr_id], "I", lenVar = self.tauBr_n)

  def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
    pass

  def analyze(self, event):
    taus = Collection(event, "Tau")
    for tauBr_id in self.tauBr_ids:
      self.out.fillBranch(self.tauBr_ids[tauBr_id], map(lambda tau: logId(getattr(tau, tauBr_id)), taus))
    return True

# provide this variable as the 2nd argument to the import option for the nano_postproc.py script
tauIDLog = lambda : tauIDLogProducer()
