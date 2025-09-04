# MOS Project

This repository contains an academic project on **Mean Opinion Score (MOS) estimation** for voice input.  
The project is part of a **Speech Processing course** and focuses on developing a new approach for automatic MOS prediction.

## Project Overview

- **Objective:** To design and evaluate methods for predicting MOS for speech samples.  
- **Motivation:** Human MOS evaluation is costly and time-consuming. An automatic method can make the process faster and more scalable.  
- **Contribution:** We aim to introduce a new idea for MOS estimation by combining modern signal processing and machine learning techniques.

## Project Structure

mos_project/
│── README.md               # Documentation  
│── requirements.txt        # Dependencies  
│── setup.py                # Installation file  
│── src/  
│    └── mos_project/  
│         ├── __init__.py  
│         └── main.py       # Main entry point  
│── tests/  
     └── test_main.py       # Unit tests

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/A-Yaghoubian/mos_project.git
cd mos_project

python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

pip install -r requirements.txt

python src/mos_project/main.py

```

---

### **5. Testing**

## Testing

```bash
# Step 1: download one dataset part
python src/mos_project/download_dataset.py

# Step 2: extract wav files
python src/mos_project/extract_mana_to_wavs.py --max_samples 200

# Step 3: run NISQA
python src/mos_project/run_nisqa.py

# Step 4: evaluate (requires ground truth MOS CSV)
python src/mos_project/eval_preds.py

```

---

### **6. Academic Context**

## Academic Context

This project is developed as part of a graduate-level **Speech Processing course**.  
It contributes to research in **speech quality assessment** and provides a foundation for future work in MOS prediction.

## Authors

- [Moein Khorasani]
- [Ali Yaghoubian]

## License

This project is intended for academic and research purposes only.
