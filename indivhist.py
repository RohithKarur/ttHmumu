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

c=ROOT.TCanvas()

ChA = ROOT.TH1D("Hist7",";;",60,100.,160.)
ChB = ROOT.TH1D("Hist7",";;",60,100.,160.)
ChC = ROOT.TH1D("Hist7",";;",60,100.,160.)

ChAStack = ROOT.THStack("ChAStack","")
ChBStack = ROOT.THStack("ChBStack","")
ChCStack = ROOT.THStack("ChCStack","")

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
def HistAdder(ttree1,ChA,ChB,ChC):
	ChT= ChP= M2= M2E0= M2E0J3= M2E0J3B2= M2= M2E1= M2E1J1= M2E1J1B1= M3= M3E1= M3E1J1= M3E1J1B1=0
	BinListA = BinListB = BinListC = {}
	for entry in ttree1:
		ChT+=entry.GlobalWeight
		Dmim = dmim(entry)
		MuonNumber=entry.Muons_Pos_PT.size()+entry.Muons_Neg_PT.size()
		ElectronNumber=entry.Electrons_Pos_PT.size()+entry.Electrons_Neg_PT.size()
		JetsSize=entry.Jets_PT.size()
		BTagJets=entry.Jets_LowestPassedBTagOP


		if entry.Muons_Pos_PT.size()==0 or entry.Muons_Neg_PT.size()==0:
			continue	
		ChP+=entry.GlobalWeight
		if MuonNumber==2:
			M2 += entry.GlobalWeight
			if ElectronNumber==0:
				M2E0 += entry.GlobalWeight
				if JetsSize>=3:
					M2E0J3 += entry.GlobalWeight
					if VCounter(BTagJets)>=2:
						M2E0J3B2 += entry.GlobalWeight
						ChA.Fill(Dmim,entry.GlobalWeight)
						HHA = ChA.FindBin(Dmim)
						if HHA not in BinListA:
							BinListA[HHA] = entry.GlobalWeight
						elif BinListA[HHA] >= entry.GlobalWeight:
							BinListA[HHA] = entry.GlobalWeight
						else:
							pass
			if ElectronNumber>=1:
				M2E1 += entry.GlobalWeight
				if JetsSize>=1:
					M2E1J1 += entry.GlobalWeight
					if VCounter(BTagJets)>=1:
						M2E1J1B1 += entry.GlobalWeight
						ChC.Fill(Dmim,entry.GlobalWeight)

						HHB = ChB.FindBin(Dmim)
						if HHB not in BinListB:
							BinListB[HHB] = entry.GlobalWeight
						elif BinListA[HHB] >= entry.GlobalWeight:
							BinListB[HHB] = entry.GlobalWeight
						else:
							pass
		if MuonNumber>=3:
			M3 += entry.GlobalWeight
			if ElectronNumber==0:
				M3E1 += entry.GlobalWeight
				if JetsSize>=1:
					M3E1J1 += entry.GlobalWeight
					if VCounter(BTagJets)>=1:
						M3E1J1B1 += entry.GlobalWeight
						ChB.Fill(Dmim,entry.GlobalWeight)

						HHC = ChC.FindBin(Dmim)
						if HHC not in BinListC:
							BinListC[HHC] = entry.GlobalWeight
						elif BinListA[HHC] >= entry.GlobalWeight:
							BinListC[HHC] = entry.GlobalWeight
						else:
							pass
	#return ChT, M2E0, M3E1, M2E1
	for i in BinListA:
		ChA.Fill(i, -BinListA[i])
	for i in BinListB:
		ChB.Fill(i, -BinListB[i])
	for i in BinListC:
		ChC.Fill(i, -BinListC[i])
	return ChA, ChB, ChC

for i in [ttree7,ttree6,ttree5,ttree4,ttree3,ttree2,ttree1,ttree0]:
	ChA, ChB, ChC = HistAdder(i,ChA,ChB,ChC)
	if i == ttree7:
		ChA.SetFillColor(ROOT.kViolet)
		ChB.SetFillColor(ROOT.kViolet)
		ChC.SetFillColor(ROOT.kViolet)
	if i == ttree6:
		ChA.SetFillColor(ROOT.kCyan)
		ChB.SetFillColor(ROOT.kCyan)
		ChC.SetFillColor(ROOT.kCyan)
	if i == ttree5:
		ChA.SetFillColor(ROOT.kMagenta)
		ChB.SetFillColor(ROOT.kMagenta)
		ChC.SetFillColor(ROOT.kMagenta)
	if i == ttree4:
		ChA.SetFillColor(ROOT.kGreen)
		ChB.SetFillColor(ROOT.kGreen)
		ChC.SetFillColor(ROOT.kGreen)
	if i == ttree3:
		ChA.SetFillColor(ROOT.kBlack)
		ChB.SetFillColor(ROOT.kBlack)
		ChC.SetFillColor(ROOT.kBlack)
	if i == ttree2:
		ChA.SetFillColor(ROOT.kRed)
		ChB.SetFillColor(ROOT.kRed)
		ChC.SetFillColor(ROOT.kRed)
	if i == ttree1:
		ChA.SetFillColor(ROOT.kBlue)
		ChB.SetFillColor(ROOT.kBlue)
		ChC.SetFillColor(ROOT.kBlue)
	if i == ttree0:
		ChA.SetFillColor(ROOT.kYellow)
		ChA.Scale(100)
		ChB.SetFillColor(ROOT.kYellow)
		ChC.SetFillColor(ROOT.kYellow)
	ChAStack.Add(ChA)
	ChBStack.Add(ChB)
	ChCStack.Add(ChC)

	ChA = ROOT.TH1D("Hist7",";;",60,100.,160.)
	ChB = ROOT.TH1D("Hist7",";;",60,100.,160.)
	ChC = ROOT.TH1D("Hist7",";;",60,100.,160.)
	
			
ChAStack.Draw("hist")
c.Print("ChAFullStack.png")
ChBStack.Draw("hist")
c.Print("ChBFullStack.png")
ChCStack.Draw("hist")
c.Print("ChCFullStack.png")


'''
ChA.Draw("E")
c.Print("ttree0ChA.png")
ChB.Draw("E")
c.Print("ttree0ChB.png")
ChC.Draw("E")
c.Print("ttree0ChC.png")
'''
