reset
set term gif animate delay 10
set datafile separator ";"
set output "outp.gif"
n=360
dt=360/n
i=0
load "pviewer-animate.gnuplot"
set output

