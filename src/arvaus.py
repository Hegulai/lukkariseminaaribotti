import string

def parse(text):
    parsed = text.strip().lower()
    for p in string.punctuation:
        parsed = parsed.replace(p, '')
    return parsed

class arvauksen_tarkastaja:
    def __init__(self):
        self.arvattava = ""
        self.pisteet = {}
        self.piste_arvaus = 1
        self.piste_oikein = 5

    def aseta_arvattava(self, arvattava):
        self.arvattava = parse(arvattava)

    def on_oikea_arvaus(self, arvaus):
        return self.arvattava == parse(arvaus)

    def saa_arvattava(self):
        return self.arvattava

    #def arvaa(self, arvaus, nickname):
    #   self.pisteet.get(key[, -1])
