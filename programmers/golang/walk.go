/*
https://school.programmers.co.kr/learn/courses/30/lessons/172928
공원 산책
*/

package lv1

import (
	"fmt"
	"strconv"
	"strings"
)

func walk() {
	// 예제용 데이터
	park := []string{
		"OSO", "OOO", "OXO", "OOO",
	}
	routes := []string{
		"E 2", "S 3", "W 1",
	}

	fmt.Println(walk_solution(park, routes))
}

// 정답 함수
func walk_solution(park []string, routes []string) []int {
	// 정답 return 배열
	location := make([]int, 2, 2)

	// park 2차원 배열로 변환
	var converted_park = make([][]string, len(park))

	// 방향 초기화
	dy := map[string]int{
		"E": 0, "W": 0, "S": 1, "N": -1,
	}
	dx := map[string]int{
		"E": 1, "W": -1, "S": 0, "N": 0,
	}

	for y, width := range park {
		converted_park[y] = strings.Split(width, "")
	}

	// 시작점(S) 찾기 + 초기화
	for y, width := range converted_park {
		for x := range width {
			if converted_park[y][x] == "S" {
				location[0] = y
				location[1] = x
				break
			}
		}
	}

	// 산책 시작
	for _, route := range routes {
		// 방향과 거리, 성공 시 도착지점 초기화
		d := strings.Split(route, " ")
		direction := d[0]
		distance, _ := strconv.Atoi(d[1])
		moved_y := location[0] + dy[direction]*distance
		moved_x := location[1] + dx[direction]*distance

		// 2중 반복문을 탈출하기 위한 변수 초기화
		var flag bool = true

		// 배열에 벗어나는 예외 검사 (y축, x축)
		if moved_y < 0 || len(converted_park) <= moved_y || moved_x < 0 || len(converted_park[0]) <= moved_x {
			continue
		}

		// 장애물을 만나는 예외 검사
		for i := 1; i <= distance; i++ {
			y := location[0] + dy[direction]*i
			x := location[1] + dx[direction]*i

			// 예외처리: flag 변환 후 for문 탈출
			if converted_park[y][x] == "X" {
				flag = false
				break
			}
		}

		if flag {
			location[0] = moved_y
			location[1] = moved_x
		}
	}

	return location
}
