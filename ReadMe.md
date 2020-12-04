# GraphDroid
A First Step Towards Explainable Static Detection of Android Malware with GNN.

### [Source Code](https://github.com/MalwareDetection/GraphDroid/tree/master/src)

Run the `test` script (with `model.pkl` in `./src/classification`):

```shell
python main.py --input $input_dir --output $outputdir
```

Example: 

`$input_dir`

```shell
$input_dir
├── app-debug.apk
└── Test
    └── app-debug.apk
```

`$output_dir`

```shell
$outputdir
├── decompile
│   ├── app-debug
│   │   └── call.gml
│   └── Test
│       └── app-debug
│           └── call.gml
├── FeatureLen.txt
├── prediction.csv
├── processed
│   ├── data_0_0.pt
│   └── ...
└── result
    ├── opcode
    │   ├── app-debug.csv
    │   └── Test
    │       └── app-debug.csv
    ├── permission
    │   ├── app-debug.csv
    │   └── Test
    │       └── app-debug.csv
    └── tpl
        ├── app-debug.csv
        └── Test
            └── app-debug.csv
```

- `prediction.csv` classification results (*APK ID*, *APK Path*, *Class*).

> The `train` code will be released after the paper is published.

### [Processed Graph Data](https://github.com/MalwareDetection/GraphDroid/tree/master/Datasets)

`.pt` file is named after *APK ID* and *Behavior Subgraph ID*. 

Mappings between (*APK ID*, *Behavior Subgraph ID*) and (*APK Hash*, *API Name*) for each dataset are available in `Datasets/mappings`
