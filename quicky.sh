#! /bin/sh
echo "\n Count lines-chars-Largest line width"
echo $(exec wc -lcL "$1")

echo "\n Unique lines (exclude index)"
echo $(cut -d',' -f2- "$1" | sort | uniq | wc -l)


echo "\nShow first five lines:"
echo $(exec head "$1")


echo "\n Sed : Filter lines 10 to 12"
echo $(sed -n '10,12p' "$1" )

echo "\n Sed : Filter lines 10 to 12"
echo $(sed -n '/First/p' "$1" | head -n 2 )


echo "\n Awk :Filter lines with number line"
echo $(awk 'NR==5, NR==12  { print NR ":" $0}' "$1" )

echo "\n Awk :FFilter pattern "First" in specific field"
echo $(awk -F','  '$10 ~ /First/ {print "Line " NR ":" $0}'  "$1" | head -n 2)

