from calculator import square


def main():
    # ---1st method----
    # if square(2) != 4:
    #     print('Something goes wrong')
    # if square(3) != 9:
    #     print("something goes wrong")
        
    # --2nd method--
    # try:
    #     assert square(2) == 4
    # except AssertionError:
    #     print('2 square was not 4')
    # try:
    #     assert square(3) == 9
    # except ArithmeticError:
    #     print('3 square was not 9')

    # --3rd method--
    assert square(2) == 4
    assert square(3) == 9 
    assert square(0) == 0
    # for test we need to use our terminal and wirte pytest + file_name



    
    
# if __name__=="__main__":
#     main()           