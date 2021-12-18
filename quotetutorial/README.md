# Quote Website Scraping (Mini Project)

Wesite link - (https://www.quotable.io/)[https://www.quotable.io/]


## Scraping via CSS Selectors

- Getting into the shell of the scrapy for the website
```bash
scrapy shell "https://quotes.toscrape.com/"

```
- This will open scrape the website and if the response is 200, the website is scraped
- To extract the title we can type 
```bash 
> response.css('title::text')
```


## Scraping via xpath 

```bash

```