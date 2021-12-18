# Quote Website Scraping (Mini Project)

Wesite link - (https://www.quotable.io/)[https://www.quotable.io/]


## Scraping via CSS Selectors

- Getting into the shell of the scrapy for the website. First Open the terminal and type the following command:
```bash
scrapy shell "https://quotes.toscrape.com/"

```
- This will open scrape the website and if the response is 200, the website is scraped
- To extract the title we can type 
```bash 
> response.css("title::text")
```
- To extract only the lists of the texts
```bash
> response.css("title::text").extract()
```
- To extract only the first item of the texts
```bash
> response.css("title::text").extract_first()
```
- To extract the Quotes for the page, Install a chrome extention (Selector Gadget)[https://chrome.google.com/webstore/detail/selectorgadget/mhjhnkcfbdhnjickkkdbjoemdmbfginb/related?hl=en]. Next click on the extention and select the text. It will return a unique class name or id name for the text. For the class name type the following command:
```bash
> response.css(".text::text").extract()
```
- For id you can type the following command(The below code will not work for this website):
```bash
> response.css("#text::text").extract()
```

## Scraping via xpath 

```bash

```