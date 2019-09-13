# AtlasPrelims
This is practice code for Atlas data analysis

The important code is written in PyROOT and is organized as follows:

There is data acquisition and analysis code, which draws upon real data/ MC simulations whose information is given by the site : http://www-pnp.physics.ox.ac.uk/~zgubic/v17_documentation/samples.txt

The files are:

7analysis.py (stacks separate signal/background decays from several ROOT files to create a stacked histogram)

dimuoninvariant.py (returns plot of the background di-muon Invariant Mass Spectrum)

indivcutflow.py (returns cutflow list do help debug code in $$H \mu \mu$$ decay)

indivhist.py ( returns stacked/ or solitary histogram describign different channels of $H \mu \mu $ decay)

rejection.py (clumsy way of documenting cutflow)

The .png files are labelled clearly as to what they represent.

Channel A allows 2muons, 0electrons

Channel B allows 3muons, 0electrons

Channel C allows 2muons, 1electrons
