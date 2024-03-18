unbuffer python3 tools/execsnoop.py -T | python3 parsers/parser.py execsnoop 6 
#unbuffer python3 ../tools/exitsnoop.py -t | python3 parser.py exitsnoop 7 &
#unbuffer python3 ../tools/gethostlatency.py | python3 parser.py gethostlatency 5 &
#unbuffer python3 ../tools/tcpconnect.py -d | python3 parser.py tcpconnect 7 &
#unbuffer python3 ../tools/tcprtt.py -i 5 | python3 histogram-parser.py tcprtt &
#unbuffer python3 ../tools/runqlat.py 5 | python3 histogram-parser.py runqlat &
#unbuffer python3 ../tools/tcplife.py -T | python3 parser.py tcplife 10  &
#unbuffer python3 ../tools/cpudist.py 5 | python3 histogram-parser.py cpudist  &
#unbuffer python3 ../tools/biolatency.py -Q 5 | python3 histogram-parser.py biolatency

