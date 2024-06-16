import math


def md_nre_single_sample(y, y_hat, p):
    MD_RE = (math.sqrt(y) - math.sqrt(y_hat)) ** p

    return MD_RE


print(md_nre_single_sample(y=100, y_hat=99.5, p=1))
print(md_nre_single_sample(y=50, y_hat=49.5, p=1))
print(md_nre_single_sample(y=20, y_hat=19.5, p=1))
print(md_nre_single_sample(y=0.6, y_hat=0.1, p=1))
