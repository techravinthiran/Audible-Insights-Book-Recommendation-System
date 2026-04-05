# 📚 Audible Book Recommendation System

An intelligent book recommendation system built with Streamlit that uses Natural Language Processing and Machine Learning to suggest similar books based on user preferences. This system analyzes book features and provides personalized recommendations using similarity algorithms.

## 🌟 Features

- **Smart Recommendations**: Uses TF-IDF vectorization and cosine similarity to recommend books similar to your favorites
- **Interactive UI**: Beautiful and responsive Streamlit interface with real-time recommendations
- **Book Details**: Shows book title, author, and rating for each recommendation
- **Real-time Processing**: Instant recommendations powered by pre-trained similarity models
- **Clustering Analysis**: Includes K-means clustering for book categorization
- **Performance Metrics**: Evaluated using Precision@K, Recall@K, and RMSE metrics

## 🚀 How to Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/Audible-Insights-Book-Recommendation-System.git
   cd Audible-Insights-Book-Recommendation-System
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install streamlit pandas numpy scikit-learn matplotlib seaborn
   ```

4. **Run the Application**
   ```bash
   streamlit run app.py
   ```

5. **Open in Browser**
   Navigate to `http://localhost:8501` in your web browser

## 📁 Project Structure

```
├── app.py              # Main Streamlit application
├── apps.ipynb          # Jupyter notebook for development and analysis
├── model/              # Trained models and data
│   ├── books.pkl       # Book dataset (processed)
│   └── similarity.pkl  # Similarity matrix
├── dataset/            # Raw dataset files
├── env/                # Virtual environment
├── README.md           # Project documentation
├── LICENSE             # MIT License
└── .gitignore          # Git ignore file
```

## 🛠️ Technologies Used

- **Python**: Core programming language
- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Scikit-learn**: Machine learning library (TF-IDF, K-means, metrics)
- **Matplotlib & Seaborn**: Data visualization
- **Pickle**: Model serialization
- **Jupyter**: Development and analysis notebook

## 📊 How It Works

1. **Data Loading**: Loads pre-processed book data and similarity matrix from pickle files
2. **User Selection**: User selects a book from dropdown menu containing all available books
3. **Similarity Calculation**: Uses pre-computed similarity matrix to find most similar books
4. **Recommendation Display**: Shows top 5 most similar books with title, author, and rating
5. **Clustering**: Books are categorized using K-means clustering for better organization

## 📈 Model Performance

The recommendation system has been evaluated using the following metrics:
- **Precision@5**: 0.8 (80% of recommended books are relevant)
- **Recall@5**: 0.8 (80% of relevant books are recommended)
- **RMSE**: 2.298 (Root Mean Square Error for rating predictions)
- **Optimal Clusters**: 3 clusters identified using elbow method

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to the book dataset providers
- Streamlit community for the amazing framework
- All contributors who help improve this project
