import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

# Text to be converted to speech
text = "Machine Learning: Experienced in building and optimizing machine learning models using frameworks such as Scikit-Learn, TensorFlow, and Keras. Skilled in various algorithms, including regression, classification, clustering, and deep learning.Data Analysis: Proficient in exploring and analyzing datasets to uncover patterns and insights. Strong skills in using Python libraries like Pandas and NumPy for data manipulation and analysis.Data Visualization: Adept at creating clear and compelling visualizations using tools like Matplotlib, Seaborn, and Plotly to communicate data-driven stories effectively.Web Scraping: Capable of gathering and preprocessing data from web sources using BeautifulSoup, Scrapy, and Selenium for various data-driven projects."

# Generate and play the speech
engine.say(text)

# Wait until the speech is finished
engine.runAndWait()
