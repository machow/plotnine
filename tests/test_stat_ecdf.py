import pandas as pd

from plotnine import aes, after_stat, ggplot, stat_ecdf

data = pd.DataFrame({"x": range(10)})
p = ggplot(data, aes("x")) + stat_ecdf(size=2)


def test_ecdf():
    p = ggplot(data, aes("x")) + stat_ecdf(size=2)

    assert p == "ecdf"


def test_computed_y_column():
    p = (
        ggplot(data, aes("x"))
        + stat_ecdf(size=2)
        # Should be able to used computed y column & create a
        # new mapped column also called y
        + stat_ecdf(aes(y=after_stat("y-0.2")), size=2, color="blue")
    )
    assert p == "computed_y_column"
