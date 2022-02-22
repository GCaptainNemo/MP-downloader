from pymatgen.ext.matproj import MPRester
import re
from pymatgen.io.cif import CifWriter
import numpy as np
import pickle




class CifDownload:
    def __init__(self):
        # self.mp_rest_obj = MPRester("pc0rARlba5Ae3SArM09")
        self.mp_rest_obj = MPRester("OnQDHiVv3hzqx6p2")

    def to_cif(self, id, flag=True):
        if flag:
            id = 'mp-' + str(id)
        conventional_structure = self.mp_rest_obj.get_structure_by_material_id(id,
                                                                               conventional_unit_cell=True)
        # conventional_structure = self.mp_rest_obj.get_structure_by_material_id(id)

        cif_writer_obj = CifWriter(conventional_structure, write_magmoms=True)
        material = re.findall('Full\sFormula\s(.*?)\n', str(conventional_structure))[0].lstrip('(').rstrip(')')
        name = material + "-" + str(id)
        cif_writer_obj.write_file(r'../data/conventional_cell/{}.cif'.format(name))


if __name__ == '__main__':
    cif_download_obj = CifDownload()
    # 324854
    with open("all_mp_id.pkl", "rb+") as f:
        all_mp_id_lst = pickle.load(f)
    all_mp_id_lst.sort(key=lambda x: int(x.split("-")[-1]))
    print(all_mp_id_lst)
   
    for i in all_mp_id_lst:
        num = int(i.split("-")[-1])
        if num < 350000:
            continue
        print(i)
        # mp-350000 的后一个是 504097(裂开)
        try:
            cif_download_obj.to_cif(i, flag=False)
        except Exception as e:
            # ...
            print(e)