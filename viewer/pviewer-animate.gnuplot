set view 60,i*dt
splot "path.csv" w li
i=i+1
if (i<n) reread
