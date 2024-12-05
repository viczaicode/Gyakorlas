class Hatoslotto:
 
 def __init__(self, huzas:int,ev:int,het:int,szam:int):
  self.huzas = int(huzas)
  self.ev = int(ev)
  self.het = int(het)
  self.szam = int(szam)

 def __str__(self):
  return f"Húzás: {self.huzas}, Év: {self.ev}, Hét: {self.het}, Szám: {self.szam}"