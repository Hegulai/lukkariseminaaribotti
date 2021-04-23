import cmd
import arvausStore

class commandShell(cmd.Cmd):

    def __init__(self, tarkastaja, arvausStore, bot):
        super().__init__()
        self.intro = "Botti käynnistetty. help -komento auttaa"
        self.tarkastaja = tarkastaja
        self.arvausStore = arvausStore
        self.completekey = 'tab'
        self.bot = bot

    def do_list(self, arg):
        'Listaa kaikki saapuneet oikeat arvaukset'
        items = self.arvausStore.getAll()
        print(items)


    def do_status(self, arg):
        'Printtaa status info'
        arvattava = self.tarkastaja.saa_arvattava()
        allResponses = self.arvausStore.getAll()
        correctResponses = self.arvausStore.getWinners()
        print('Arvattava laulu: ' + arvattava)
        print('Vastauksia tullut: ' + str(len(allResponses)))
        print('Oikeita vastauksia tullut: ' + str(len(correctResponses)))

    def do_changeguess(self, arg):
        'Aseta uusi arvaus ja poista tiedoista edellisen arvauksen vastaukset'
        self.tarkastaja.aseta_arvattava(arg)
        arvausStore.clear()

    def do_sendresponse(self, arg):
        'Lähetä template viesti viidelle parhaalle'
        winners = self.arvausStore.getWinners()
        i = 1
        for winner in winners:
            text = "Hei, vastauksesi on oikein ja olet odottamassa sijalla " + str(i) + ". Ole valppaana, oikein vastanneille soitetaan Telegram-puhelu vastausjärjestyksessä, ja ensimmäinen puheluun vastannut pääsee lähetykseen."
            self.bot.send_message(
                chat_id=winner[1], text=text)
            i += 1

        others = self.arvausStore.getOthers()
        for other in others:
            text = "Hei, viisi nopeiten oikein vastannutta on nyt valittu ja et valitettavasti ole heidän joukossaan tällä kertaa."
            self.bot.send_message(
                chat_id=other[1], text=text)


    def do_first_5(self, arg):
        'Printtaa viisi ensimmäistä'
        items = self.arvausStore.getWinners()
        print(items)

    def do_list_others(self, arg):
        'Printtaa muut paitsi viisi ensimmäistä'
        items = self.arvausStore.getOthers()
        print(items)

    def emptyline(self):
        pass
