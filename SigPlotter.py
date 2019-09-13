from ROOT import TCanvas, TGraph, TPaveText,kBlack
from ROOT import gROOT
from array import array

c1 = TCanvas( 'c1', 'A Simple Graph with error bars', 200, 10, 700, 500 )

c1.SetGrid()
c1.GetFrame().SetFillColor( 21 )
c1.GetFrame().SetBorderSize( 12 )
Z = 0.0395
n = 50;
x  = array( 'f' )
y  = array( 'f' )

for i in range(n):
	x.append(i)
	y.append((x[i])**.5*Z) 

gr = TGraph( n, x, y )
gr.SetTitle( 'TGraphErrors Example' )
gr.SetMarkerColor( 4 )
gr.SetMarkerStyle( 21 )
gr.GetXaxis().SetTitle('L #times [80 fb^{-1}]')
gr.GetYaxis().SetTitle('Significance')
t = TDraw()
t.SetNDC()
t.SetTextFont(1)
t.SetTextSize(0.05)
t.SetTextAlign(12)
t.SetTextColor(kBlack)
t.DrawLatex(.4, .4, 'At 80 fb^{-1}, Sig = %.3f' % Z)
aa = (350./80.)**.5*Z
t.DrawLatex(.4, .5, 'At 350 fb^{-1}, Sig = %.3f' % aa)


gr.Draw('ACPL')

c1.Print('SigPlot.png')
