!# /bin/bash

python3 userinterface.py > intermediate.dat &

wait

echo "$(cat intermediate.dat)"python3 hail_mary.py > input.txt &

wait

./run

