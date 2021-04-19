import cmd
import arvausStore

class commandShell(cmd.Cmd):

    def __init__(self, tarkastaja, arvausStore):
        super().__init__()
        self.tarkastaja = tarkastaja
        self.arvausStore = arvausStore
        self.completekey = 'tab'

    def do_list(self, arg):
        'Listaa kaikki saapuneet oikeat arvaukset'
        items = self.arvausStore.getAll()
        print(items)


    def do_status(self, arg):
        'Printtaa status info'
        arvattava = self.tarkastaja.saa_arvattava()
        print('Arvattava laulu: ')
        print(arvattava)

    def do_changeguess(self, arg):
        'Aseta uusi arvaus ja poista tiedoista edellisen arvauksen vastaukset'
        self.tarkastaja.aseta_arvattava(arg)
        arvausStore.clear()

    def do_sendresponse(self, arg):
        'Lähetä template viesti viidelle parhaalle'
        pass

    def do_first_5(self, arg):
        'Printtaa viisi ensimmäistä'
        items = self.arvausStore.getWinners()
        print(items)

    def emptyline(self):
        pass
