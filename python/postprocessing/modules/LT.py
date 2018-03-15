import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from xsec import getXsec

class selectionProducer(Module):
    def __init__(self):
        self.lt = "LT"
    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
		self.out = wrappedOutputTree

#		self.out.branch("MET",  "F")
		self.out.branch("L_T",  "F")
		self.out.branch("xsec",  "F")
		xsec = getXsec(inputFile.GetName())
		print inputFile.GetName()
		print xsec
		self.out.fillBranch("xsec",xsec)
		
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):
        isMC = event.run == 1
        electrons = Collection(event, "Electron")
        muons = Collection(event, "Muon")
        met = Object(event, "MET")

		#lepton selection
        wElectrons = [x for x in electrons if (x.cutBased == 4 and x.miniPFRelIso_all < 0.1 and x.convVeto)]	 #loose pt cut for veto 
        wMuons = [x for x in muons if (x.mediumId and x.miniPFRelIso_all < 0.2 and x.sip3d < 4 )]   			 #loose pt cut for veto
        wMuons.sort(key=lambda x:x.pt,reverse=True)
        wElectrons.sort(key=lambda x:x.pt,reverse=True)
        Vtype = -1
        vLeptons = [] # decay products of V
        if len(wElectrons) + len(wMuons) == 1:
            if len(wMuons) == 1:
                Vtype = 0
                vLeptons = [wMuons[0]]
            if len(wElectrons) == 1:
                Vtype=1
                vLeptons = [wElectrons[0]]
        else: return False

        self.out.fillBranch("L_T", vLeptons[0].pt + met.pt)
        
        return True
        

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed
LTModule = lambda : selectionProducer()
