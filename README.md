# Animal Photo Datasets Repository

This repository hosts multiple sets of labeled animal photographs, curated specifically for the [personal project](https://github.com/OlegQm/manipulator_project) by **Oleh Savchenko**. All datasets—except `efficientdet-dataset`—are organized in a format ready for training YOLO models.

*Place a chart or image showing dataset scales here.*

---

## 📁 Repository Structure

Each branch in this repository represents a distinct dataset:

* **dataset-v1**, **dataset-v2**, **dataset-v3**: Complete collections of images and annotations.

  * `dataset-v3` is the latest, most comprehensive version.
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
    └── data.yaml   
```

* **data.yaml**: Configuration file describing the custom animal dataset (paths, classes, splits).
* **coco-data.yaml**: Configuration file for the COCO dataset (for benchmarking and comparison).

---

![image](https://github.com/user-attachments/assets/b54f1374-5ffb-481c-b012-62e6d5f46c54)
![image](https://github.com/user-attachments/assets/36cf24b1-4859-4d6e-aab6-37b308c73f9f)
