# Terminal CLI Dataset check

The aim of this page is to provide a few lines of commands that can be used quickly in the context of DataScience.


## Approach
1. From Seaborn's Titanic dataset, we will export it to a CSV file (main.py)
2. This CSV file will be our starting point. It simulates a dataset that we would have received in order to process it.
3. With Zsh, the aim is just to do a quick check of this CSV before pre-processing it with python.

## Shape of file
* Count lines-chars-Largest line width : 
```
  > wc -lcL < snstitanic.csv
```
* Unique lines (exclude index) : 
```
  > cut -d',' -f2- snstitanic.csv | sort | uniq | wc -l 
```
## Sed 
* Filter lines 10 to 12 : 
```
  > sed -n '10,12p' snstitanic.csv 
```
* Filter pattern "First":
```
  > sed -n '/First/p' snstitanic.csv  
```
## Awk
* Filter lines with number line : 
``` 
  > awk 'NR==5, NR==12  { print NR ":" $0}' snstitanic.csv   
```

* Filter pattern "First" in specific field:
```
  > awk -F','  '$10 ~ /First/ {print "Line " NR ":" $0}' snstitanic.csv  
```

### Documentation
* Awk : https://www.gnu.org/software/gawk/manual/gawk.pdf
* Sed : https://www.gnu.org/software/sed/manual/sed.pdf
* Scripts Shell Linux et Unix, Christophe Blaess, ISBN : 978212135794
* https://www.blaess.fr/christophe/livres/