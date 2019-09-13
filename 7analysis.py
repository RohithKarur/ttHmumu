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
HistStack = ROOT.THStack("HistSTack","")
Hist0 = ROOT.TH1D("Hist0",";;",100,100.,160.)
Hist1 = ROOT.TH1D("Hist1",";;",100,100.,160.)
Hist2 = ROOT.TH1D("Hist2",";;",100,100.,160.)
Hist3 = ROOT.TH1D("Hist3",";;",100,100.,160.)
Hist4 = ROOT.TH1D("Hist4",";;",100,100.,160.)
Hist5 = ROOT.TH1D("Hist5",";;",100,100.,160.)
Hist6 = ROOT.TH1D("Hist6",";;",100,100.,160.)
Hist7 = ROOT.TH1D("Hist7",";;",100,100.,160.)
Histmain = ROOT.TH1D("HistMain",";;",100,100.,160.)



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

def HistAdder(ttree1,Hist):
	BinList = {}
	for entry in ttree1:
		MuonNumber=entry.Muons_Pos_PT.size()+entry.Muons_Neg_PT.size()
		LeptonNumber=entry.Muons_Pos_PT.size()+entry.Muons_Neg_PT.size()+entry.Electrons_Pos_PT.size()+entry.Electrons_Neg_PT.size()
		JetsSize=entry.Jets_PT.size()
		BTagJets=entry.Jets_LowestPassedBTagOP
		Dmim = dmim(entry)
		if entry.Muons_Pos_PT.size()==0 or entry.Muons_Neg_PT.size()==0:
			continue	
		if LeptonNumber >= 4:
			continue
		if MuonNumber==2 and JetsSize>=3 and VCounter(BTagJets)>=2:
			Hist.Fill(Dmim,entry.GlobalWeight)
			HH = Hist.FindBin(Dmim)
			if HH not in BinList:
				BinList[HH] = entry.GlobalWeight
			elif BinList[HH] >= entry.GlobalWeight:
				BinList[HH] = entry.GlobalWeight
			else:
				pass
		if LeptonNumber>2 and JetsSize>=1 and VCounter(BTagJets)>=1:
			Hist.Fill(Dmim,entry.GlobalWeight)
			HH = Hist.FindBin(Dmim)
			if HH not in BinList:
				BinList[HH] = entry.GlobalWeight
			elif BinList[HH] >= entry.GlobalWeight:
				BinList[HH] = entry.GlobalWeight
			else:
				pass
	for i in BinList:
		Hist.Fill(i, -BinList[i])

	return Hist




		



'''
Histmain=HistAdder(ttree0,Histmain)
Histmain=HistAdder(ttree1,Histmain)
Histmain=HistAdder(ttree2,Histmain)
Histmain=HistAdder(ttree3,Histmain)
Histmain=HistAdder(ttree4,Histmain)
Histmain=HistAdder(ttree5,Histmain)
Histmain=HistAdder(ttree6,Histmain)
Histmain=HistAdder(ttree7,Histmain)

'''
#Histmain=HistAdder(ttree0,Histmain)



Hist0=HistAdder(ttree0,Hist0)
Hist0.SetFillColor(ROOT.kBlack)
Hist0.Scale(100)
Hist1=HistAdder(ttree1,Hist1)
Hist1.SetFillColor(ROOT.kBlue)
Hist1.Scale(50)
Hist2=HistAdder(ttree2,Hist2)
Hist2.SetFillColor(ROOT.kRed)
Hist2.Scale(50)
Hist3=HistAdder(ttree3,Hist3)
Hist3.SetFillColor(ROOT.kBlack)
Hist3.Scale(50)
Hist4=HistAdder(ttree4,Hist4)
Hist4.SetFillColor(ROOT.kGreen)
Hist4.Scale(50)
Hist5=HistAdder(ttree5,Hist5)
Hist5.SetFillColor(ROOT.kMagenta)
Hist6=HistAdder(ttree6,Hist6)
Hist6.SetFillColor(ROOT.kCyan)
Hist7=HistAdder(ttree7,Hist7)
Hist7.SetFillColor(ROOT.kViolet)


HistStack.Add(Hist6)
HistStack.Add(Hist5)
HistStack.Add(Hist7)
HistStack.Add(Hist4)
#HistStack.Add(Hist3)
#HistStack.Add(Hist2)
#HistStack.Add(Hist1)
HistStack.Add(Hist0)

HistStack.Draw("hist")
c.SetLogy()
c.Print("histstack.png")






'''

Histmain.Draw("hist")
c.Print("totaldmimttree0.png")
#c.Print("superimposeddmim.png")
'''
