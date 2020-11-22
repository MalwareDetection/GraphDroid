#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   map.py
@Time    :   2020/09/03 14:44:22
@Author  :   Yiling He
@Version :   1.0
@Contact :   heyilinge0@gmail.com
@License :   (C)Copyright 2020
@Desc    :   None
'''

# here put the import lib
import pandas as pd
import torch
import glob
import logging
import os


def get_map(exp_dir, post='', add=0, agg=False):
    pt_folder = f"{output_dir}/processed/"
    pt_files = glob.glob(f"{pt_folder}*.pt")

    names = ['graph_id','subgraph_id','apk','api']
    mappings = pd.DataFrame(columns=names)
    dataset = {}
    for pt in pt_files:
        gid, sid = pt[:-3].split('_')[-2:]
        data = torch.load(pt)
        apk_name = data.app
        api_name = data.mapping[data.center]
        if post:
            newgid = int(gid) + add
            new = pt.replace(f'/{post}/', '/processed/').replace(f'data_{gid}_', f'data_{newgid}_')
            os.rename(pt, new)
            gid = newgid
        item = pd.DataFrame([[gid, sid, apk_name, api_name]], columns=names)
        mappings = mappings.append(item)
        if agg:
            try:
                dataset[int(gid)][int(sid)] = data
            except KeyError:
                dataset[int(gid)] = {}
                dataset[int(gid)][int(sid)] = data
    mappings.sort_values(by=['graph_id','subgraph_id'])

    return mappings, dataset


def db_map(exp_dir, agg=False):
    basic_map, dataset = get_map(exp_dir)
    num_graph = len(basic_map.graph_id.value_counts())

    i = 1
    while True:
        extra = f"{exp_dir}/{i}/"
        if os.path.exists(extra):
            m, d = get_map(exp_dir, i, num_graph)
            basic_map = basic_map.append(m)
            num_graph += len(m.graph_id.value_counts())
            i += 1
            os.rmdir(extra)
            if agg: dataset.update(d)
        else:
            break

    basic_map.to_csv(f'{exp_dir}/api_mapping.csv', index=False)
    return pd.DataFrame(dataset)


if __name__ == "__main__":
    import sys
    db, hop, tpl = ['amd-0', 2, True]
    db_map(db, hop, tpl)
