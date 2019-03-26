Cross-Quantilogram
===========================
## Introduction
This is a Python3 implementation of the academic method `Cross-Quantilogram`   invented by Han et al.(2016).

$$\rho_α(k)=\frac{E[\psi_{\alpha_1}(x_{1,t}-q_1(\alpha_1))\psi_{\alpha_2}(x_{2,t-k}-q_2(\alpha_2))]}{\sqrt{\psi_{\alpha_1}^2(x_{1,t}-q_1(\alpha_1))}\sqrt{\psi_{\alpha_2}^2(x_{2,t-k}-q_2(\alpha_2))}}$$

The `Cross-Quantilogram`(CQ) measures the quantile dependence between two time series. It can be applied to test the hypothesis that one time  series has no directional predictability to another. Stationary bootstrap method help establish the asymptotic distribution for CQ and the corresponding test statistics.

This repo has included:
* Numpy accelerated `Cross-Quantilogram`.
* Numpy accelerated Stationary Bootstrap method.
* Numpy accelerated Portmenteau test(Ljung-Box or Box-Pierce).
* Typical research methods:
    * CQ at a certain quantile $(\alpha_1,\alpha_2)$ for different lags $\{k|k \in \mathbb{Z^+\}}$.
    * CQ at a certain lag $k$ for different quantile $\{(\alpha_1,\alpha_2)|\alpha_1,\alpha_2 \in \mathbb{Z^+}\}$.
    * Rolling CQ at a certain $(\alpha_1,\alpha_2)$ and a certain lag $k$ for different time period.
* Matplotlib results plotting for 3 typical method.

If you have any question or idea, please create issues or contact me:
* Email: richardwang96@qq.com

---
## Dependencies

* Python 3
* Numpy 1.16 + MKL
* Panadas 0.23
* statsmodels 0.9
* matplotlib 3.0.2

I recommand to install [Anaconda 3](https://www.anaconda.com/) first, then Numpy+MKL ([you can get it here](https://www.lfd.uci.edu/~gohlke/pythonlibs/)).

I haven't finish it so there is not a setup.py, please just download and put it to your projects' directory or `site-packages/`. The setuptool will soon be updated.

---
## How to use

First I hope you can fully understand this academic method. You can start from reading these papers:

* [The intraday directional predictability of large Australian stocks: A cross-quantilogram analysis](http://www.sciencedirect.com/science?_ob=ShoppingCartURL&_method=add&_eid=1-s2.0-S0264999316306691&originContentFamily=serial&_origin=article&_ts=1492368119&md5=491a05e4a63188a64d19190b613b2971)
* [Directional predictability from stock market sector indices to gold: A cross-quantilogram analysis]()



---
## References

 Han H, Linton O, Oka T, et al. The cross-quantilogram: measuring quantile dependence and testing directional predictability between time series[J]. Journal of Econometrics, 2016, 193(1): 251-270.
