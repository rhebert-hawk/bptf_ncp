#!/bin/bash
module load cuda/12 amber/22
if [ "$#" -ne 6 ]; then
        echo "Usage: $0 <data_file1> <data_file2> <data_file3> <data_file4> <data_file5> <output_data_file>"
        exit 1
fi

DAT1=$1
DAT2=$2
DAT3=$3
DAT4=$4
DAT5=$5
OUT=$6

cat << EOF > rmsf_temp.in
readdata $DAT1
readdata $DAT2
readdata $DAT3
readdata $DAT4
readdata $DAT5
avg $DAT1:2 $DAT2:2 $DAT3:2 $DAT4:2 $DAT5:2 oversets out $OUT
go
quit
EOF

cpptraj -i rmsf_temp.in

rm rmsf_temp.in
