# Animal Photo Datasets Repository

This repository hosts multiple sets of labeled animal photographs, curated specifically for the [personal project](https://github.com/OlegQm/manipulator_project) by **Oleh Savchenko**. All datasets—except `efficientdet-dataset`—are organized in a format ready for training YOLO models.

*Place a chart or image showing dataset scales here.*

---

## 📁 Repository Structure

Each branch in this repository represents a distinct dataset:

* **dataset-v1**, **dataset-v2**, **dataset-v3**, **dataset-v4**, **dataset-v5**: Complete collections of images and annotations.

  * `dataset-v5` is the latest, most comprehensive version.
* **efficientdet-dataset**: Images and labels formatted specifically for EfficientDet models.
* **own-dataset**: Photographs personally collected and annotated by Oleh Savchenko at two different zoos.

Within each dataset folder:

```
└── [dataset-name]
    ├── images
    │   ├── train/   (70% of images)
    │   ├── test/    (20% of images)
    │   └── valid/   (10% of images)
    └── labels
    │   ├── train/   (bounding boxes and class labels)
    │   ├── test/
    │   └── valid/
    ├── coco-data.yaml
    ├── data.yaml
    └── segments_to_bbox_converter.py
```

* **data.yaml**: Configuration file describing the custom animal dataset (paths, classes, splits).
* **coco-data.yaml**: Configuration file for the COCO dataset (for benchmarking and comparison).
* **segments_to_bbox_converter.py**: Covert segment annotations to bounding boxes (useful for training). 

---

<img width="1989" height="1114" alt="image" src="https://github.com/user-attachments/assets/30477dc3-462c-4305-872f-9b635afaea87" />
<img width="1744" height="976" alt="image" src="https://github.com/user-attachments/assets/d136eff7-d7b7-4ef3-a2ee-970f42b71684" />
