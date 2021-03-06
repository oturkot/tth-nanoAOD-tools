from PhysicsTools.NanoAODTools.postprocessing.modules.btv.btagSFProducer import btagSFProducer

class btagSFProducer_explicitBranchNames(btagSFProducer):
  def __init__(self, algo, verbose = 0):
    btagSFProducer.__init__(self, '2017', algo, None, verbose)

    self.branchName_prefix       = "Jet_btagSF_%s" % self.algo
    self.branchName_shape_prefix = '%s_shape'      % self.branchName_prefix

    self.branchNames_central_and_systs = {}
    for central_or_syst in self.central_and_systs:
      if central_or_syst == "central":
        self.branchNames_central_and_systs[central_or_syst] = self.branchName_prefix
      else:
        self.branchNames_central_and_systs[central_or_syst] = "%s_%s" % (self.branchName_prefix, central_or_syst)

    self.branchNames_central_and_systs_shape_corr = {}
    for central_or_syst in self.central_and_systs_shape_corr:
      if central_or_syst == "central":
        self.branchNames_central_and_systs_shape_corr[central_or_syst] = self.branchName_shape_prefix
      else:
        self.branchNames_central_and_systs_shape_corr[central_or_syst] = "%s_%s" % (self.branchName_shape_prefix, central_or_syst)

btagSF_csvv2 = lambda : btagSFProducer_explicitBranchNames('csvv2')
btagSF_deep  = lambda : btagSFProducer_explicitBranchNames('deepcsv')

