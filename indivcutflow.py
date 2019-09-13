import ROOT

ROOT.gROOT.SetBatch(1)
ROOT.gStyle.SetOptStat(0)
tfile0=ROOT.TFile("mc16a.344388.root","OLD")
tfile1=ROOT.TFile("mc16a.345672.root","OLD")
tfile2=ROOT.TFile("mc16a.345673.root","OLD")
tfile3=ROOT.TFile("mc16a.345674.root","OLD")
tfile4=ROOT.TFile("mc16a.410155.root","OLD")
tfile5=ROOT.TFile("mc16a.410218.root","OLD")
tfile6=ROOT.TFile("mc16a.410219.root","OLD")
tfile7=ROOT.TFile("mc16a.410470.root","OLD")
ttree0=tfile0.Get("DiMuonNtuple")
ttree1=tfile1.Get("DiMuonNtuple")
ttree2=tfile2.Get("DiMuonNtuple")
ttree3=tfile3.Get("DiMuonNtuple")
ttree4=tfile4.Get("DiMuonNtuple")
ttree5=tfile5.Get("DiMuonNtuple")
ttree6=tfile6.Get("DiMuonNtuple")
ttree7=tfile7.Get("DiMuonNtuple")
tfiled=ROOT.TFile("data16.allYear.sideband.root","OLD")
ttreed=tfiled.Get("DiMuonNtuple")


def dmim(entry):
	muon1=ROOT.TLorentzVector()
	muon2=ROOT.TLorentzVector()
	muon1.SetPtEtaPhiM(entry.Muons_PT_Lead,entry.Muons_Eta_Lead,entry.Muons_Phi_Lead,.11)
	muon2.SetPtEtaPhiM(entry.Muons_PT_Sub,entry.Muons_Eta_Sub,entry.Muons_Phi_Sub,.11)
	return (muon1+muon2).M()
def VCounter(item):
	count = 0
	for a in item:
		if a == 70 or a == 60:
			count += 1
	return count	
def Cutflow(ttree1):
	ChT = ChP = ChAC = ChBB = ChA = ChB = ChC = ChA1 = ChB1 = ChC1 = ChA2 = ChB2 = ChC2 = ChA3 = ChB3 = ChC3 =ChAS=ChBS=ChCS = 0
	BinListA = BinListB = BinListC = {}
	for entry in ttree1:
		ChT+=entry.GlobalWeight
		Dmim = dmim(entry)
		MuonNumber=entry.Muons_Pos_PT.size()+entry.Muons_Neg_PT.size()
		ElectronNumber=entry.Electrons_Pos_PT.size()+entry.Electrons_Neg_PT.size()
		JetsSize=entry.Jets_PT.size()
		BTagJets=entry.Jets_LowestPassedBTagOP
		GW = entry.GlobalWeight
		ChT += GW
		if entry.Muons_Pos_PT.size()==0 or entry.Muons_Neg_PT.size()==0:
			continue	
		ChP += GW
		if MuonNumber==2:
			ChAC += GW
			if ElectronNumber==0:
				ChA += GW
				if JetsSize>=3:
					ChA1 += GW
					if VCounter(BTagJets)>=2:
						ChA2 += GW
						if abs(Dmim - 125.) <= 2.:
							ChA3 += GW
                        else:
                            ChAS += GW

			if ElectronNumber>=1:
				ChC += GW
				if JetsSize>=1:
					ChC1 += GW
					if VCounter(BTagJets)>=1:
						ChC2 += GW
						if abs(Dmim - 125.) <= 2.:
							ChC3 += GW
                        else:
                            ChCS += GW

		if MuonNumber>=3:
			ChBB += GW
			if ElectronNumber==0:
				ChB += GW
				if JetsSize>=1:
					ChB1 += GW
					if VCounter(BTagJets)>=1:
						ChB2 += GW
						if abs(Dmim - 125.) <= 2.:
							ChB3 += GW
                        else:
                            ChBS += GW

	return  [ChAS, ChCS, ChBS]



print Cutflow(ttreed)

# B_i = [sum(x) for x in zip(Cutflow(ttree4),Cutflow(ttree5), Cutflow(ttree6), Cutflow(ttree7))]
# S = Cutflow(ttree0)
# print(S)
# print("B_i = ",B_i)


