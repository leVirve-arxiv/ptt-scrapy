# ptt-scrapy

A powerful `scrapy` spider make all-out effort to collect information from PTT into database.


## Requisites

- Python 3
- MongoDB


## Usage

- Make sure your `mongod` is running in system.
- Run with `scrapy` command:

    ```bash
    scrapy crawl ptt
    ```
- (Option) You can export these data into `json`, e.g.:

    ```bash
    mongoexport --db ptt --collection mobilecomm --out mobilecomm.json
    ```


## Acknowledgement

- [shaform/experiments of PTT scrapy]( https://github.com/shaform/experiments/tree/master/scrapy)
