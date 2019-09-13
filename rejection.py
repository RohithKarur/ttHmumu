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

c=ROOT.TCanvas()

Hist1 = ROOT.TH1D("Hist1",";;",100,0.,200.)
Hist2 = ROOT.TH1D("Hist2",";;",100,0.,200.)
Hist3 = ROOT.TH1D("Hist3",";;",100,0.,200.)
Hist4 = ROOT.TH1D("Hist4",";;",100,0.,200.)
Hist5 = ROOT.TH1D("Hist5",";;",100,0.,200.)
Hist6 = ROOT.TH1D("Hist6",";;",100,0.,200.)
Hist7 = ROOT.TH1D("Hist7",";;",100,0.,200.)
Histmain = ROOT.TH1D("HistMain",";;",100,0.,200.)

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




def RejectCounter(ttree1):
	Total=ttree1.GetEntries()
	Accept=0
	Reject=0
	cut0=0.
	cut1=0.
	cut2=0.
	cut3=0.
	cut4=0.
	cut5=0.
	cut2a=0.
	cut2b=0.
	cut3a=0.
	cut3b=0.
	cut4a=0.
	cut4b=0.
	Great4=0.
	for entry in ttree1:
		Muons_Pos_No=entry.Muons_Pos_PT.size()
		Muons_Neg_No=entry.Muons_Neg_PT.size()
		Elec_Pos_No=entry.Electrons_Pos_PT.size()	
		Elec_Neg_No=entry.Electrons_Neg_PT.size()
		MuonNumber=entry.Muons_Neg_PT.size()+entry.Muons_Pos_PT.size()
		LepNumber=Elec_Pos_No+Elec_Neg_No+Muons_Pos_No+Muons_Neg_No
		BTagJets=entry.Jets_LowestPassedBTagOP

		cut0 += entry.GlobalWeight
		if Muons_Pos_No==0 or Muons_Neg_No==0:
			Reject+=1
			continue
		else:
			cut1 += entry.GlobalWeight
		if MuonNumber==2:
			cut2 += entry.GlobalWeight
			cut2a += entry.GlobalWeight


			if entry.Jets_PT.size()<3:
				continue
			else:
				cut3 += entry.GlobalWeight
				cut3a += entry.GlobalWeight
				if VCounter(BTagJets)<2:
					Reject+=1
					continue
				else:
					cut4 += entry.GlobalWeight
					cut4a += entry.GlobalWeight
					Accept+=1
					if abs(dmim(entry)-125.) <= 2.0:
						cut5 = cut5 + entry.GlobalWeight
		elif entry.Muons_Pos_PT.size()+entry.Muons_Neg_PT.size()>2:
			cut2 = cut2 + entry.GlobalWeight
			cut2b = cut2b + entry.GlobalWeight
			if entry.Muons_Pos_PT.size()+entry.Muons_Neg_PT.size()+entry.Electrons_Pos_PT.size()+entry.Electrons_Neg_PT.size() >= 4:
				Great4 += entry.GlobalWeight
				continue
			if entry.Jets_PT.size()<1:
				Reject+=1
				continue
			else:
				cut3 = cut3 + entry.GlobalWeight
				cut3b += entry.GlobalWeight
				if VCounter(BTagJets)<1:
					Reject+=1
					continue
				else:
					cut4 = cut4 + entry.GlobalWeight
					cut4b += entry.GlobalWeight
					Accept+=1
					if abs(dmim(entry)-125.) <= 2.0:
						cut5 = cut5 + entry.GlobalWeight
		

	return cut0, cut1, cut2, cut2a, cut2b, cut3, cut3a, cut3b,cut4, cut4a, cut4b,cut5, Great4

def Sideband(ttree):
    return Reject
'''
R0=RejectCounter(ttree0)
R1=RejectCounter(ttree1)
R2=RejectCounter(ttree2)
R3=RejectCounter(ttree3)
R4=RejectCounter(ttree4)
R5=RejectCounter(ttree5)
R6=RejectCounter(ttree6)
R7=RejectCounter(ttree7)
print R0
print R1
print R2
print R3
print R4
print R5
print R6
print R7
'''
R1=RejectCounter(ttree0)
print R1
