from board import Board


def test_generate_board():
    board = Board()
    board.generate_board(3, 3)
    assert len(board.list) == 9
    for i in range(9):
        assert board.list[i].index == i
        assert board.list[i].hex_type in ["basic", "sand", "forest", "rock"]
        assert board.list[i].x == 110 + (i % 3) * 60 + (30 if i // 3 % 2 == 0 else 60)
        assert board.list[i].y == 100 + (i // 3) * 52


def test_list_neighbors():
    board = Board()
    board.generate_board(3, 3)
    assert len(board.list_neighbors(board.list[0])) == 2
    assert len(board.list_neighbors(board.list[1])) == 4
    assert len(board.list_neighbors(board.list[2])) == 3
    assert len(board.list_neighbors(board.list[3])) == 5
    assert len(board.list_neighbors(board.list[4])) == 6
    assert len(board.list_neighbors(board.list[5])) == 3
    assert len(board.list_neighbors(board.list[6])) == 2
    assert len(board.list_neighbors(board.list[7])) == 4
    assert len(board.list_neighbors(board.list[8])) == 3


def test_neighbors():
    board = Board()
    board.generate_board(3, 3)
    assert board.neighbors(board.list[0], board.list[1])
    assert board.neighbors(board.list[0], board.list[3])
    assert not board.neighbors(board.list[0], board.list[2])
    assert board.neighbors(board.list[4], board.list[1])
    assert board.neighbors(board.list[4], board.list[3])
    assert board.neighbors(board.list[4], board.list[5])
    assert board.neighbors(board.list[4], board.list[7])
    assert board.neighbors(board.list[4], board.list[8])
    assert not board.neighbors(board.list[4], board.list[0])
    assert not board.neighbors(board.list[4], board.list[6])


def test_isdistance():
    board = Board()
    board.generate_board(3, 3)
    assert board.isdistance(board.list[0], board.list[0], 0)
    assert board.isdistance(board.list[0], board.list[1], 1)
    assert board.isdistance(board.list[0], board.list[3], 1)
    assert board.isdistance(board.list[0], board.list[4], 2)
    assert board.isdistance(board.list[0], board.list[5], 3)
    assert board.isdistance(board.list[0], board.list[7], 2)
    assert board.isdistance(board.list[0], board.list[8], 3)
    assert not board.isdistance(board.list[0], board.list[2], 1)
    assert not board.isdistance(board.list[0], board.list[8], 2)


def test_larger_list_neighbors():
    board = Board()
    board.generate_board(3, 3)
    assert len(board.larger_list_neighbors(board.list[0])) == 4
    assert len(board.larger_list_neighbors(board.list[1])) == 6
    assert len(board.larger_list_neighbors(board.list[2])) == 4
    assert len(board.larger_list_neighbors(board.list[3])) == 6
    assert len(board.larger_list_neighbors(board.list[4])) == 9
    assert len(board.larger_list_neighbors(board.list[5])) == 6
    assert len(board.larger_list_neighbors(board.list[6])) == 4
    assert len(board.larger_list_neighbors(board.list[7])) == 6
    assert len(board.larger_list_neighbors(board.list[8])) == 4
