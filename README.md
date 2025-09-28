# Auto MOS Prediction with NISQA for Persian

This repository contains a project focused on **automatic Mean Opinion Score (MOS) estimation** for speech signals.  
MOS is a widely used metric in speech and audio quality assessment, traditionally obtained through subjective human listening tests. While accurate, these tests are expensive, time-consuming, and not scalable.  

Our project addresses this challenge by building an automated system that predicts MOS using **signal processing techniques** and **machine learning models**. The system provides an efficient and consistent way to evaluate speech quality across large datasets without the need for extensive human evaluations.  

Key highlights of this project include:
- Implementation of preprocessing, augmentation, and training pipelines for speech data  
- Integration of baseline methods such as **[NISQA](https://github.com/gabrielmittag/NISQA)** for comparison  
- Usage of publicly available datasets such as **[Mana-TTS](https://huggingface.co/datasets/MahtaFetrat/Mana-TTS)**  
- Tools for dataset preparation, audio quality analysis, and result visualization  
- Flexible training scripts for experimenting with different models and approaches  

This project is designed for **educational and research purposes**, serving as both a framework for students learning about speech processing and a foundation for future research on MOS prediction. our simple documentation with Persian language is in **[Doc](https://docs.google.com/document/d/1F5ecEGLcXbL567xjhDInn82WpVJb6CDdAzqUfzILPWM/edit?usp=sharing)**

--- 

🙏 Special thanks to the creators of **NISQA** and the **Mana-TTS dataset** for providing valuable resources that made this project possible.  

--- 

## 🚀 Project Overview 

- **Objective**: Develop methods to automatically predict MOS for speech samples. 
- **Motivation**: Human MOS evaluation is expensive and time-consuming. An automatic prediction system can scale to large datasets. 
- **Contribution**: Introduce a novel approach combining signal features and machine learning models to estimate MOS. 

--- 

## 📁 Repository Structure

```
mos_project/
├── README.md
├── requirements.txt
├── .gitignore
├── .gitmodules
├── data/              
├── src/
│   └── mos_main/
│       ├── augmentation/
│       ├── download/
│       ├── train/
│       ├── ui/
│       ├── eval_preds.py
│       ├── run_nisqa.py
├── tests/
│   └── test_main.py
```

--- 

## 🛠️ Getting Started / Installation Follow these steps to get a working environment: 

1. Clone the repo
```bash
   git clone https://github.com/A-Yaghoubian/mos_project.git
   cd mos_project
   ```

2. (Optional but recommended) Create & activate a virtual environment
```bash
   python -m venv .venv
   source .venv/bin/activate   # On macOS / Linux
   .venv\Scripts\activate      # On Windows
   ```

3. Install dependencies
```bash
   pip install -r requirements.txt
   ```

--- 

## 🔍 Usage / Workflow Here is a typical pipeline you might follow (adapt based on your implementation): 

1. **Download dataset**
```bash
   python src/mos_main/download/download_dataset.py
   ```

2. **Extract / Preprocess audio files**
```bash
   python src/mos_main/download/convert_wavs.py
   ```

3. **Augmentation / Process audio files**
```bash
   python src/mos_main/augmentation/augment_wavs.py
   ```

4. **User Interface / User examination**
```bash
   python src/mos_main/ui/audio_ui.py
   ```

5. **Train with different ways**
```bash
   python src/mos_main/train/[train_way].py
   ```

6. **Evaluatioon**
```bash
   python src/mos_main/eval_preds.py
   ```

--- 

## 📚 Academic Context & Authors 

This work is developed as part of a **Speech Processing** course / research project. 

**Professor:** 
- Dr. H Sameti 

**Authors:** 
- *Moein Khorasani*
- *Ali Yaghoubian* 

--- 

## 📄 License 

This project is intended for **academic and research purposes only**. 

--- 

## 🧠 Future Work & Extensions (Optional)

- Exploring newer architectures for MOS prediction 
- Incorporating additional acoustic / perceptual features 
- Deploying as a web service or API 

--- 

## 📫 Contact & Acknowledgements 

If you have questions, suggestions, or want to collaborate: 
- Email: *[ayaghoubian2000@gmail.com]*

Acknowledgements to any funding agencies, labs, advisors, or datasets you used. 

--- 

*Thank you for checking out this project!*
