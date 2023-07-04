/*
https://school.programmers.co.kr/learn/courses/30/lessons/150370
개인정보 수집 유효기간
*/

package lv1

import (
	"fmt"
	"strconv"
	"strings"
)

func validity_period() {
	// 예제용 데이터
	today := "2022.05.19"
	terms := []string{
		"A 6", "B 12", "C 3",
	}
	privacies := []string{
		"2021.05.02 A",
		"2021.07.01 B",
		"2022.02.19 C",
		"2022.02.20 C",
	}

	fmt.Println(validity_period_solution(today, terms, privacies))
}

// 정답 함수
func validity_period_solution(today string, terms []string, privacies []string) []int {
	terms_map := make(map[string]int)
	answer := []int{}

	// 월 추가 함수
	addMonth := func(start_date string, period int) string {
		// fotmat 에 맞게 연/월/일 구분
		ymd := strings.Split(start_date, ".")
		y, _ := strconv.Atoi(ymd[0])
		m, _ := strconv.Atoi(ymd[1])
		d, _ := strconv.Atoi(ymd[2])

		m += period // 월 추가

		for m > 12 { // 12 초과 시 연으로 캐리 넘겨줌
			m -= 12
			y += 1
		}

		// m 을 2자리 문자열로 변환
		finish_date := fmt.Sprintf("%04d.%02d.%02d", y, m, d)
		return (finish_date)
	}

	// 유효기간이 유효한지 확인하는 함수
	isValid := func(today string, start_date string, period int) bool {
		// 시작일로부터 기간을 더하여 마감일 계산
		finish_date := addMonth(start_date, period)

		// 오늘과 비교하여 유효성 검증
		for i := range today {
			if today[i] > finish_date[i] {
				return false
			} else if today[i] < finish_date[i] {
				return true
			}
		}
		return false
	}

	// 문자별 기간 저장
	for _, term := range terms {
		t := strings.Split(term, " ")
		terms_map[t[0]], _ = strconv.Atoi(t[1])
	}

	// 각각의 개인정보에 대해 유효성 검증 및 파기할 정보 인덱스 저장
	for i, privacy := range privacies {
		r := strings.Split(privacy, " ")
		start_date, term_name := r[0], r[1]

		if !isValid(today, start_date, terms_map[term_name]) {
			answer = append(answer, i+1)
		}
	}

	return answer
}
