#!/usr/bin/env python
import os,sys

from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from wvAnalysisModule import *

testfile = "root://cms-xrd-global.cern.ch//store/data/Run2018C/DoubleMuon/NANOAOD/Nano25Oct2019-v1/240000/BB1EC3A4-AB2E-BC49-A2A5-97242D4808C4.root"

if testfile.find("SingleMuon") != -1 or testfile.find("EGamma") != -1 or testfile.find("SingleElectron") != -1 or testfile.find("DoubleMuon") != -1 or testfile.find("MuonEG") != -1 or testfile.find("DoubleEG") != -1:
  print "==> Processing a data file..."
  if testfile.find("Run2016") != -1:
    print "==> Running over 2016 data...."
    p=PostProcessor(".",[testfile],None,None,[wvAnalysisModule()],provenance=False,fwkJobReport=False,jsonInput="Cert_271036-284044_13TeV_PromptReco_Collisions16_JSON.txt",)
  if testfile.find("Run2017") != -1:
    print "==> Running over 2017 data...."
    p=PostProcessor(".",[testfile],None,None,[wvAnalysisModule()],provenance=False,fwkJobReport=False,jsonInput="Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt",)
  if testfile.find("Run2018") != -1:
    print "==> Running over 2018 data...."
    p=PostProcessor(".",[testfile],None,None,[wvAnalysisModule()],provenance=False,fwkJobReport=False,jsonInput="Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt",)
  #p=PostProcessor(".",[testfile],None,None,[wvAnalysisModule()],provenance=False,fwkJobReport=False,jsonInput="Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt",maxEntries=21000,)

else:
  print "==> Processing a MC file..."
  from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2 import *
  if testfile.find("RunIIAutumn18NanoAODv6") != -1: year = 2018
  if testfile.find("RunIIFall17NanoAODv6") != -1: year = 2017
  if testfile.find("RunIISummer16NanoAODv6") != -1: year = 2016
  jetmetCorrector = createJMECorrector(isMC=True, dataYear=year, jesUncert="All", redojec=True, jetType = "AK4PFchs")
  fatJetCorrector = createJMECorrector(isMC=True, dataYear=year, jesUncert="All", redojec=True, jetType = "AK8PFPuppi")
  p=PostProcessor(".",[testfile],"","keep_and_drop.txt",[jetmetCorrector(),fatJetCorrector(),wvAnalysisModule()],provenance=True,)
  #p=PostProcessor(".",[testfile],"","keep_and_drop.txt",[jetmetCorrector(),fatJetCorrector(),wvAnalysisModule()],provenance=True,maxEntries=21000,)

p.run()

print "DONE"
#os.system("ls -lR")
