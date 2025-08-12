# 📱 Mobile Phone Price Predictor

A machine learning-powered web application that predicts mobile phone price ranges based on technical specifications. Built with Streamlit and scikit-learn, this tool provides instant price predictions with an intuitive and modern user interface.

![Mobile Price Predictor](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🌟 Features

- **Instant Price Predictions**: Get real-time price range predictions for mobile phones
- **Modern UI**: Beautiful, responsive interface with gradient designs and intuitive layout
- **Comprehensive Inputs**: 20+ phone specifications including camera, display, performance, and connectivity features
- **Detailed Results**: Color-coded price categories with descriptions and specification summaries
- **Machine Learning Powered**: Uses Random Forest Classifier for accurate predictions
- **Easy to Use**: No technical knowledge required - just input phone specs and get results

## 🚀 Live Demo

The application provides four price categories:
- 💚 **Low Cost** ($0 - $150): Perfect for basic usage
- 💙 **Medium Cost** ($151 - $400): Great balance of features and price  
- 💜 **High Cost** ($401 - $800): Premium features and performance
- 🧡 **Very High Cost** ($801+): Flagship with cutting-edge technology

## 📋 Prerequisites

- Python 3.8 or higher
- pip package manager

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "Mobile Phone Pricing"
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser**
   - The app will automatically open at `http://localhost:8501`
   - If it doesn't open automatically, navigate to the URL manually

## 📦 Dependencies

```
streamlit>=1.28.0
pandas>=1.5.0
numpy>=1.24.0
scikit-learn>=1.3.0
pickle-mixin>=1.0.2
```

## 📊 Input Features

The model uses the following 20 features to predict phone prices:

### 📋 Basic Specifications
- **Battery Power** (mAh): Battery capacity
- **Clock Speed** (GHz): Processor speed
- **RAM** (MB): Memory capacity
- **Internal Memory** (GB): Storage capacity
- **Processor Cores**: Number of CPU cores
- **Mobile Weight** (g): Device weight
- **Mobile Depth** (cm): Device thickness

### 📸 Camera & Display
- **Primary Camera** (MP): Rear camera resolution
- **Front Camera** (MP): Selfie camera resolution
- **Pixel Height**: Screen resolution height
- **Pixel Width**: Screen resolution width
- **Screen Height** (cm): Physical screen height
- **Screen Width** (cm): Physical screen width
- **Talk Time** (hours): Battery life during calls

### 🔗 Connectivity Features
- **Bluetooth**: Bluetooth support (Yes/No)
- **WiFi**: WiFi connectivity (Yes/No)
- **4G Support**: 4G network support (Yes/No)
- **3G Support**: 3G network support (Yes/No)
- **Dual SIM**: Dual SIM card support (Yes/No)
- **Touch Screen**: Touch screen capability (Yes/No)

## 🤖 Model Information

- **Algorithm**: Random Forest Classifier
- **Preprocessing**: StandardScaler for feature normalization
- **Training Data**: Mobile phone dataset with 2000+ samples
- **Accuracy**: Optimized for balanced prediction across all price ranges
- **Output**: 4 price categories (0: Low, 1: Medium, 2: High, 3: Very High)

## 📁 Project Structure

```
Mobile Phone Pricing/
│
├── app.py                          # Main Streamlit application
├── model.pkl                       # Trained Random Forest model
├── scaler.pkl                      # StandardScaler for preprocessing
├── dataset.csv                     # Training dataset
├── train.ipynb                     # Model training notebook
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
└── Predict Mobile Phone Pricing.pdf # Project report
```

## 🎯 Usage

1. **Launch the application** using `streamlit run app.py`
2. **Fill in the phone specifications** in the three organized sections:
   - Basic Specifications (battery, processor, memory)
   - Camera & Display (cameras, screen details)
   - Connectivity Features (bluetooth, wifi, network support)
3. **Click "🔮 Predict Price Range"** to get instant results
4. **View the prediction** with detailed price range and specification summary

## 🔧 Customization

### Adding New Features
To add new input features:
1. Add the input widget in `app.py`
2. Update the `input_data` array to include the new feature
3. Retrain the model with the new feature in `train.ipynb`

### Styling Changes
Modify the CSS in the `st.markdown()` section of `app.py` to customize:
- Colors and gradients
- Layout and spacing
- Fonts and typography
- Button styles and animations

## 📈 Performance

- **Fast Predictions**: Sub-second response time
- **Cached Models**: Models loaded once and cached for efficiency
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Memory Efficient**: Optimized for low resource usage

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Dataset source: Mobile phone specifications dataset
- Streamlit team for the amazing framework
- scikit-learn for machine learning capabilities
- The open-source community for inspiration and tools

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/yourusername/mobile-price-predictor/issues) page
2. Create a new issue with detailed description
3. Contact the author directly

---

⭐ **Star this repository if you found it helpful!** ⭐
