# stackoverflow-crawler
*A toy web crawler to play with Scrapy and MongoDB.*

Basically just followed this [tutorial](https://realpython.com/blog/python/web-scraping-with-scrapy-and-mongodb/).

### 1. Run Spider

```shell
cd stack  
scrapy crawl stack
```

### 2. View Record in MongoDB
```shell
mongo
use stackoverflow
db.questions.find()
```
