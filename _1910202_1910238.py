import numpy as np
from numpy import random

import copy

def is_full_board(board, mini = False):
    if not mini:
        for cell in board:
            if cell == 0:
                return False
    else:
        for row in board:
            for cell in row:
                if cell == 0:
                    return False
    return True

#precondition: the board is full
#return 1: agent win
#      -1: agent lose
#       0: draw
# def board_result(agent, player, board, mini = False):
#     agent_number = 0
#     player_number = 0
#     if not mini:
#         for cell in board:
#             if cell == agent:
#                 agent_number += 1
#             else:
#                 player_number += 1
#     else:
#         for row in board:
#             for cell in row:
#                 if cell == agent:
#                     agent_number += 1
#                 else:
#                     player_number += 1
#     if agent_number > player_number:
#         return 1
#     elif agent_number < player_number:
#         return -1
#     else:
#         return 0

# def eval_mini_board(board, agent):
#     eval_map = [
#         [3, 2, 3],
#         [2, 4, 2],
#         [3, 2, 3]
#     ]
#     if is_full_board(board, True):
#         if board_result == 1:
#             return 24
#         elif board_result == -1:
#             return -24
#         else:
#             return 0
    # else:
    #     result = 0
    #     for i in range(3):
    #         for j in range(3):
    #             if (board[i][j] == agent):
    #                 result += eval_map[i][j]
    #             elif (board[i][j] == -agent):
    #                 result -= eval_map[i][j]
    #     return result

# def eval(state):
#     eval_map = [3, 2, 3, 2, 4, 2, 3, 2, 3]
#     if is_full_board(state.global_cells):
#         temp_result = board_result(state.player_to_move, -state.player_to_move, state.global_cells)
#         if (temp_result == 1):
#             return 150000
#         elif (temp_result == -1):
#             return -150000
#         else:
#             return 0
    # else:
    #     result = 0

    #     for i in range(len(state.blocks)):
    #         result += eval_mini_board(state.blocks[i], state.player_to_move) * eval_map[i]
    #     return result

def eval_mini_board(state, board):
    eval_map = [
        [3, 2, 3],
        [2, 4, 2],
        [3, 2, 3]
    ]
    temp_result = state.game_result(board)
    if temp_result == state.player_to_move:
        return 24
    elif temp_result == -state.player_to_move:
        return -24
    
    elif temp_result == 0.:
        return 0
    else:
        result = 0
        for i in range(3):
            for j in range(3):
                if (board[i][j] == state.player_to_move):
                    result += eval_map[i][j]
                elif (board[i][j] == -state.player_to_move):
                    result -= eval_map[i][j]
        return result




def eval(state):
    eval_map = [3, 2, 3, 2, 4, 2, 3, 2, 3]
    temp_result = state.game_result(state.global_cells.reshape(3,3))
    if temp_result == state.player_to_move:
        return 150000
    elif temp_result == -state.player_to_move:
        return -150000
    elif temp_result == 0.:
        return 0
    else:
        result = 0

        for i in range(len(state.blocks)):
            result += eval_mini_board(state, state.blocks[i]) * eval_map[i]
        return result












# def eval1_mini_board(state, array_board):
#     # if miniB.is_board_full():
#     #     return 0
#     POSSIBLE_WIN_SEQUENCES = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
#     APPROXIMATE_WIN_SCORE = 7
#     player_counter = 0
#     opponent_counter = 0
#     # player_str = str(player)
#     # opponent_str = str(player.opponent())
#     # miniB_as_list = miniB.get_board()
#     for seq in POSSIBLE_WIN_SEQUENCES:
#         filtered_seq = [array_board[index] for index in seq if array_board[index] != 0]
#         if state.player_to_move in filtered_seq:
#             if -state.player_to_move in filtered_seq:
#                 continue
#             if len(filtered_seq) > 1:
#                 player_counter += APPROXIMATE_WIN_SCORE
#             player_counter += 1
#         elif -state.player_to_move in filtered_seq:
#             if len(filtered_seq) > 1:
#                 opponent_counter += APPROXIMATE_WIN_SCORE
#             opponent_counter += 1
#     return player_counter - opponent_counter

# def count_free_cells(array_board):
#     count = 0
#     for cell in array_board:
#         if cell == 0:
#             count += 1
#     return count

        
# def eval1(state):
#     WIN_SCORE = 10**6
#     BIG_BOARD_WEIGHT = 23
#     temp_result = state.game_result(state.global_cells.reshape(3,3))
#     if temp_result != 0:
#         free_cells = 0
#         for i in range(9):
#             mini_board = state.blocks[i].reshape(-1)
#             free_cells += count_free_cells(mini_board)
#         return WIN_SCORE + free_cells if temp_result == state.player_to_move else -WIN_SCORE - free_cells
#     elif temp_result == 0:
#         return 0
#     else:
#         result = eval1_mini_board(state, state.global_cells) * BIG_BOARD_WEIGHT 
#         for i in range(9):
#             board = state.blocks[i].reshape(-1)
#             if not is_full_board(board):
#                 result += eval1_mini_board(state, board)
#         return result










