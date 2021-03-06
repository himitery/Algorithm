## 채널링

#### ⚙ 문제 설명

    N명의 참가자로 이루어진 격투게임 대회에서는 모든 참가자들이 단 하나의 채널링 스킬만으로 전투를 진행한다. 채널링 스킬은 지속시간 동안 효과를 유지하기 위해 스킬을 사용한 사람이 다른 행동을 할 수 없는 스킬을 말한다. 예를 들어 스킬을 사용한 시간이 (1, 6)이라면 1초가 된 순간부터 6초가 될 때까지 스킬을 사용하며 움직일 수 없다.

    모든 참가자들은 대회가 진행되는 시간 동안 스킬을 단 한 번 사용할 수 있다. 또한, 참가자들은 모두 매우 뛰어난 실력을 가지고 있기에 자신보다 먼저 스킬을 사용하고 있는 참가자가 있는 경우 해당 참가자의 스킬이 적용된 범위를 벗어난 곳에서 해당 참가자를 공격할 수 있는 범위를 찾아 스킬을 사용한다.

    예를 들어, 1번 참가자가 스킬을 사용한 시간이 (s1, e1)이고, 2번 참가자가 스킬을 사용한 시간이 (s2, e2)일 때 s2 < s1 < e2 를 만족하는 경우 1번 참가자는 항상 2번 참가자의 공격을 피하며 2번 참가자를 공격할 수 있다.

    참가자 수와 참가자들이 스킬을 사용한 시간이 주어졌을 때, 각각의 참가자들이 공격할 수 있는 사람의 수를 구해보자.

#### ⚙ 입력

    첫 번째 줄에는 경기의 참가자의 수 N이 주어진다.
    (2 <= N <= 100,000)

    두 번째 줄부터 각각의 참가자가 결정한 스킬의 시작시간과 종료 시간이 si, ei의 형태로 한 줄에 하나씩 주어진다.
    (1 <= si <= ei <= 1,000,000,000)

    si는 스킬을 사용하기 시작한 시간을, ei는 스킬 사용을 종료하는 시간을 뜻하며, 주어지는 시간은 항상 범위 내의 정수이다.

#### ⚙ 출력

    각 참가자가 공격할 수 있는 참가자의 수를 한 줄에 하나씩 출력한다.

#### ⚙ 입/출력 예시

- 예시 1

  - 입력

        9
        15 32
        41 100
        54 58
        26 75
        3 71
        48 52
        30 83
        66 79
        9 37

  - 출력

        2
        3
        4
        3
        0
        4
        4
        4
        1

- 예시 2

  - 입력

        4
        12 71
        51 79
        17 87
        9 28

  - 출력

        1
        2
        2
        0
