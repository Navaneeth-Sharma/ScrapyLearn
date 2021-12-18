# Quote Website Scraping (Mini Project)

Wesite link - https://quotes.toscrape.com/

 Getting into the shell of the scrapy for the website. First Open the terminal and type the following command:
```bash
scrapy shell "https://quotes.toscrape.com/"

```
 This will open scrape the website and if the response is 200, the website is scraped


## Scraping via CSS Selectors

 To extract the title we can type 
```bash 
> response.css("title::text")
```
 To extract only the lists of the texts
```bash
> response.css("title::text").extract()
```
 To extract only the first item of the texts
```bash
> response.css("title::text").extract_first()
> response.css("title::text")[0].extract()
```
 To extract the Quotes for the page, Install a chrome extention <a href="https://chrome.google.com/webstore/detail/selectorgadget/mhjhnkcfbdhnjickkkdbjoemdmbfginb/related?hl=en">Selector Gadget</a>. Next click on the extention and select the text. It will return a unique class name or id name for the text. For the class name type the following command:
```bash
> response.css(".text::text").extract()
```
 For id you can type the following command(The below code will not work for this website):
```bash
> response.css("#text::text").extract()
```

## Scraping via xpath 

 To extract the title we can type 
```bash
> response.xpath("//title").extract()
```
 To extract only the lists of the texts
```bash
> response.xpath("//title/text()").extract()
```
 To extract from the class name
```bash
> response.xpath("//span[@class='text']/text()").extract()
```
 To extract from the id name (The below code will not work for this website):
```bash
> response.xpath("//span[@id='text']/text()").extract()
```


## A Deadly Combination Scraping via xpath and CSS Selectors

 To extract the url of the next page we can type
```bash 
> response.css("li.next a").xpath("@href").extract()
```