#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import time
import logging

logging.basicConfig(level=logging.DEBUG)

topic_id = "19555513"
topic_start_url = f"https://www.zhihu.com/api/v4/topics/{topic_id}/feeds/top_activity?include=data%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.is_normal%2Ccomment_count%2Cvoteup_count%2Ccontent%2Crelevant_info%2Cexcerpt.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Darticle%29%5D.target.content%2Cvoteup_count%2Ccomment_count%2Cvoting%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Dpeople%29%5D.target.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Canswer_type%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.paid_info%3Bdata%5B%3F%28target.type%3Darticle%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dquestion%29%5D.target.annotation_detail%2Ccomment_count%3B&limit=10&after_id=0"


def topic_spider(topic_url):
    headers = {
        "referer": "https://www.zhihu.com/topics",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"
    }
    resp = requests.get(topic_url, headers=headers)
    topic_resp_json = resp.json()
    topic_page_info = topic_resp_json["paging"]
    topic_article_list = topic_resp_json["data"]

    for topic_article in topic_article_list:
        article_id = topic_article["target"]["id"]
        article_type = topic_article["target"]["type"]
        article_content = topic_article["target"]["content"]
        article_file = article_type + "_" + str(article_id) + ".html"
        with open(article_file, "w") as f:
            f.write(article_content)

    topic_page_is_end = topic_page_info["is_end"]
    if not topic_page_is_end:
        topic_next_url = topic_page_info["next"]
        return topic_next_url

    return None


def main():
    topic_next_url = topic_spider(topic_start_url)
    while topic_next_url:
        time.sleep(30)
        topic_next_url = topic_spider(topic_next_url)


if __name__ == "__main__":
    main()