def minimax_alpha_beta(state, a, b, depth, depth_limit, is_minimum = True):
    valid_moves = state.get_valid_moves


    if not len(valid_moves) or depth == depth_limit:
        return eval(state)
    else:
        alpha = -np.inf
        beta = np.inf
        if is_minimum:
            for successor_move in valid_moves:

                new_state = copy.deepcopy(state)
                new_state.act_move(successor_move)

                val = minimax_alpha_beta(new_state, a, min(b, beta), depth + 1, depth_limit, not is_minimum)
                beta = min(beta, val)
                if a >= beta:
                    return beta
            return beta
        else:
            for successor_move in valid_moves:
                
                new_state = copy.deepcopy(state)
                new_state.act_move(successor_move)

                val = minimax_alpha_beta(new_state, max(a, alpha), b, depth + 1, depth_limit, not is_minimum)
                alpha = max(alpha, val)
                if alpha >= b:
                    return alpha
            return alpha



class UltimateTTT_Move:
    
    def __init__(self, index_local_board, x_coordinate, y_coordinate, value):
        self.index_local_board = index_local_board
        self.x = x_coordinate
        self.y = y_coordinate
        self.value = value
    

    def __repr__(self):
        return "local_board:{0}, (x:{1} y:{2}), value:{3}".format(
                self.index_local_board,
                self.x,
                self.y,
                self.value       
            )




x = 0
y = 0
i = 0



def get_block(x, y):
    return 3*x + y


def ultimate_move(cur_state):
    global i,x,y
    if cur_state.blocks[4, 1, 1] == 0:
        i = 1
        return UltimateTTT_Move(4, 1, 1, cur_state.player_to_move)
    else:
        if i < 8:
            b = get_block(cur_state.previous_move.x, cur_state.previous_move.y)
            i += 1
            return UltimateTTT_Move(b, 1, 1, cur_state.player_to_move)
        elif i == 8:
            x = cur_state.previous_move.x
            y = cur_state.previous_move.y
            i += 1
            return UltimateTTT_Move(get_block(x, y), x, y, cur_state.player_to_move)
        else:
            if cur_state.previous_move.x == 1 and cur_state.previous_move.y == 1:
                cur_state.free_move = True
                op_x = 2 - x
                op_y = 2 - y
                b = get_block(op_x, op_y)
                if cur_state.blocks[b, x, y] == 0:
                    return UltimateTTT_Move(b, x, y, cur_state.player_to_move)
                else:
                    return UltimateTTT_Move(b, op_x, op_y, cur_state.player_to_move)
            else:
                b = get_block(cur_state.previous_move.x,
                             cur_state.previous_move.y)
                if cur_state.blocks[b, x, y] == 0:
                    return UltimateTTT_Move(b, x, y, cur_state.player_to_move)
                else:
                    return UltimateTTT_Move(b, 2 - x, 2 - y, cur_state.player_to_move)



def select_move(cur_state, remain_time): 
    if cur_state.player_to_move == 1:
        return ultimate_move(cur_state)
    else:
        
        valid_moves = cur_state.get_valid_moves

        cur_max = -np.inf
        result_index = -1

        if cur_state.previous_move == None:
            depth_limit = 1
        else:
            depth_limit = 3

        if len(valid_moves) != 0:
            for i in range(len(valid_moves)):
                new_state = copy.deepcopy(cur_state)
                new_state.act_move(valid_moves[i])
                temp = minimax_alpha_beta(new_state, -np.inf, np.inf, 0, depth_limit)
                
                if temp > cur_max:
                    cur_max = temp
                    result_index = i
            return valid_moves[result_index]
        return None






# def select_move(cur_state, remain_time):
#     valid_moves = cur_state.get_valid_moves

#     cur_max = -np.inf
#     result_index = -1

#     if cur_state.previous_move == None:
#         depth_limit = 1
#     else:
#         depth_limit = 3

#     if len(valid_moves) != 0:
#         for i in range(len(valid_moves)):
#             new_state = copy.deepcopy(cur_state)
#             new_state.act_move(valid_moves[i])
#             temp = minimax_alpha_beta(new_state, -np.inf, np.inf, 0, depth_limit)
            
#             if temp > cur_max:
#                 cur_max = temp
#                 result_index = i
#         return valid_moves[result_index]
#     return None
