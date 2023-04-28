# Project Name:- Amazon Reviews Scrapping using Beautifulsoup

This project is designed to extract product reviews from Amazon.in using Python, Requests, Pandas and BeautifulSoup libraries.

## Project Description

This project extracts product reviews from Amazon.in using web scraping. The code uses Python libraries such as Requests, Pandas and BeautifulSoup to scrape data from the Amazon website. The code is capable of extracting data such as review title, review body, review rating, and more. 

## Installation

To run this code, you will need to install the following libraries:

```python
import requests
import pandas as pd
from bs4 import BeautifulSoup
```

## Usage

To use this code, run the `main()` function after setting the appropriate values for the `productUrl` and `HEADERS` variables. The `totalPages()` function is used to determine the total number of pages of reviews for the product, and the `extractReviews()` function is used to extract reviews from each page. 

The extracted data is then saved to an Excel file named `output.xlsx` using Pandas.

```python
main()
```

## Contribution

If you would like to contribute to this project, please submit a pull request or contact the author.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

## Credits

This project was created by Aadil Mansoori. 

Special thanks to Code with harry.
