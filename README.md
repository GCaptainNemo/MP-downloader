# MP-Downloader

## 一、介绍

因为项目原因需要下载[Materials Project](https://materialsproject.org/)网站所有的CIF文件进行机器学习，`pymatgen`给出了如下示例，也就是说理论上遍历所有id就可以把网站所有CIF文件下载完成。

```
get_structure_by_material_id("mp-1000")
```

然而坑爹的是Materials Project网站的**材料ID并不连续**，比如mp-300000之后的下一个id是mp-504097，中间相差200000个id。按照1个CIF文件每秒的下载速度，3小时才能下载10000个，60小时才能从找到下一个CIF文件。

参考资料[1-2]，发现可以先通过构造筛选条件找到所有materials_id保存下来，再从中进行下载，这样就可以更快地下载完所有CIF文件。



## 二、使用方法

1. 获得所有id，并保存在本地src/all_mp_id.pkl

```python
python ./get_mp_id.py
```

2. 遍历src/all_mp_id.pkl文件，下载所有惯用晶胞(conventional_unit_cell)CIF文件

```
python ./download_conventional_cell.py
```

3. 下载所有单胞CIF文件（由于使用默认下载，下载速度远快于2）

```
python ./download_unit_cell.py
```



## 三、补充下载方式

除了利用pymatgen通过Materials Project API下载MP网站材料数据之外，还有许多数据集属于文章发布后被Materials Project收录，比如文献[3]发布的[电子输运性质数据集](https://contribs.materialsproject.org/projects/carrier_transport/)，这类数据集可以通过matminer或其它方式下载，见[Website](https://github.com/hackingmaterials/matminer/issues/606)。



## 四、参考资料

[1] [github-pymatgen](https://github.com/materialsproject/mapidoc)

[2] [github-pymatgen-下载demo](https://github.com/materialsproject/mapidoc/blob/7f7ce08488b2e44fc758c903e9828b969a27d421/example_notebooks/Get%20all%20MP%20oxide%20CIFs.ipynb)

[3] Ricci, F., Chen, W., Aydemir, U. *et al.* An *ab initio* electronic transport database for inorganic materials. *Sci Data* **4,** 170085 (2017). https://doi.org/10.1038/sdata.2017.85

