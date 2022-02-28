from pymatgen.ext.matproj import MPRester
import re
from pymatgen.io.cif import CifWriter
import numpy as np
import pickle
from tqdm import tqdm


if __name__ == '__main__':
    with open("all_mp_id.pkl", "rb+") as f:
        all_mp_id_lst = pickle.load(f)
    all_mp_id_lst.sort(key=lambda x: int(x.split("-")[-1]))
    mpr = MPRester("OnQDHiVv3hzqx6p2")
    # print(all_mp_id_lst)
    step = 20000
    print(len(all_mp_id_lst))
    for i in range(6, len(all_mp_id_lst) // step + 1, step):
        requrest_lst = all_mp_id_lst[i * step: (i + 1) * step]
        print(requrest_lst  )
        entries = mpr.query({"material_id": {"$in": requrest_lst}},
                            ["material_id", "cif", "pretty_formula"]) # pretty_formula->reduced formula, full_formula->full formula
        data = []
        data.extend(entries)
        print(len(data))
        for d in data:
            with open("../data/unit_cell/{}-{}.cif".format(d["pretty_formula"], d["material_id"]), 'w') as f:
                f.write(d["cif"])
