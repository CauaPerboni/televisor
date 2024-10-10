import unittest
from funcionalidades import Televisor, ControleRemoto

class TestTelevisor(unittest.TestCase):
    def setUp(self):
        self.tv = Televisor('SONY', 'SONY123')
        self.controle = ControleRemoto(self.tv)

    def test_aumenta_volume(self):
        self.controle.ligaDesliga()  # Liga a TV
        self.controle.aumentaVolume(10)
        self.assertEqual(self.tv.volume, 30)

    def test_diminui_volume(self):
        self.controle.ligaDesliga()  # Liga a TV
        self.controle.aumentaVolume(30)
        self.controle.diminuiVolume(10)
        self.assertEqual(self.tv.volume, 20)

    def test_troca_canal(self):
        self.controle.ligaDesliga()  # Liga a TV
        self.controle.sintonizaCanal('SBT')
        self.controle.trocaCanal('SBT')
        self.assertEqual(self.tv.canal_atual, 'SBT')

    def test_mute(self):
        self.controle.ligaDesliga()  # Liga a TV
        self.controle.aumentaVolume(50)
        self.controle.mute()
        self.assertEqual(self.tv.volume, 0)

    def test_unmute(self):
        self.controle.ligaDesliga()  # Liga a TV
        self.controle.aumentaVolume(50)
        self.controle.mute()
        self.controle.unmute()
        self.assertEqual(self.tv.volume, 50)

if __name__ == "__main__":
    unittest.main()
