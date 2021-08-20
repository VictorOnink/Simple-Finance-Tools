import math
import numpy as np


def discount_factor(r, t):
    """
    Calculating the discount factor at a time t, where this is given by
    DF = (1 + r) ** t

    :param r: the rate of return
    :param t: the number of time periods
    :return:
    """
    return (1 + r) ** t


def future_value(CF, r, t):
    """
    The future value of a cash flow at time t=0 at time t>0
    :param CF: the cash flow at t=0
    :param r: the rate of return
    :param t: number of time periods
    :return:
    """
    return CF * discount_factor(r, t)


def present_value(CF, r, t):
    """
    The present value of a cash flow at t time intervals in the future
    :param CF: the cash flow at t>0
    :param r: the rate of return
    :param t: number of time intervals in the future that we are discounting back
    :return:
    """
    return CF * discount_factor(r, t)


def annuity_PV(CF, r, t, g=0):
    """
    The present value of an annuity that pays out cash flow CF at time t=0 over t time periods
    :param CF: cash flow being paid at t=1
    :param r: rate of return
    :param g: growth rate of the cash flow/annuity payout
    :param t: number of time periods
    :return:
    """
    assert r > g, 'Underlying assumption of this calculation is that r > g'
    return CF / (r - g) * (1 - ((1 + r) / (1 + g)) ** -t)


def perpetuity_PV(CF, r, g=0):
    """
    The present value of a perpetuity that pays out cash flow CF at time t=0
    :param CF: cash flow being paid at t=1
    :param r: rate of return
    :param g: growth rate of the cash flow/annuity payout
    :return:
    """
    assert r > g, 'Underlying assumption of this calculation is that r > g'
    return CF / (r - g)


def after_tax_return(r, tax):
    """
    The after tax return for a nominal return r and tax rate tax
    :param r: nominal rate of return
    :param tax: tax rate
    :return:
    """
    return r * (1 - tax)


def real_return_inflation(r, i):
    """
    The real rate of return assuming a nominal rate of return r and an inflation rate i, where the real rate of retur
    is defined as:
    1 + rr = (1 + r) / (1 + i)
    :param r:
    :param i:
    :return:
    """
    return (1 + r) / (1 + i) - 1


def convert_APR_to_EAR(apr, k):
    """
    Calculating the effective annual rate (EAR) from the annual percentage rate, assuming that we compound k times per
    year
    :param apr:
    :param k:
    :return:
    """
    period_interest_rate = apr / k
    return (1 + period_interest_rate) ** k - 1