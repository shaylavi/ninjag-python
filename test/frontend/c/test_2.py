import ninjag
import os
from read_all import read_all


def test():
    f_inputs = [
        "input/in1_const.yaml",
        "input/in1_rules.yaml",
        "input/in1_tasks.yaml",
        ]
    f_answer = "output/out1_combined.ninja"
    f_solution = "solution/sol1.ninja"
    cmd = " ".join(["ninjag", f_answer, *f_inputs])
    os.system(cmd)
    answer = read_all(f_answer)
    solution = read_all(f_solution)
    assert answer == solution
