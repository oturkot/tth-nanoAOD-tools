import ROOT
import math, os

ROOT.PyConfig.IgnoreCommandLineOptions = True
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection,Object

class trigsusy(Module):
	def __init__(self):#, muonSelection, electronSelection):
		#self.isMC = isMC
		#self.isSig = isSig
		#self.muSel = muonSelection
		#self.elSel = electronSelection
		pass
	def beginJob(self):
		pass
	def endJob(self):
		pass
	def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
		self.out = wrappedOutputTree
		self.out.branch("HLT_HT350","I")
		self.out.branch("HLT_HT600","I")
		self.out.branch("HLT_HT800","I") 
		self.out.branch("HLT_HT900","I")
		self.out.branch("HLT_PFJet450","I")
		self.out.branch("HLT_MET170","I")
		#self.out.branch("HLT_HT350MET120","I")
		#self.out.branch("HLT_HT350MET100","I")
		#self.out.branch("HLT_HTMET","I")
		self.out.branch("HLT_IsoMu27","I")
		self.out.branch("HLT_IsoMu20","I")
		self.out.branch("HLT_IsoMu24","I")
		self.out.branch("HLT_Mu50","I")
		# single mu
		#self.out.branch("HLT_MuHT400MET70","I")
		#self.out.branch("HLT_MuHT350MET70","I")
		self.out.branch("HLT_MuHT350MET50","I")
		#self.out.branch("HLT_MuHTMET","I")
		self.out.branch("HLT_MuHT350","I")
		# for analysis
		#"HLT_MuHT600", "HLT_MuMET120", "HLT_MuHT400B", #aux
		self.out.branch("HLT_IsoEle32","I")
		self.out.branch("HLT_IsoEle22","I")
		self.out.branch("HLT_IsoEle23","I")
		self.out.branch("HLT_IsoEle27T","I")
		self.out.branch("HLT_Ele105","I")
		self.out.branch("HLT_Ele115","I")
		self.out.branch("HLT_Ele50PFJet165","I")
		# single ele
		#self.out.branch("HLT_EleHT400MET70","I")
		#self.out.branch("HLT_EleHT350MET70","I")
		self.out.branch("HLT_EleHT350MET50","I")
		#self.out.branch("HLT_EleHTMET","I")
		self.out.branch("HLT_EleHT350","I")
		# for analysis
		self.out.branch("HLT_EleHT400","I")
		self.out.branch("HLT_MuHT400","I")
		self.out.branch("HLT_Ele50HT400","I")
		self.out.branch("HLT_Mu50HT400","I")
		#latest additions 
		self.out.branch("HLT_highMHTMET","I")
		self.out.branch("HLT_MET100MHT100","I")
		self.out.branch("HLT_MET110MHT110","I")
		self.out.branch("HLT_MET120MHT120","I")
		#more MET triggers
		#self.out.branch("HLT_MET190_TypeOne_HBHE_BH","I")
		#"HLT_EleHT600","HLT_EleHT200", "HLT_EleHT400B", # aux
		## custom names
		#self.out.branch("HLT_EleOR","I")
		#self.out.branch("HLT_MuOR","I")
		#self.out.branch("HLT_LepOR","I")
		#self.out.branch("HLT_MetOR","I")
		#"HLT_IsoMu27","HLT_IsoEle32",
		#"HLT_Mu50","HLT_Ele105"
		## Trigger efficiencies
		#self.out.branch("TrigEff","F")	
	def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
		pass
	def analyze(self, event):
		"""process event, return True (go to next module) or False (fail, go to next event)"""
		HLT_obj = Object(event, "HLT")
		
		if HLT_obj.PFHT350 == True : self.out.fillBranch("HLT_HT350",1)
		else : self.out.fillBranch("HLT_HT350",0)
		
		if HLT_obj.PFHT600 == True : self.out.fillBranch("HLT_HT600",1)
		else :self.out.fillBranch("HLT_HT600",0)
		
		if HLT_obj.PFHT800 == True : self.out.fillBranch("HLT_HT800",1)
		else : self.out.fillBranch("HLT_HT600",0)
		
		if HLT_obj.PFHT900 == True : self.out.fillBranch("HLT_HT900",1)
		else : self.out.fillBranch("HLT_HT900",0)
		
		if HLT_obj.PFJet450 and HLT_obj.AK8PFJet450 == True : self.out.fillBranch("HLT_PFJet450",1)
		else : self.out.fillBranch("HLT_PFJet450",0)
		
		if HLT_obj.PFMET170_NoiseCleaned == True : self.out.fillBranch("HLT_MET170",1)
		else : self.out.fillBranch("HLT_MET170",0)
		# not in nanoAOD
		#if HLT_obj. == True : self.out.fillBranch("HLT_HT350MET120",1)
		#else : self.out.fillBranch("HLT_HT350MET120",0)
		
		#if HLT_obj. == True : self.out.fillBranch("HLT_HT350MET100",1)
		#else : self.out.fillBranch("HLT_HT350MET100",0)
		
		#if HLT_obj. == True : self.out.fillBranch("HLT_HTMET",1)
		#else : self.out.fillBranch("HLT_HTMET",0)
		
		if HLT_obj.IsoMu27 == True : self.out.fillBranch("HLT_IsoMu27",1)
		else : self.out.fillBranch("HLT_IsoMu27",0)
		
		if HLT_obj.IsoMu20 == True : self.out.fillBranch("HLT_IsoMu20",1)
		else : self.out.fillBranch("HLT_IsoMu20",0)
		
		if HLT_obj.IsoMu24 == True : self.out.fillBranch("HLT_IsoMu24",1)
		else : self.out.fillBranch("HLT_IsoMu24",0)
		
		if HLT_obj.Mu50 == True : self.out.fillBranch("HLT_Mu50",1)
		else : self.out.fillBranch("HLT_Mu50",0)
		# PFMET70 is not there only 50 
		#if HLT_obj.Mu15_IsoVVVL_PFHT400_PFMET70 == True : self.out.fillBranch("HLT_MuHT400MET70",1)
		#else : self.out.fillBranch("HLT_MuHT400MET70",0)
		
		#if HLT_obj.Mu15_IsoVVVL_PFHT350_PFMET70 == True : self.out.fillBranch("HLT_MuHT350MET70",1)
		#else : self.out.fillBranch("HLT_MuHT350MET70",0)
		
		if HLT_obj.Mu15_IsoVVVL_PFHT350_PFMET50 == True : self.out.fillBranch("HLT_MuHT350MET50",1)
		else : self.out.fillBranch("HLT_MuHT350MET50",0)
		
		#if HLT_obj.Mu15_IsoVVVL_PFHT350_PFMET70 == True and HLT_obj.Mu15_IsoVVVL_PFHT400_PFMET70 == True : self.out.fillBranch("HLT_MuHTMET",1)
		#else : self.out.fillBranch("HLT_MuHTMET",0)
		
		if HLT_obj.Mu15_IsoVVVL_PFHT350 == True : self.out.fillBranch("HLT_MuHT350",1)
		else : self.out.fillBranch("HLT_MuHT350",0)
		# for analysis
		#if HLT_obj.Ele32_eta2p1_WP75_Gsf == True and
		#should be uncommented with CMS 80X
		#if HLT_obj.Ele32_eta2p1_WPLoose_Gsf == True and is 
		if HLT_obj.Ele32_eta2p1_WPTight_Gsf == True :
			self.out.fillBranch("HLT_IsoEle32",1)
		else : self.out.fillBranch("HLT_IsoEle32",0)
		
		if HLT_obj.Ele22_eta2p1_WPLoose_Gsf == True :#and HLT_obj.Ele22_eta2p1_WPTight_Gsf == True : --> no Ele22 WP tight
			self.out.fillBranch("HLT_IsoEle22",1)
		else : self.out.fillBranch("HLT_IsoEle22",0)
		
		if HLT_obj.Ele23_WPLoose_Gsf == True : self.out.fillBranch("HLT_IsoEle23",1)
		else : self.out.fillBranch("HLT_IsoEle23",0)
		
		if HLT_obj.Ele27_WPTight_Gsf == True : self.out.fillBranch("HLT_IsoEle27T",1)
		else : self.out.fillBranch("HLT_IsoEle27T",0)
		
		if HLT_obj.Ele105_CaloIdVT_GsfTrkIdT == True : self.out.fillBranch("HLT_Ele105",1)
		else : self.out.fillBranch("HLT_Ele105",0)
		
		if HLT_obj.Ele115_CaloIdVT_GsfTrkIdT == True : self.out.fillBranch("HLT_Ele115",1)
		else : self.out.fillBranch("HLT_Ele115",0)
		
		if HLT_obj.Ele50_CaloIdVT_GsfTrkIdT_PFJet165 == True : self.out.fillBranch("HLT_Ele50PFJet165",1)
		else : self.out.fillBranch("HLT_Ele50PFJet165",0)
		
		# single ele
		#if HLT_obj.Ele15_IsoVVVL_PFHT400_PFMET70 == True : self.out.fillBranch("HLT_EleHT400MET70",1)
		#else : self.out.fillBranch("HLT_EleHT400MET70",0)
		
		#if HLT_obj._Ele15_IsoVVVL_PFHT350_PFMET70 == True : self.out.fillBranch("HLT_EleHT350MET70",1)
		#else : self.out.fillBranch("HLT_EleHT350MET70",0)
		
		if HLT_obj.Ele15_IsoVVVL_PFHT350_PFMET50 == True : self.out.fillBranch("HLT_EleHT350MET50",1)
		else : self.out.fillBranch("HLT_EleHT350MET50",0)
		
		#if HLT_obj.Ele15_IsoVVVL_PFHT350_PFMET70 == True and HLT_obj.Ele15_IsoVVVL_PFHT400_PFMET70 == True : self.out.fillBranch("HLT_EleHTMET",1)
		#else : self.out.fillBranch("HLT_EleHTMET",0)
		
		if HLT_obj.Ele15_IsoVVVL_PFHT350 == True : self.out.fillBranch("HLT_EleHT350",1)
		else : self.out.fillBranch("HLT_EleHT350",0)
		
		# for analysis
		if HLT_obj.Ele15_IsoVVVL_PFHT400 == True : self.out.fillBranch("HLT_EleHT400",1)
		else : self.out.fillBranch("HLT_EleHT400",0)
		
		if HLT_obj.Mu15_IsoVVVL_PFHT400 == True : self.out.fillBranch("HLT_MuHT400",1)
		else : self.out.fillBranch("HLT_MuHT400",0)
		
		if HLT_obj.Ele50_IsoVVVL_PFHT400 == True : self.out.fillBranch("HLT_Ele50HT400",1)
		else : self.out.fillBranch("HLT_Ele50HT400",0)
		
		if HLT_obj.Mu50_IsoVVVL_PFHT400 == True : self.out.fillBranch("HLT_Mu50HT400",1)
		else : self.out.fillBranch("HLT_Mu50HT400",0)
		
		#latest additions 
		if HLT_obj.PFMET90_PFMHT90_IDTight == True and HLT_obj.PFMETNoMu90_PFMHTNoMu90_IDTight == True and HLT_obj.PFMET100_PFMHT100_IDTight == True and HLT_obj.PFMETNoMu100_PFMHTNoMu100_IDTight == True and HLT_obj.PFMET110_PFMHT110_IDTight == True and HLT_obj.PFMETNoMu110_PFMHTNoMu110_IDTight == True and HLT_obj.PFMETNoMu120_PFMHTNoMu120_IDTight == True and HLT_obj.PFMET120_PFMHT120_IDTight == True:
			self.out.fillBranch("HLT_highMHTMET",1)
		else : self.out.fillBranch("HLT_highMHTMET",0)
		
		if HLT_obj.PFMET100_PFMHT100_IDTight == True and HLT_obj.PFMETNoMu100_PFMHTNoMu100_IDTight == True :
			 self.out.fillBranch("HLT_MET100MHT100",1)
		else : self.out.fillBranch("HLT_MET100MHT100",0)
		
		if HLT_obj.PFMET110_PFMHT110_IDTight == True and HLT_obj.PFMETNoMu110_PFMHTNoMu110_IDTight == True : 
			self.out.fillBranch("HLT_MET110MHT110",1)
		else : self.out.fillBranch("HLT_MET110MHT110",0)
		
		if HLT_obj.PFMET120_PFMHT120_IDTight == True and HLT_obj.PFMETNoMu120_PFMHTNoMu120_IDTight == True :
			 self.out.fillBranch("HLT_MET120MHT120",1)
		else : self.out.fillBranch("HLT_MET120MHT120",0)
		
		#more MET triggers should be uncommented with CMS 80X
		#if HLT_obj.PFMETTypeOne190_HBHE_BeamHaloCleaned== True : self.out.fillBranch("HLT_MET190_TypeOne_HBHE_BH",1)
		#else : self.out.fillBranch("HLT_MET190_TypeOne_HBHE_BH",0)

		
		return True


# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed
trigsusysusymod = lambda : trigsusy()#,
 
