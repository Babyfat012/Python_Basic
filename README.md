# Project: Ngôn Ngữ Lập Trình Python — Example Notebooks & Scripts

Repository contains teaching/demo code (notebooks and small scripts) for Python, PyTorch, torchvision, PyG, minisom, etc.

## Structure (high level)
- baitap1/ — small exercise scripts
  - [baitap1/bai1.py](baitap1/bai1.py)
  - [baitap1/bai2.py](baitap1/bai2.py)
  - [baitap1/bai3.py](baitap1/bai3.py)
  - [baitap1/bai4.py](baitap1/bai4.py)
- tuan2/ — OOP fundamentals (classes, inheritance, encapsulation, polymorphism)
  - [tuan2/qlsv.py](tuan2/qlsv.py) — simple student manager (see class [`StudentManager`](tuan2/qlsv.py))
  - [tuan2/abstraction.py](tuan2/abstraction.py)
  - [tuan2/encapsulation.py](tuan2/encapsulation.py)
  - [tuan2/inheritance.py](tuan2/inheritance.py)
  - [tuan2/polymorphism.py](tuan2/polymorphism.py)
  - [tuan2/oop.py](tuan2/oop.py)
- tuan3/ — numpy / pandas demos
  - [tuan3/test_numpy.py](tuan3/test_numpy.py)
  - [tuan3/pandas_demo1.ipynb](tuan3/pandas_demo1.ipynb)
- tuan4..tuan10/ — deep learning notebooks (transfer learning, GAN, ViT, CLIP, GCN, SOM, etc.)
  - [tuan7/ResNet.ipynb](tuan7/ResNet.ipynb)
  - [tuan7/EfficientNet.ipynb](tuan7/EfficientNet.ipynb)
  - [tuan8/GAN.ipynb](tuan8/GAN.ipynb)
  - [tuan8/Encoder-Decoder.ipynb](tuan8/Encoder-Decoder.ipynb)
  - [tuan9/VIT.ipynb](tuan9/VIT.ipynb)
  - [tuan9/fine_tune_vtt.ipynb](tuan9/fine_tune_vtt.ipynb)
  - [tuan9/Transformer.ipynb](tuan9/Transformer.ipynb)
  - [tuan9/ex2_CLIP.ipynb](tuan9/ex2_CLIP.ipynb)
  - [tuan10/GCN.ipynb](tuan10/GCN.ipynb)
  - [tuan10/GNN.ipynb](tuan10/GNN.ipynb)
  - [tuan10/SOM.ipynb](tuan10/SOM.ipynb)

## Quickstart

1. Create a Python venv and install typical deps used by notebooks:
```sh
python -m venv .venv
source .venv/bin/activate        # or .venv\Scripts\activate on Windows
pip install --upgrade pip
pip install torch torchvision jupyterlab matplotlib pandas numpy scikit-learn minisom
# Optional (used in some notebooks): torch-geometric, open_clip, ultralytics
```

2. Open notebooks in VS Code or Jupyter:
- Use VS Code "Open Folder" on repository root then open any notebook, e.g. [tuan8/GAN.ipynb](tuan8/GAN.ipynb).
- Or run JupyterLab:
```sh
jupyter lab
```

3. Run small scripts:
- Example: run student manager demo
```sh
python tuan2/qlsv.py
```
- Example: run numpy demo
```sh
python tuan3/test_numpy.py
```
- For exercises in baitap1:
```sh
python baitap1/bai2.py
python baitap1/bai3.py
python baitap1/bai4.py
```

## Notable files / entry points
- GAN (DCGAN MNIST demo): [tuan8/GAN.ipynb](tuan8/GAN.ipynb)
- Encoder-Decoder toy seq2seq: [tuan8/Encoder-Decoder.ipynb](tuan8/Encoder-Decoder.ipynb)
- Transfer learning examples (ResNet / EfficientNet / VGG / ViT): [tuan7/ResNet.ipynb](tuan7/ResNet.ipynb), [tuan7/EfficientNet.ipynb](tuan7/EfficientNet.ipynb), [tuan6/VGG.ipynb](tuan6/VGG.ipynb), [tuan9/VIT.ipynb](tuan9/VIT.ipynb)
- CLIP examples: [tuan9/ex2_CLIP.ipynb](tuan9/ex2_CLIP.ipynb), [tuan9/example1_CLIP.ipynb](tuan9/example1_CLIP.ipynb)
- Graph demos: [tuan10/GCN.ipynb](tuan10/GCN.ipynb), [tuan10/GNN.ipynb](tuan10/GNN.ipynb)
- Student manager & model classes: [tuan2/qlsv.py](tuan2/qlsv.py) (class [`StudentManager`](tuan2/qlsv.py))

## Tips
- Many notebooks use torchvision weights transforms (preprocess). Ensure torchvision version matches code.
- For GPU notebooks, set CUDA-visible device or run on CPU fallback; code uses DEVICE = "cuda" if available.
- To export a notebook to script:
```sh
jupyter nbconvert --to script tuan8/GAN.ipynb
```

## Contributing
- Add new notebooks under tuanX/ with descriptive names.
- Keep dataset downloads local (./data) or use torchvision.datasets FakeData for quick demos.

---
Open any file above by clicking its link (e.g. [tuan8/GAN.ipynb](tuan8/GAN.ipynb)) to inspect or run the code.


# first commit in 2026
