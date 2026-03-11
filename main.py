import ivoryos

from sample_sdl import SampleSDL

# SDLクラスのインスタンス作成
sdl = SampleSDL()

if __name__ == "__main__":
    ivoryos.run(__name__, port=8888)