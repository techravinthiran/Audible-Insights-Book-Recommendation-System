# 📚 Audible Book Recommendation System

An intelligent book recommendation system built with Streamlit that uses Natural Language Processing and Machine Learning to suggest similar books based on user preferences.

## 🌟 Features

- **Smart Recommendations**: Uses similarity algorithms to recommend books similar to your favorites
- **Interactive UI**: Beautiful and responsive Streamlit interface
- **Book Details**: Shows book title, author, and rating for each recommendation
- **Real-time Processing**: Instant recommendations powered by pre-trained models

## 🚀 How to Run

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**
   ```bash
   streamlit run app.py
   ```

3. **Open in Browser**
   Navigate to `http://localhost:8501` in your web browser

## 📁 Project Structure

```
├── app.py              # Main Streamlit application
├── apps.ipynb          # Jupyter notebook for development
├── model/              # Trained models and data
│   ├── books.pkl       # Book dataset
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
- **Pickle**: Model serialization
- **Machine Learning**: Similarity algorithms for recommendations

## 📊 How It Works

1. **Data Loading**: Loads pre-processed book data and similarity matrix
2. **User Selection**: User selects a book from the dropdown menu
3. **Similarity Calculation**: Finds books with highest similarity scores
4. **Recommendation Display**: Shows top 5 most similar books with details

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
