/*
https://school.programmers.co.kr/learn/courses/30/lessons/178871
달리기 경주
*/

package lv1

import "fmt"

func race() {
	// 예제용 데이터
	players := []string{
		"mumu", "soe", "poe", "kai", "mine",
	}
	callings := []string{
		"kai", "kai", "mine", "mine",
	}

	fmt.Println(race_solution(players, callings))
}

// 정답 함수
func race_solution(players []string, callings []string) []string {
	// 순위 저장용 딕셔너리 키:이름, 값:순위
	var rank = make(map[string]int)

	// 선수 이름 호명 시 순위배열과 딕셔너리에서 앞 사람과 교체
	call := func(player string) {
		winner_name := player
		winner_rank := rank[winner_name]

		loser_name := players[winner_rank-1]
		loser_rank := rank[loser_name]

		swap_name := loser_name
		players[winner_rank-1] = winner_name
		players[winner_rank] = swap_name

		swap_rank := loser_rank
		rank[loser_name] = winner_rank
		rank[winner_name] = swap_rank
	}

	// 초기 저장작업
	for i, player := range players {
		rank[player] = i
	}

	// 함수 실행
	for _, player := range callings {
		call(player)
	}

	return players
}
