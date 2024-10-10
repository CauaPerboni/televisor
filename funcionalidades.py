class Televisor:
    def __init__(self, fab, modelo):
        self.fabricante = fab
        self.modelo = modelo
        self.canal_atual = None
        self.lista_de_canais = []
        self.volume = 20
        self.volume_antes_mute = None  # Para armazenar o volume antes do mute
        self.ligada = False  # TV começa desligada

    def ligaDesliga(self):
        self.ligada = not self.ligada
        estado = "ligada" if self.ligada else "desligada"
        print(f"TV {estado}.")

    def aumentaVolume(self, valor):
        if self.ligada:
            if self.volume + valor <= 100:
                self.volume += valor
            else:
                self.volume = 100
            print(f"Volume aumentado para {self.volume}")
        else:
            print("A TV está desligada.")

    def diminuiVolume(self, valor):
        if self.ligada:
            if self.volume - valor >= 0:
                self.volume -= valor
            else:
                self.volume = 0
            print(f"Volume diminuído para {self.volume}")
        else:
            print("A TV está desligada.")

    def trocaCanal(self, canal):
        if self.ligada:
            if canal in self.lista_de_canais:
                self.canal_atual = canal
                print(f"Canal trocado para: {self.canal_atual}")
            else:
                print("Canal não encontrado")
        else:
            print("A TV está desligada.")

    def sintonizaCanal(self, canal):
        if len(self.lista_de_canais) < 100:  # Limite de 100 canais
            if canal not in self.lista_de_canais:
                self.lista_de_canais.append(canal)
                print(f"Canal {canal} sintonizado.")
            else:
                print(f"O canal {canal} já está sintonizado.")
        else:
            print("Limite de canais atingido.")

    def mute(self):
        if self.ligada:
            if self.volume != 0:
                self.volume_antes_mute = self.volume
                self.volume = 0
                print("TV silenciada.")
            else:
                print("A TV já está no mudo.")
        else:
            print("A TV está desligada.")

    def unmute(self):
        if self.ligada:
            if self.volume == 0 and self.volume_antes_mute:
                self.volume = self.volume_antes_mute
                print(f"Volume restaurado para {self.volume}")
            else:
                print("A TV não está no mudo.")
        else:
            print("A TV está desligada.")

    def exibeInformacoes(self):
        estado = "ligada" if self.ligada else "desligada"
        print(f"TV {estado}")
        print(f"Fabricante: {self.fabricante}")
        print(f"Modelo: {self.modelo}")
        print(f"Volume atual: {self.volume}")
        print(f"Canal atual: {self.canal_atual if self.canal_atual else 'Nenhum'}")
        print(f"Canais sintonizados: {', '.join(self.lista_de_canais) if self.lista_de_canais else 'Nenhum'}")

class ControleRemoto:
    def __init__(self, tv):
        self.tv = tv

    def aumentaVolume(self, valor=10):
        self.tv.aumentaVolume(valor)

    def diminuiVolume(self, valor=10):
        self.tv.diminuiVolume(valor)

    def trocaCanal(self, canal):
        self.tv.trocaCanal(canal)

    def sintonizaCanal(self, canal):
        self.tv.sintonizaCanal(canal)

    def mute(self):
        self.tv.mute()

    def unmute(self):
        self.tv.unmute()

    def ligaDesliga(self):
        self.tv.ligaDesliga()

    def exibeInformacoes(self):
        self.tv.exibeInformacoes()
