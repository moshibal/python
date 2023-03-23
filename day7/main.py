test_h=int(input("give the height. "))
test_w=int(input("give the width. "))
coverage=5
def cal_paint(test_h,test_w,coverage):
    number_of_cans=round((test_h*test_w)/coverage)
    print(f"the number of can required is {number_of_cans}")
cal_paint(test_h,test_w,coverage)