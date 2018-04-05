
def getXsec(sample):
    if sample.find(   "DYJetsToLL_M-50_HT-400to600_ext"             ) !=-1 : return 5.674;
    elif sample.find( "DYJetsToLL_M-50_HT-400to600"                 ) !=-1 : return 5.674;
    elif sample.find( "DYJetsToLL_M-50_HT-600to800"                 ) !=-1 : return 1.358;
    elif sample.find( "DYJetsToLL_M-50_HT-800to1200"                ) !=-1 : return 0.6229;
    elif sample.find( "DYJetsToLL_M-50_HT-1200to2500"               ) !=-1 : return 0.1512;
    elif sample.find( "DYJetsToLL_M-50_HT-2500toInf"                ) !=-1 : return 0.003659;
    elif sample.find( "QCD_HT300to500_BGenFilter"                   ) !=-1 : return 37680.0;
    elif sample.find( "QCD_HT300to500_GenJets5"                     ) !=-1 : return 70260.0;
    elif sample.find( "QCD_HT500to700_BGenFilter"                   ) !=-1 : return 4141.0;
    elif sample.find( "QCD_HT500to700_GenJets5"                     ) !=-1 : return 11200.0;
    elif sample.find( "QCD_HT500to700_ext"                          ) !=-1 : return 32060.0;
    elif sample.find( "QCD_HT500to700"                              ) !=-1 : return 32060.0;
    elif sample.find( "QCD_HT700to1000_BGenFilter"                  ) !=-1 : return 978.4;
    elif sample.find( "QCD_HT700to1000_GenJets5"                    ) !=-1 : return 3030.0;
    elif sample.find( "QCD_HT700to1000_ext"                         ) !=-1 : return 6829.0;
    elif sample.find( "QCD_HT700to1000"                             ) !=-1 : return 6829.0;
    elif sample.find( "QCD_HT1000to1500_BGenFilter"                 ) !=-1 : return 189.4;
    elif sample.find( "QCD_HT1000to1500_GenJets5"                   ) !=-1 : return 626.0;
    elif sample.find( "QCD_HT1000to1500_ext"                        ) !=-1 : return 1207.0;
    elif sample.find( "QCD_HT1000to1500"                            ) !=-1 : return 1207.0;
    elif sample.find( "QCD_HT1500to2000_BGenFilter"                 ) !=-1 : return 20.35;
    elif sample.find( "QCD_HT1500to2000_GenJets5"                   ) !=-1 : return 67.33;
    elif sample.find( "QCD_HT1500to2000_ext"                        ) !=-1 : return 120.0;
    elif sample.find( "QCD_HT1500to2000"                            ) !=-1 : return 120.0;
    elif sample.find( "QCD_HT2000toInf_BGenFilter"                  ) !=-1 : return 4.463;
    elif sample.find( "QCD_HT2000toInf_GenJets5"                    ) !=-1 : return 14.52;
    elif sample.find( "QCD_HT2000toInf_ext"                         ) !=-1 : return 25.25;
    elif sample.find( "QCD_HT2000toInf"                             ) !=-1 : return 25.25;
    elif sample.find( "SMS-T1tttt_mGluino-1200_mLSP-800"            ) !=-1 : return 0.04129;
    elif sample.find( "SMS-T1tttt_mGluino-1500_mLSP-100"            ) !=-1 : return 0.006889;
    elif sample.find( "SMS-T1tttt_mGluino-2000_mLSP-100"            ) !=-1 : return 0.0004488;
    elif sample.find( "TBar_tWch_ext2"                              ) !=-1 : return 38.06;
    elif sample.find( "TBar_tWch"                                   ) !=-1 : return 38.06;
    elif sample.find( "TBar_tch_powheg"                             ) !=-1 : return 0.0;        # ?????
    elif sample.find( "TTJets_DiLepton_ext"                         ) !=-1 : return 56.86;
    elif sample.find( "TTJets_DiLepton"                             ) !=-1 : return 56.86;
    elif sample.find( "TTJets_LO_HT600to800_ext"                    ) !=-1 : return 1.65;
    elif sample.find( "TTJets_LO_HT800to1200_ext"                   ) !=-1 : return 0.6736;
    elif sample.find( "TTJets_LO_HT1200to2500_ext"                  ) !=-1 : return 0.1194;
    elif sample.find( "TTJets_LO_HT2500toInf_ext"                   ) !=-1 : return 0.001445;
    elif sample.find( "TTJets_SingleLeptonFromT"                    ) !=-1 : return 114.0;
    elif sample.find( "TTJets_SingleLeptonFromTbar_ext"             ) !=-1 : return 114.0;
    elif sample.find( "TTJets_SingleLeptonFromTbar"                 ) !=-1 : return 114.0;
    elif sample.find( "TTWToLNu_ext1"                               ) !=-1 : return 0.2001;
    elif sample.find( "TTWToLNu_ext2"                               ) !=-1 : return 0.2001;
    elif sample.find( "TTWToQQ"                                     ) !=-1 : return 0.405;
    elif sample.find( "TTZToLLNuNu_ext1"                            ) !=-1 : return 0.2529;
    elif sample.find( "TTZToLLNuNu_ext2"                            ) !=-1 : return 0.2529;
    elif sample.find( "TTZToLLNuNu_ext3"                            ) !=-1 : return 0.2529;
    elif sample.find( "TTZToQQ"                                     ) !=-1 : return 0.5297;
    elif sample.find( "TToLeptons_sch"                              ) !=-1 : return 3.365;
    elif sample.find( "T_tWch_ext2"                                 ) !=-1 : return 38.09;
    elif sample.find( "T_tWch_v2"                                   ) !=-1 : return 38.09;
    elif sample.find( "T_tch_powheg"                                ) !=-1 : return 0.0;        # ?????
    elif sample.find( "WJetsToLNu_HT400to600_ext"                   ) !=-1 : return 48.8;
    elif sample.find( "WJetsToLNu_HT400to600"                       ) !=-1 : return 48.8;
    elif sample.find( "WJetsToLNu_HT800to1200_ext"                  ) !=-1 : return 5.497;
    elif sample.find( "WJetsToLNu_HT800to1200"                      ) !=-1 : return 5.497;
    elif sample.find( "WJetsToLNu_HT1200to2500"                     ) !=-1 : return 1.329;
    elif sample.find( "WJetsToLNu_HT2500toInf_ext"                  ) !=-1 : return 0.03209;
    elif sample.find( "WJetsToLNu_HT2500toInf"                      ) !=-1 : return 0.03209;
    elif sample.find( "WWTo2L2Nu"                                   ) !=-1 : return 10.48;
    elif sample.find( "WWToLNuQQ_ext"                               ) !=-1 : return 43.53;
    elif sample.find( "WWToLNuQQ"                                   ) !=-1 : return 43.53;
    elif sample.find( "WZTo1L1Nu2Q"                                 ) !=-1 : return 10.73;
    elif sample.find( "WZTo2L2Q"                                    ) !=-1 : return 5.606;
    elif sample.find( "ZZTo2L2Nu"                                   ) !=-1 : return 0.5644;
    elif sample.find( "ZZTo2L2Q_powheg"                             ) !=-1 : return 0.0;        # ?????
    elif sample.find( "ZZTo2L2Q"                                    ) !=-1 : return 3.222;
    elif sample.find("SingleMuon")!=-1  or sample.find("SingleElectron") !=-1 or sample.find("JetHT") !=-1 : return 1.
    else:
        print "Cross section not defined for this sample!"
        return 0

