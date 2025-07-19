# Write your MySQL query statement below
SELECT DISTINCT v1.viewer_id AS id
FROM Views v1 JOIN Views v2
ON v1.author_id = v2.viewer_id AND v1.viewer_id = v2.viewer_id ORDER BY id;

