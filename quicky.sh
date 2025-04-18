#! /bin/sh
echo "\n Count lines-chars-Largest line width"
wc -lcL "$1"

echo "\n Unique lines (exclude index)"
cut -d',' -f2- "$1" | sort | uniq | wc -l


echo "\nShow first five lines:"
head "$1"


echo "\n Sed : Filter lines 10 to 12"
sed -n '10,12p' "$1"

echo "\n Sed : Filter lines 10 to 12"
sed -n '/First/p' "$1" | head -n 3 


echo "\n Awk :Filter lines with number line"
awk 'NR==5, NR==12  { printf "%d : %s \n",NR,$0 }' "$1"

echo "\n Awk :Filter pattern "First" in specific field"
awk -F','  '$10 ~ /First/ {printf "Line  %d : %s \n",NR,$0}'  "$1" | head -n 3

