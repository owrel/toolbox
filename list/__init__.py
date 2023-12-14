__all__ = ['common_element']


def common_element(l1:list, l2:list):
    return len(set(l1) & set(l2))