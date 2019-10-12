from datascience import *


# additional test for comparing tables
def tables_are_same(t1: Table, t2: Table):
    same_labels = set(t1.labels) == set(t2.labels)
    if not same_labels:
        return f"Expected labels '{', '.join(t1.labels)}', found labels '{', '.join(t2.labels)}''"

    for label in t1.labels:
        t1_sorted = t1.sort(label)
        t2_sorted = t2.sort(label)
        c1 = t1_sorted.column(label)
        c2 = t2_sorted.column(label)

        if c1.dtype == float:
            if not all((c1 - c2) < 1e-6):
                return f"Column '{label}' has values that don't match expected values"
        else:
            if not all(c1 == c2):
                return f"Column '{label}' has values that don't match expected values"

    return True
