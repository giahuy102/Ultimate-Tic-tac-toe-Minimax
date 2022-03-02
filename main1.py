from state import State, State_2
import time
from importlib import import_module

import xlwt
from xlwt import Workbook


def main(player_X, player_O, index, sheet1, rule = 1):
    dict_player = {1: 'X', -1: 'O'}
    if rule == 1:
        cur_state = State()
    else:
        cur_state = State_2()
    turn = 1    

    limit = 81
    remain_time_X = 120
    remain_time_O = 120
    
    player_1 = import_module(player_X)
    player_2 = import_module(player_O)
    
    
    while turn <= limit:
        # print("turn:", turn, end='\n\n')
        if cur_state.game_over:
            # print("winner:", dict_player[cur_state.player_to_move * -1])
            if player_O == '_MSSV':
                sheet1.write(index + 2, 0, dict_player[cur_state.player_to_move * -1])
            else:
                sheet1.write(index + 2, 3, dict_player[cur_state.player_to_move * -1])
            break
        
        start_time = time.time()
        if cur_state.player_to_move == 1:
            new_move = player_1.select_move(cur_state, remain_time_X)
            elapsed_time = time.time() - start_time
            remain_time_X -= elapsed_time
        else:
            new_move = player_2.select_move(cur_state, remain_time_O)
            elapsed_time = time.time() - start_time
            remain_time_O -= elapsed_time
            
        if new_move == None:
            break
        
        if remain_time_X < 0 or remain_time_O < 0:
            # print("out of time")
            # print("winner:", dict_player[cur_state.player_to_move * -1])
            if player_O == '_MSSV':
                sheet1.write(index + 2, 0, dict_player[cur_state.player_to_move * -1])
            else:
                sheet1.write(index + 2, 3, dict_player[cur_state.player_to_move * -1])
            break
                
        if elapsed_time > 10.0:
            # print("elapsed time:", elapsed_time)
            # print("winner: ", dict_player[cur_state.player_to_move * -1])
            if player_O == '_MSSV':
                sheet1.write(index + 2, 0, dict_player[cur_state.player_to_move * -1])
            else:
                sheet1.write(index + 2, 3, dict_player[cur_state.player_to_move * -1])
            break
        
        cur_state.act_move(new_move)
        # print(cur_state)
        
        turn += 1
        
    # print("X:", cur_state.count_X)
    # print("O:", cur_state.count_O)
    if player_O == '_MSSV':
        sheet1.write(index + 2, 1, cur_state.count_X)
        sheet1.write(index + 2, 2, cur_state.count_O)
    else:
        sheet1.write(index + 2, 4, cur_state.count_X)
        sheet1.write(index + 2, 5, cur_state.count_O)




# main('_MSSV', 'random_agent')

wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')
sheet1.write(1, 0, 'Winner')
sheet1.write(1, 1, 'X')
sheet1.write(1, 2, 'O')
sheet1.write(1, 3, 'Winner')
sheet1.write(1, 4, 'X')
sheet1.write(1, 5, 'O')


for index in range(100):
    main('random_agent', '_MSSV', index, sheet1)

# for index in range(100):
#     main('_MSSV', 'random_agent', index, sheet1)

wb.save('result1.xls')