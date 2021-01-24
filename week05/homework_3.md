##### 一. 哪个业务适合使用 rabbitmq？ 引入 rabbitmq 主要解决什么问题?
1. 评论系统引入 rabbitmq，用户评论后写入 rabbitmq，用户积分系统、话题热度系统、推荐系统等可以同时消费消息，进行各自的业务逻辑处理。<br>
   解决了没有消息队列之前多系统耦合度高、多系统并行异步处理困难等问题，实现多系统解耦和异步并行处理。
2. 秒杀系统引入 rabbitmq，大量用户秒杀请求先写入 rabbitmq，后端订单系统根据相应的规则消费消息生成少量订单。<br>
   解决了没有消息队列之前订单系统可能被流量洪峰打垮的问题，起到了流量消峰的作用。
##### 二. 如何避免消息重复投递或重复消费?
1. 根据业务上的唯一标识对消息做幂等处理。
###### 参考资料:
- [阿里云消息队列 RocketMQ 版/最佳实践/消费幂等](https://help.aliyun.com/document_detail/44397.html)
##### 三. 交换机 fanout、direct、topic 有什么区别
1. fanout exchange 投递消息到所有绑定其上的队列中，忽略 routing key。
2. direct exchange 根据 routing key 来投递消息到相对应的队列中。
3. topic exchange 和 direct exchange 类似，也需要通过 routing Key 来路由消息，区别在于 direct exchange 对 routing key 是精确匹配，而 topic exchange 支持模糊匹配。分别支持 * 和 # 通配符，* 表示匹配一个单词，# 则表示匹配没有或者多个单词。<br>
###### 参考资料:
- [官方文档: AMQP 0-9-1 Model Explained](https://www.rabbitmq.com/tutorials/amqp-concepts.html#exchange-topic)
- [官方文档: Topic exchange](https://www.rabbitmq.com/tutorials/tutorial-five-python.html)
- [知乎(理解 RabbitMQ Exchange)](https://zhuanlan.zhihu.com/p/37198933)
##### 四. 架构中引入消息队列是否利大于弊？你认为消息队列有哪些缺点？
1. 引入消息队列是否利大于弊，需要依赖具体场景判断。在业务简单，业务量小，引入消息队列没有明显收益的情况下是弊大于利。在一些需要异步处理，多系统解耦，流量消峰等场景下引入消息队列有明显收益，是利大于弊。
2. 缺点：a. 引入消息队列会增加系统整体的复杂度, 增加维护和开发成本; b. 很多服务依赖消息队列，消息队列异常影响面较广。
