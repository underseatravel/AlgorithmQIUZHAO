学习笔记
## 学习总结
* 对于一些难题感到分析时间复杂度困难，还是要多学习。专注，冷静坚持
* 对于一些新方法适当选择放弃，抓紧时间，老方法能做出题目也行
* 面试四步骤：确认题意，阐述所有解并分析时空间复杂度，写代码，测试。勿忘
* 多总结题型，找相似点，熟能生巧
* 自上而下的编程
* 五毒神掌 
* 熟练度,防BUG！

### 布隆过滤器与lru chche
* 特点： 布隆过滤器：二进制位随机映射，作为数据库查询前的预查询处理，若全为1则可能存在，若至少有一个0，则一定不存在。lru chche   least recently used  两个要素：大小，替换策略   本质位哈希表和双向链表的结合
* 常见题型：理解概念，并会写lru chche

### 高级搜索
* 分类：比较类排序和非比较类排序
* 比较类排序：又分为初级排序O(n^2)：选择排序，插入排序，冒泡排序； 和高级排序O(nlogn)：快排, 归并排序，堆排序
* 剩下的特殊排序（非比较类排序）O(n)：计数排序，桶排序，基数排序


### 动态规划
* 三步骤：找出子问题（分治），定义状态数组，写出dp方程

### 字符串
* 各类问题：基础问题，字符串操作问题（随机应变）；异位词（多用哈希）；回文串（中心扩散或者dp); 其他DP问题

