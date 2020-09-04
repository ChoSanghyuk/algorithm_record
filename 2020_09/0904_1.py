# 가래떡썰기 (수업)
def cut(mozzi , wish):
    max_ = max(mozzi)-1
    for i in range(max_, max_-wish, -1):
        len_ = sum([ j-i if j-i>0 else 0 for j in mozzi])
        if len_ >= wish:
            return i