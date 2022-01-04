# About
This project webscrapes 4800 of the recently sold CryptoPunks including details such as their type, attributes, and selling price. This dataset is then cleaned where feature engineering is used to perform one-hot encoding, and an analysis is done to determine feature importance. Lastly, a linear regression model was made using this dataset to predict the value of a CryptoPunk, where the model deployed on Heroku as a web application.

![image](https://user-images.githubusercontent.com/68152521/148126129-e5e1b593-2a28-4607-be5f-e3f99ecc1fa2.png)

# Decision Choices
Up to 6 months of data (in this case, 50 pages of data) was used, as while the value of NFT's were rapidly increasing which would mean old data could deflate the predicted price, not allowing enough data would make the model unfamiliar with certain attributes not in the dataset.

As these CryptoPunk were traded for Ethereum, the decision to make the price value in terms of Ethereum was more logical. However, it is unknown if these NFT's follow their value in USD (ex. if Ethereum drops 10%, the NFT's value would remain the same in USD) or if they follow their value in ETH (ex. if Ethereum drops 10%, the NFT's value would reamin the same in ETH). The latter was assumed.

Lastly, this linear regression model works well for CryptoPunks that are closer to the average value. That is, CryptoPunks that aren't extremely special and valuable due to a certain rare attribute. This is because of the decision to remove outliers from our dataset, that may have been valued highly because they contained rare attributes.

# Usage
Rerun create-dataset.py to update the dataset and rerun the analysis notebook file to update the model, and then deploy the web application on Heroku.
Alternatively, visit https://cryptopunks-model.herokuapp.com/ for a model trained with data at the time this repository was last updated.

# Credits
https://youtu.be/zD0FDYI5_rs
Useful for webscraping multiple pages within a single page.

https://betterprogramming.pub/how-to-scrape-multiple-pages-of-a-website-using-a-python-web-scraper-4e2c641cff8
Useful for webscraping multiple points of data such as type, attributes, attribute count, and recent sale price from a single page. 

https://towardsdatascience.com/dealing-with-list-values-in-pandas-dataframes-a177e534f173
Useful for creating a boolean dataframe for if an attribute existed for a CryptoPunk, given the dataframe that contained a list of attributes.

https://youtu.be/EAezvs0eL1s
Useful for removing outliers in the dataset.

https://youtu.be/p_tpQSY1aTs
Useful for saving the machine learning model and creating a Flask web application from it. In addition, useful for deploying the application to Heroku.

https://youtu.be/Li0Abz-KT78
Helped fix my bug for the Heroku application deploying successfully, but the website having an application error. Turns out I just needed a Procfile.
