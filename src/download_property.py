from tqdm import tqdm
from pymatgen.ext.matproj import MPRester
import pickle
import os
import json


def get_criterion_json(criterion_lst, input_dir="../data/tetrahedron_124657_csm/", is_save=True,
                       output_json_address="query.json"):
    """
    把query的criterion保存进json文件
    注意：query的顺序和查询的顺序不一致
    """
    mpr = MPRester("OnQDHiVv3hzqx6p2")
    file_lst = os.listdir(input_dir)
    cif_file_lst = [file for file in file_lst if file.split(".")[-1] == "cif"]
    mp_id_lst = ["-".join(file.split(".")[0].split("-")[-2:]) for file in cif_file_lst]
    entries = mpr.query({"material_id": {"$in": mp_id_lst}},
                        criterion_lst)  # pretty_formula->reduced formula, full_formula->full formula
    if is_save:
        with open(output_json_address, "w") as f:
            print(len(entries))
            f.write(json.dumps(entries))
    else:
        return entries


def get_criterion_txt(criterion_lst, input_dir="../data/tetrahedron_124657_csm/", is_save=True,
                      output_dir="../data/tetrahedron_124657_csm/"):
    """
    GET SPECIFIC property from tetrahedrons e.g., band_gap spacegroup
    把query的criterion保存进txt文件
    注意：query的顺序和查询的顺序不一致，因此最好假如material_id, pretty_formula进行标志
    """
    # #############################################
    # 本地cif文件命名格式为：pretty_formula-material_id.cif
    # #############################################
    if "material_id" not in criterion_lst:
        criterion_lst.append("material_id")
    if "pretty_formula" not in criterion_lst:
        criterion_lst.append("pretty_formula")

    mpr = MPRester("OnQDHiVv3hzqx6p2")
    file_lst = os.listdir(input_dir)
    cif_file_lst = [file for file in file_lst if file.split(".")[-1] == "cif"]
    print(cif_file_lst)
    mp_id_lst = ["-".join(file.split(".")[0].split("-")[-2:]) for file in cif_file_lst]
    entries = mpr.query({"material_id": {"$in": mp_id_lst}},
                        criterion_lst)  # pretty_formula->reduced formula, full_formula->full formula
    if is_save:
        for i, entry in tqdm(enumerate(entries)):
            prefix = entry["pretty_formula"] + "-" + entry["material_id"]
            for criterion in criterion_lst:
                if criterion in ["material_id", "pretty_formula"]:
                    continue
                address = output_dir + prefix + "-{}.txt".format(criterion)
                with open(address, "w") as f:
                    f.write(str(entry[criterion]))
    else:
        return entries


if __name__ == "__main__":
    criterion_lst = ["spacegroup.symbol", "band_gap", "material_id", "pretty_formula"]
    obj_dir = "../data/tetrahedron_126335_csm_remove_repeat/"
    query = get_criterion_txt(criterion_lst, input_dir=obj_dir, output_dir=obj_dir, is_save=True)
    print(query)