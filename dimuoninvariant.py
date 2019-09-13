import ROOT

ROOT.gROOT.SetBatch(1)
ROOT.gStyle.SetOptStat(0)

tfile=ROOT.TFile("mc16d.364253.root","OLD")
ttree=tfile.Get("DiMuonNtuple")
c=ROOT.TCanvas()
dummy = ROOT.TH1D( "dummy", "Di-Muon Invariant Mass Spectrum;m_{#mu #mu}(GeV);Events", 100,0., 200. )

for entry in ttree:
	muon1=ROOT.TLorentzVector()
	muon1.SetPtEtaPhiM(entry.Muons_PT_Lead,entry.Muons_Eta_Lead,entry.Muons_Phi_Lead,.11)
	muon2=ROOT.TLorentzVector()
	muon2.SetPtEtaPhiM(entry.Muons_PT_Sub,entry.Muons_Eta_Sub,entry.Muons_Phi_Sub,.11)	
	dmim=(muon1+muon2).M()
	dummy.Fill(dmim)

dummy.SetFillColor(kBlack)
dummy.Draw("hist")
c.Print("hello.png")
