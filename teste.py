from funcionalidades import *

tv = Televisor('SONY', 'SONY123')
controle = ControleRemoto(tv)

controle.ligaDesliga()

controle.exibeInformacoes()

controle.sintonizaCanal('SBT')
controle.sintonizaCanal('Globo')
controle.sintonizaCanal('Record')

controle.trocaCanal('SBT')

controle.aumentaVolume(15)
controle.diminuiVolume(5)

controle.mute()
controle.unmute()

controle.exibeInformacoes()

controle.ligaDesliga()

controle.aumentaVolume(10)
