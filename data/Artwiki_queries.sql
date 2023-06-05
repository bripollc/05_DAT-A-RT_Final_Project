USE wikiart;
SELECT * FROM wikiart.artwiki_artworks;


-- 00. Number of artworks by movement and style
SELECT Style, Movement, COUNT(*) AS count_of_movement
FROM wikiart.artwiki_artworks
GROUP BY Style, Movement
ORDER BY Style ASC;

 -- 01.Average of feelings by "Movement" (positive, neutral and negative)
SELECT Movement, 
		-- Image + Title
       ROUND(AVG(IT_gratitude) + AVG(IT_happiness) + AVG(IT_humility) + AVG(IT_love) + AVG(IT_optimism) + AVG(IT_trust), 2) AS IT_pos_avg,
       ROUND(AVG(IT_agreeableness) + AVG(IT_anticipation) + AVG(IT_disagreeableness) + AVG(IT_neutral) + AVG(IT_surprise) + AVG(IT_shyness), 2) AS IT_neu_avg,
       ROUND(AVG(IT_anger) + AVG(IT_arrogance) + AVG(IT_disgust) + AVG(IT_fear) + AVG(IT_pessimism) + AVG(IT_regret) + AVG(IT_sadness) + AVG(IT_shame), 2) AS IT_neg_avg,
		-- Image only
	   ROUND(AVG(I_gratitude) + AVG(I_happiness) + AVG(I_humility) + AVG(I_love) + AVG(I_optimism) + AVG(I_trust), 2) AS I_pos_avg,
       ROUND(AVG(I_agreeableness) + AVG(I_anticipation) + AVG(I_disagreeableness) + AVG(I_neutral) + AVG(I_surprise) + AVG(I_shyness), 2) AS I_neu_avg,
       ROUND(AVG(I_anger) + AVG(I_arrogance) + AVG(I_disgust) + AVG(I_fear) + AVG(I_pessimism) + AVG(I_regret) + AVG(I_sadness) + AVG(I_shame), 2) AS I_neg_avg,
		-- Title only
	   ROUND(AVG(T_gratitude) + AVG(T_happiness) + AVG(T_humility) + AVG(T_love) + AVG(T_optimism) + AVG(T_trust), 2) AS T_pos_avg,
       ROUND(AVG(T_agreeableness) + AVG(T_anticipation) + AVG(T_disagreeableness) + AVG(T_neutral) + AVG(T_surprise) + AVG(T_shyness), 2) AS T_neu_avg,
       ROUND(AVG(T_anger) + AVG(T_arrogance) + AVG(T_disgust) + AVG(T_fear) + AVG(T_pessimism) + AVG(T_regret) + AVG(T_sadness) + AVG(T_shame), 2) AS T_neg_avg
FROM wikiart.artwiki_artworks
GROUP BY Movement
ORDER BY Movement ASC;

 -- 02.Average of feelings by "Style" (positive, neutral and negative)
SELECT Style, 
		-- Image + Title
       ROUND(AVG(IT_gratitude) + AVG(IT_happiness) + AVG(IT_humility) + AVG(IT_love) + AVG(IT_optimism) + AVG(IT_trust), 2) AS IT_pos_avg, -- pos
       ROUND(AVG(IT_agreeableness) + AVG(IT_anticipation) + AVG(IT_disagreeableness) + AVG(IT_neutral) + AVG(IT_surprise) + AVG(IT_shyness), 2) AS IT_neu_avg, -- neu
       ROUND(AVG(IT_anger) + AVG(IT_arrogance) + AVG(IT_disgust) + AVG(IT_fear) + AVG(IT_pessimism) + AVG(IT_regret) + AVG(IT_sadness) + AVG(IT_shame), 2) AS IT_neg_avg, -- neg
		-- Image only
	   ROUND(AVG(I_gratitude) + AVG(I_happiness) + AVG(I_humility) + AVG(I_love) + AVG(I_optimism) + AVG(I_trust), 2) AS I_pos_avg, -- pos
       ROUND(AVG(I_agreeableness) + AVG(I_anticipation) + AVG(I_disagreeableness) + AVG(I_neutral) + AVG(I_surprise) + AVG(I_shyness), 2) AS I_neu_avg, -- neu
       ROUND(AVG(I_anger) + AVG(I_arrogance) + AVG(I_disgust) + AVG(I_fear) + AVG(I_pessimism) + AVG(I_regret) + AVG(I_sadness) + AVG(I_shame), 2) AS I_neg_avg, -- neg
		-- Title only
	   ROUND(AVG(T_gratitude) + AVG(T_happiness) + AVG(T_humility) + AVG(T_love) + AVG(T_optimism) + AVG(T_trust), 2) AS T_pos_avg, -- pos
       ROUND(AVG(T_agreeableness) + AVG(T_anticipation) + AVG(T_disagreeableness) + AVG(T_neutral) + AVG(T_surprise) + AVG(T_shyness), 2) AS T_neu_avg, -- neu
       ROUND(AVG(T_anger) + AVG(T_arrogance) + AVG(T_disgust) + AVG(T_fear) + AVG(T_pessimism) + AVG(T_regret) + AVG(T_sadness) + AVG(T_shame), 2) AS T_neg_avg -- neg
