# import requests
# from nomad.client import ArchiveQuery
#
# query = ArchiveQuery(query={"dataset.name":"NOMAD webinar"}, required={"section_run":})
#
#
# base_url = 'http://nomad-lab.eu/prod/rae/api'
# response = requests.get(base_url + '/repo', params={ 'datasets.name': 'NOMAD webinar'})
# print(response)
# data = response.json()
# entry = data['results'][0]
# calc_id, upload_id = entry['calc_id'], entry['upload_id']
# print(calc_id, upload_id)
# response = requests.get(base_url + '/archive/%s/%s' %(upload_id, calc_id))
# print(response.json())
#
#
import json
# from itertools import izip_longest

# An optional utility to display a progress bar
# for long-running loops. `pip install tqdm`.
from tqdm import tqdm

from pymatgen.ext.matproj import MPRester
import pickle
import os


def get_criterion(criterion="spacegroup.symbol", is_save=True, output_dir="../data/tetrahedron_124657/"):
    """
    GET SPECIFIC property from tetrahedrons e.g., band_gap spacegroup
    """
    mpr = MPRester("OnQDHiVv3hzqx6p2")
    file_dir = "../data/tetrahedron_124657_union/"
    file_lst = os.listdir(file_dir)
    # file_lst_1 = os.listdir("../data/tetrahedron_124657")
    # file_lst_1 = [file for file in file_lst_1 if file.split(".")[-1] == "cif"]
    # file_lst_2 = os.listdir("../data/tetrahedron_124657_bond")
    # file_set_1 = set(file_lst_1)
    # file_set_2 = set(file_lst_2)
    # file_lst = list(file_set_2 - file_set_1)
    # print(len(file_lst))
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

