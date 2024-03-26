all: fetch split cleanfetch genplot

fetch:
	python3 fetch.py > fetchout.csv

split:
	python3 split.py < fetchout.csv

cleanfetch:
	del /F /Q fetchout.csv

genplot:
	python3 genplot_all.py