FROM wikiart.artwiki_artworks
GROUP BY Style
ORDER BY Style ASC;

 -- 03.Top 10 artworks with more POSITIVE avg
SELECT  Movement, Title, Artist,
       ROUND(AVG(IT_gratitude) + AVG(IT_happiness) + AVG(IT_humility) + AVG(IT_love) + AVG(IT_optimism) + AVG(IT_trust), 2) AS pos_avg
FROM wikiart.artwiki_artworks
GROUP BY Title, Artist, Movement
ORDER BY pos_avg DESC
LIMIT 10;

 -- 04.Top 10 artworks with more NEGATIVE avg
SELECT  Movement, Title, Artist,
       ROUND(AVG(IT_anger) + AVG(IT_arrogance) + AVG(IT_disgust) + AVG(IT_fear) + AVG(IT_pessimism) + AVG(IT_regret) + AVG(IT_sadness) + AVG(IT_shame), 2) AS neg_avg
FROM wikiart.artwiki_artworks
GROUP BY Title, Artist, Movement
ORDER BY neg_avg DESC
LIMIT 10;

 -- 05.Top 10 artworks with more NEUTRAL avg
SELECT  Movement, Title, Artist,
	ROUND(AVG(IT_agreeableness) + AVG(IT_anticipation) + AVG(IT_disagreeableness) + AVG(IT_neutral) + AVG(IT_surprise) + AVG(IT_shyness), 2) AS neu_avg
FROM wikiart.artwiki_artworks
GROUP BY Title, Artist, Movement
ORDER BY neu_avg DESC
LIMIT 10;

 -- 06. Number of works according to whether they are paintings or not and whether they are faces or bodies, by artistic movement.
SELECT Movement,
	COUNT(*) AS total,
	COUNT(CASE WHEN Painting_Y_N = 'yes' THEN 1 END) AS painting,
	COUNT(CASE WHEN Painting_Y_N = 'no' THEN 1 END) AS no_painting,
	COUNT(CASE WHEN `Face/Body` = 'face' THEN 1 END) AS face,
	COUNT(CASE WHEN `Face/Body` = 'body' THEN 1 END) AS body,
	COUNT(CASE WHEN `Face/Body` = 'None' THEN 1 END) AS none
FROM wikiart.artwiki_artworks
GROUP BY Movement;

 -- 07.Top 15 artists with higher number of artworks in the database
SELECT Artist, COUNT(*) AS count_of_artworks
FROM wikiart.artwiki_artworks
GROUP BY Artist
ORDER BY count_of_artworks DESC
LIMIT 10;

 -- 08.Top 15 words more frequent in "Title"
SELECT word, frequency
FROM (
    SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(Title, ' ', numbers.n), ' ', -1) AS word,
           COUNT(*) AS frequency
    FROM wikiart.artwiki_artworks
    INNER JOIN (
        SELECT 1 AS n UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4
        UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8
        UNION ALL SELECT 9 UNION ALL SELECT 10
    ) numbers
    ON CHAR_LENGTH(Title) - CHAR_LENGTH(REPLACE(Title, ' ', '')) >= numbers.n - 1
    GROUP BY word
) t
WHERE word NOT IN ('the', 'of', 'a', 'and', 'with', 'de', 'at', 'on', 'from', 'La', 'In', 'I', 'to', 'his', 'II', 'For', '-', 'by')
ORDER BY frequency DESC
LIMIT 15;

 -- 09.Average rating by movement
	-- min
SELECT MIN(Avg_rating) AS min_avg
FROM artwiki_artworks; -- (-2.0)
	-- max
SELECT MAX(Avg_rating) AS min_avg
FROM artwiki_artworks; -- (-2.8)

SELECT Movement, AVG(Avg_rating) AS avg_rating
FROM wikiart.artwiki_artworks
GROUP BY Movement
ORDER BY avg_rating DESC;

 -- 10.Top 10 artwork with higher average rating
SELECT Movement, Title, Artist, Avg_rating
FROM wikiart.artwiki_artworks
ORDER BY Avg_rating DESC
LIMIT 10;

 -- 11.Top 10 artwork with lower average rating
SELECT Movement, Title, Artist, Avg_rating
FROM wikiart.artwiki_artworks
ORDER BY Avg_rating ASC
LIMIT 10;

 -- 12. Total of artworks published by century
	-- min
SELECT MIN(Year) AS min_year
FROM artwiki_artworks;
	-- max
SELECT MAX(Year) AS max_year
FROM wikiart.artwiki_artworks
WHERE Year NOT LIKE '%cent.';

SELECT CONCAT(
    FLOOR((CAST(SUBSTRING(Year, 1, 4) AS UNSIGNED) - 1) / 100) + 1,
    'th century'
) AS century,
COUNT(*) AS count
FROM artwiki_artworks
WHERE Year NOT LIKE '%cent.'
    AND Year >= '1415'
    AND Year <= '2012'
GROUP BY century
ORDER BY MIN(Year);


