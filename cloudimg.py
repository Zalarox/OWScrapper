from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image

with open('scrapdata.txt', 'r', encoding='utf-8') as f:
	data = f.read()

stopwords = set(STOPWORDS)

ow_mask = np.array(Image.open('mask.png'))

wordcloud = WordCloud(background_color='white', mask=ow_mask, stopwords=stopwords).generate(data)
image = wordcloud.to_image()
image.show()