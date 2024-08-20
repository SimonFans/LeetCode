https://leetcode.com/problems/finding-the-topic-of-each-post/

SELECT 
    P.post_id, 
    IFNULL(GROUP_CONCAT(DISTINCT K.topic_id ORDER BY K.topic_id), 'Ambiguous!') AS topic
FROM Posts AS P
LEFT JOIN Keywords AS K
ON CONCAT(' ', LOWER(P.content), ' ') LIKE CONCAT('% ', LOWER(K.word), ' %')
GROUP BY P.post_id
