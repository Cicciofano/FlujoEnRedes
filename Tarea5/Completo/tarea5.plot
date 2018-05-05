set term eps
set output 'tarea5.eps'
set xrange [0: 4]
set yrange [0: 4]
set pointsize .5
set size square
set key off
set arrow 1 from 1, 1 to 1, 2 nohead
set arrow 2 from 1, 2 to 1, 1 nohead
set arrow 3 from 3, 1 to 2, 1 nohead
set arrow 4 from 2, 1 to 2, 2 nohead
set arrow 5 from 2, 2 to 2, 1 nohead
set arrow 6 from 3, 1 to 3, 2 nohead
set arrow 7 from 3, 2 to 3, 1 nohead
set arrow 8 from 1, 2 to 2, 2 nohead
set arrow 9 from 2, 2 to 1, 2 nohead
set arrow 10 from 2, 3 to 2, 2 nohead
set arrow 11 from 3, 2 to 3, 3 nohead
set arrow 12 from 1, 3 to 2, 3 nohead
set arrow 13 from 2, 3 to 1, 3 nohead
set arrow 14 from 3, 3 to 2, 3 nohead
show arrow
plot 'cuadricula.dat' using 1:2:3 with points pt 5 lc var
quit()
