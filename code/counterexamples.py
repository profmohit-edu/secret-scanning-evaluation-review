"""Analytical examples only. No scanners, credentials, or empirical data are used."""
from fractions import Fraction as F
import json
from pathlib import Path

def metrics(found,total):
 assert 0<=found<=total and total>0
 return {'numerator':found,'denominator':total,'fraction':str(F(found,total)),'decimal':float(F(found,total))}
a={'conditional':metrics(45,50),'source':metrics(45,100)}
b={'conditional':metrics(72,90),'source':metrics(72,100)}
assert F(45,50)>F(72,90) and F(45,100)<F(72,100)
assert F(50,100)*F(45,50)==F(45,100)
assert F(90,100)*F(72,90)==F(72,100)
x={'occurrence':metrics(100,109),'value':metrics(1,10)}
y={'occurrence':metrics(10,109),'value':metrics(10,10)}
assert F(100,109)>F(10,109) and F(1,10)<F(10,10)
old={'A':metrics(10,10),'B':metrics(5,10)}
new={'A':metrics(10,20),'B':metrics(15,20)}
assert F(10,10)>F(5,10) and F(10,20)<F(15,20)
out={'scope':'three constructed arithmetic examples; no empirical detector validation','stage_example':{'A':a,'B':b},'unit_example':{'A':x,'B':y},'benchmark_extension':{'old':old,'expanded':new}}
if __name__=='__main__':
 p=Path(__file__).resolve().parents[1]/'counterexample_results.json';p.write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
