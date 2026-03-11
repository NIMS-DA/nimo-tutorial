import csv
import shutil

import nimo

from sample_sdl import SampleSDL

# SDLクラスのインスタンス作成
sdl = SampleSDL()

if __name__ == "__main__":
    # 目的関数の数を指定
    n_objectives = 1

    #一度のサイクルで探索アルゴリズムが提案する条件数を指定
    n_proposals = 1

    # サイクル数を指定
    n_cycles = 20

    # 実験条件をリスト化したファイルを指定
    candidates_file = "./candidates.csv"
    candidates_template_file = "./candidates_template.csv"
    shutil.copy(candidates_template_file, candidates_file)

    # 予備実験の結果から推定される相図を作成
    nimo.visualization.plot_phase_diagram.plot(input_file = candidates_file)

    # 探索アルゴリズムが提案する条件を記載するファイルを指定
    proposals_file = "./proposals.csv"

    for K in range(n_cycles):

        print("Start cycle", K+1)

        # 探索アルゴリズムの実行
        nimo.selection(method = "PDC",
                        input_file = candidates_file,
                        output_file = proposals_file,
                        num_objectives = n_objectives,
                        num_proposals = n_proposals)

        # 提案ファイルの読み込み
        with open(proposals_file, newline="") as f:
            reader = csv.DictReader(f)

            # 提案ファイルの各行ごとに実験を実行
            objs = []
            for row in reader:
                temperature = float(row["temperature"])
                pressure = float(row["pressure"])
                result = sdl.get_phase(temperature, pressure)
                objs.append(result)

        # 実験条件ファイルの更新
        nimo.output_update(input_file = proposals_file,
                           output_file = candidates_file,
                           num_objectives = n_objectives,
                           objective_values = objs)

        # 各サイクルの相図を出力
        nimo.visualization.plot_phase_diagram.plot(input_file = candidates_file)