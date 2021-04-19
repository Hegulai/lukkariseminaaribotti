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
        correctResponses = self.arvausStore.getAll()
        print('Arvattava laulu: ' + arvattava)
        print('Oikeita vastauksia tullut: ' + str(len(correctResponses)))

    def do_changeguess(self, arg):
        'Aseta uusi arvaus ja poista tiedoista edellisen arvauksen vastaukset'
        self.tarkastaja.aseta_arvattava(arg)
        arvausStore.clear()

    def do_sendresponse(self, arg):
        'Lähetä template viesti viidelle parhaalle'
        items = self.arvausStore.getWinners()
        i = 1
        for item in items:
            text = "Hei, vastauksesi on oikein ja olet odottamassa sijalla " + str(i) + ". Ole valppaana, oikein vastanneille soitetaan Telegram-puhelu vastausjärjestyksessä, ja ensimmäinen vastannut pääsee lähetykseen."
            self.bot.send_message(
                chat_id=item[1], text=text)
            i += 1

    def do_first_5(self, arg):
        'Printtaa viisi ensimmäistä'
        items = self.arvausStore.getWinners()
        print(items)

    def emptyline(self):
        pass
