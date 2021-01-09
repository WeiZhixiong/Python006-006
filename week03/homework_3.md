#### sql Ö´ÐÐË³Ðò
```
SELECT DISTINCT player_id, player_name, count(*) as num          Ö´ÐÐË³Ðò: 5
FROM player JOIN team ON player.team_id = team.team_id           Ö´ÐÐË³Ðò: 1
WHERE height > 1.80                                              Ö´ÐÐË³Ðò: 2
GROUP BY player.team_id                                          Ö´ÐÐË³Ðò: 3
HAVING num > 2                                                   Ö´ÐÐË³Ðò: 4
ORDER BY num DESC                                                Ö´ÐÐË³Ðò: 6
LIMIT 2                                                          Ö´ÐÐË³Ðò: 7
```