#!/bin/bash
module load cuda/12 amber/22

if [ "$#" -ne 4 ]; then
        echo "Usage: $0 <prmtop_file> <trajectory_file> <rmsf_output_file>"
        exit 1
fi

PARMTOP=$1
TRAJ=$2
RMSFOUT=$3

cat << EOF > rmsf_temp.in
parm $PARMTOP
trajin $TRAJ 30001 100000 100
rms Run1 :1045-1054,1062-1076,1083-1111,1119-1128,1178-1189,1197-1211,1219-1246,1254-1264,342-369,694-721@CA first
average crdset MyAvg
run
rms ref MyAvg
atomicfluct :525-646&!@H= byres out $RMSFOUT
go
quit
EOF

cpptraj -i rmsf_temp.in

rm rmsf_temp.in