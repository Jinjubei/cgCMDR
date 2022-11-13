class Player:
  def __init__(self,name,MMR):
    self.name = name
    self.MMR = MMR
#TODO: algorithim for determining MMR
  def set_mmr(self,placement):
    self.MMR = self.MMR+placement
