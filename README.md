Cross-Quantilogram
===========================

This is a Python3 implementation of econometric method `Cross-Quantilogram`  invented by [Han et al.(2016)](https://github.com/wangys96/Cross-Quantilogram/blob/master/docs/The%20Cross-Quantilogram%20Measuring%20quantile%20dependence%20and%20testing%20directional%20predictability%20between%20time%20series.pdf).


The `Cross-Quantilogram`(CQ) measures the quantile dependence between two time series. It can be applied to test the hypothesis that one time  series has no directional predictability to another. Stationary bootstrap method help establish the asymptotic distribution for CQ and the corresponding test statistics.

This repo has included:
* `Cross-Quantilogram` accelerated by Numpy.
* Stationary Bootstrap method accelerated by Numpy.
* Portmenteau test(Ljung-Box or Box-Pierce) accelerated by Numpy.
* Three Typical CQ methodologies'  APIs.      
* Matplotlib results plotting for 3 typical methods.

If you have any question or idea, please create issues or contact me:
* Email: richardwang96@qq.com
* WeChat: 89516821

## Dependencies

* Python 3
* Numpy 1.16 + MKL
* Panadas 0.23
* statsmodels 0.9
* matplotlib 3.0.2

I recommand to install [Anaconda 3](https://www.anaconda.com/) first, then Numpy+MKL ([you can get it here](https://www.lfd.uci.edu/~gohlke/pythonlibs/)).

I haven't finish it so there is not a `setup.py`, please just download and put it to your projects' directory or `site-packages/`. The setuptool will soon be added.

## Documents

Firstly, to fully understand CQ and its methodology, you can start with reading these papers:

* [The intraday directional predictability of large Australian stocks: A cross-quantilogram analysis](https://github.com/wangys96/Cross-Quantilogram/blob/master/docs/The-intraday-directional-predictability-of-large-Australian-_2017_Economic-M.pdf)
* [Spillovers and Directional Predictability with a Cross-Quantilogram Analysis The Case of US and Chinese Agricultural Futures](https://github.com/wangys96/Cross-Quantilogram/blob/master/docs/Spillovers%20and%20Directional%20Predictability%20with%20a%20Cross-Quantilogram%20Analysis%20The%20Case%20of%20US%20and%20Chinese%20Agricultural%20Futures.pdf)
* [Directional predictability from stock market sector indices to gold: A cross-quantilogram analysis](https://github.com/wangys96/Cross-Quantilogram/blob/master/docs/Directional%20predictability%20from%20stock%20market%20sector%20indices%20to%20gold%20A%20Cross-Quantilogram%20analysis.pdf)
* [Does international oil volatility have directional predictability for stock returns Evidence from BRICS countries based on cross-quantilogram analysis](https://github.com/wangys96/Cross-Quantilogram/blob/master/docs/Does%20international%20oil%20volatility%20have%20directional%20predictability%20for%20stock%20returns%20Evidence%20from%20BRICS%20countries%20based%20on%20cross-quantilogram%20analysis.pdf)

Then please read the [User Guide](https://nbviewer.jupyter.org/github/wangys96/Cross-Quantilogram/blob/master/docs/User%20Guide.ipynb). The User Guide is a Jupyter Notebook where I introduced the function details and the research methodology. 


## References

 Han H, Linton O, Oka T, et al. The cross-quantilogram: measuring quantile dependence and testing directional predictability between time series[J]. Journal of Econometrics, 2016, 193(1): 251-270.
