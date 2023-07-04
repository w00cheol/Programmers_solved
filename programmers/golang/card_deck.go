/*
https://school.programmers.co.kr/learn/courses/30/lessons/159994
카드 뭉치
*/

package lv1

import (
	"fmt"
)

func card_deck() {
	// 예제용 데이터
	cards1 := []string{
		"i", "drink", "water",
	}
	cards2 := []string{
		"want", "to",
	}
	goal := []string{
		"i", "want", "to", "drink", "water",
	}

	fmt.Println(card_deck_solution(cards1, cards2, goal))
}

// 정답 함수
func card_deck_solution(cards1 []string, cards2 []string, goal []string) string {
	runner_1, runner_2 := 0, 0 // 각 배열 순회하는 인덱스 값

	for _, word := range goal { // 각 배열의 runner 기준으로 순회
		if runner_1 < len(cards1) && word == cards1[runner_1] {
			runner_1++
		} else if runner_2 < len(cards2) && word == cards2[runner_2] {
			runner_2++
		} else { // 두 배열 모두 존재하지 않으면 No 리턴
			return "No"
		}
	}

	return "Yes"
}
