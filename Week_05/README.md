学习笔记
## 学习总结
* 对于一些难题感到分析时间复杂度困难，还是要多学习。专注，冷静坚持
* 对于本周的新学习一些方法适当选择放弃，抓紧时间，老方法能做出题目也行
* 面试四步骤：确认题意，阐述所有解并分析时空间复杂度，写代码，测试。勿忘
* 多总结题型，找相似点，熟能生巧
* 自上而下的编程
* 五毒神掌 
* 熟练度,防BUG！

### 字典树和并查集
* 特点： 两者皆有明显的套路，需反复学习熟记
* 常见题型：单词搜索2   ；  朋友圈（并查集一般也能用dfs做）
* 字典树：书上的每个节点放一个字符，python中一般用字典嵌套字典表示。优点查询效率高
* 并查集：无他，唯需手熟

### 高级搜索
* 常见题型：
* 剪枝：提前中断不可能的路径 if语句判断
* 双向BFS： 头尾两端广度搜索，queue改用Set，优先处理长度短的set


### 红黑树
* AVL;平衡二叉搜索树，有平衡因子，四种旋转操作，结点存储空间需求大，旋转操作次数多。适用于多读少些的情况
* 红黑树： 结点红或黑，根节点和叶子（空）结点为黑， 相邻两结点不全为红，任一结点到其叶子所有路径包含相同的结点数
* AVL树查找更快，因为更平衡。红黑树插入删除更快。AVL树结点要保存平衡因子int,需求存储空间大，红黑树还行，只要1bit(0, 1)

### 位运算
* 最常用： n & (n - 1)去除最低位的0  判断奇偶 n & 1 == 1 
