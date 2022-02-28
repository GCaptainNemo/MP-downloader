from tqdm import tqdm
from pymatgen.ext.matproj import MPRester
import pickle
import os


def get_criterion(criterion="spacegroup.symbol", is_save=True, output_dir="../data/tetrahedron_124657/"):
    """
    GET SPECIFIC property from tetrahedrons e.g., band_gap spacegroup
    """
    # CIF文件晶体晶系、空间群、带隙等信息可以从MP下载获得

    mpr = MPRester("OnQDHiVv3hzqx6p2")
    file_dir = "../data/tetrahedron_124657_union/"
    file_lst = os.listdir(file_dir)

    for i, file in enumerate(file_lst):
        print(i)
        # if i < 90):
        #     continue
        if file.split(".")[-1] != "cif":
            continue
        try:
            task_id = file.split("-")[1] + "-" + file.split("-")[-1].split(".")[0]
            entries = mpr.query({"task_id": task_id}, [criterion])
            print(file, entries[0][criterion])
            if is_save:
                with open(output_dir + file.split(".")[0] + "-{}.txt".format(criterion), "w") as f:
                    f.write(str(entries[0][criterion]))
        except Exception as e:
            print("[error]", file + "no {} in MP".format(criterion))


if __name__ == "__main__":
    output_dir = "../data/tetrahedron_124657_union/"
    # get_criterion("spacegroup.crystal_system", True, output_dir=output_dir)
    # get_criterion("band_gap", True, output_dir=output_dir)
    # get_criterion("spacegroup.symbol", True, output_dir=output_dir)
    get_criterion("decomposes_to", True, output_dir=output_dir)

