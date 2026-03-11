import time

class SampleSDL:   
    def get_phase(self, temperature: float, pressure: float) -> int:
        """
        指定された温度・圧力に対応する相を求める
        0: 固相, 1: 液相, 2: 気相
        """
        time.sleep(1)

        t_triple = 0
        p_triple = 5000
        slope = 50
        
        boundary = slope * (temperature - t_triple) + p_triple
        
        if pressure < boundary:
            return 2
        else:
            if temperature < t_triple:
                return 0
            else:
                return 1