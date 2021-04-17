class arvauksen_tarkastaja:
    def __init__(self):
        self.arvattava = ""
        self.pisteet = {}
        self.piste_arvaus = 1
        self.piste_oikein = 5

    def aseta_arvattava(self, arvattava):
        self.arvattava = arvattava

    def on_oikea_arvaus(self, arvaus):
        return self.arvattava == arvaus

    def saa_arvattava(self):
        return self.arvattava

    #def arvaa(self, arvaus, nickname):
    #   self.pisteet.get(key[, -1])
        