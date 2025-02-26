#!/bin/bash
# Count the number of lines containing the word "python" in CSV files
grep -i "python" *.csv | wc -l
