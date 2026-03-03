# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 21:18:35 2026

@author: USER
"""
#Computation of drawdown
#Nom:Nzedjan Poueme loic germain
#Contact:loic_poueme@gmail.com
#date: Dec 2025

import pandas as pd
import numpy as np
def données (me_m:pd.DataFrame()):
    "la foction attend un fichier csv(header=0, index_col=0, parse_dates=True, na_values=-99.9) et retourne le fichier mis dans standart exploitatable pour l'annalyse "
   # print(me_m)
    #colum=['Lo 10','Hi 10']
    #rets=me_m[colum]
   # print(rets)
    #rets.columns= ['smallcaps','largecaps']
   # print(rets)
    rets=me_m/100
    #rets.plot.line()
    #print(rets.index)
    rets.index= pd.to_datetime(rets.index,format='%Y%m')
    rets.index=rets.index.to_period("M")
    print(rets)
    return rets

def données1 ():
    "la foction attend un fichier csv(header=0, index_col=0, parse_dates=True, na_values=-99.9) et retourne le fichier mis dans standart exploitatable pour l'annalyse "
    me_m1=pd.read_csv('Portfolios_Formed_on_ME_monthly_EW.csv', header=0,index_col=0, parse_dates=True, na_values=-99.99)
    colum=['Lo 20','Hi 20']
    rets1=me_m1[colum]
    rets1.columns= ['smallcaps','largecaps']
    rets1=rets1/100
    #rets1.plot.line()
    rets1.index= pd.to_datetime(rets1.index,format='%Y%m')
    rets1.index=rets1.index.to_period("M")
    return rets1

def anualyse_rets (r,n_period_per_year):
    """this function compute the annualyse returne for a given return serie r at period n"""
    general_ren=(1+r).prod()
    annualyse=general_ren**(n_period_per_year/r.shape[0]) 
    return annualyse-1
def anualyse_vol (r,n_period_per_year):
    """this function compute the annualyse returne for a given return serie r at period n"""
    vol=r.std(ddof=0)
    anual_vol=vol*(n_period_per_year)**0.5
    return anual_vol

def sharpe_ratio(r, risk_free, n_period_year):
    """this function compute de sharpe ration for the r return series with free risk return risk_free for periode n """
    #anualyse risk_free
    rf=((1+risk_free)**(1/n_period_year))  - 1
    #return at tne n period
    excess=r-rf
    annual_ret=anualyse_rets(excess, n_period_year)
    #vality at the period n
    volatilty=anualyse_vol(r,n_period_year)
    #excess_rets
    return annual_ret/volatilty
    

def drawdowns (returns_series):
    """  cette fonction prend en entré une série de rendement sous format pada serie
    et  retourne:
    - Wealt_caps for 1000 dollars d'investissement initiale
    - previous_peak
    - drawndown en pourcent du previous_peak"""
    wealt_caps=1000*(1+returns_series).cumprod()
    previous_peak= wealt_caps.cummax()
    drawdowns= (wealt_caps-previous_peak)/previous_peak
    return drawdowns

def skewness(returns_series2:pd.DataFrame()):
    "la présente fonction permet de prendre en entrée une serie de rendement au format dataframe de pandas et retourne la valeur des paramétres skewness(asymétrie)  pour le jack bera test"
    #evaluation of skewness rappelons que S= E[(E-R)**3]/sigma(R)**3
    sigma=returns_series2.std(ddof=0)
    sigma1=sigma**3
    exp1=(returns_series2-returns_series2.mean())**3.
    exp1=exp1.mean()
    #skewness
    S=exp1/sigma1
    return S
def Kurtosis (returns_series2:pd.DataFrame()):
    "la présente fonction permet de prendre en entrée une serie de rendement au format dataframe de pandas et retourne la valeur des paramétres  kurtossis (applatissement) pour le jack bera test"
    #evaluation of skewness rappelons que S= E[(E-R)**3]/sigma(R)**3
    sigma=returns_series2.std(ddof=0)
    #kurtosis K= E[(E-R)**4]/sigma(R)**4
    sigma2=sigma**4
    exp2=(returns_series2-returns_series2.mean())**4.
    exp2=exp2.mean()
    K=(exp2/sigma2)
    return K

def is_it_normal (returns_series3,level=0.01):
    "This realise the jack_bera test and return a booleen value to certify if the returns series have a normal distribution or not (true or false)"
    import scipy.stats
    bera , pvalue= scipy.stats.jarque_bera(returns_series3)
    return pvalue>level

def semi_deviation (r:pd.DataFrame()):
    """ This function calculates the semi-deviation of a given series.
    Args:
    r: The series as a pd.DataFrame.
    Returns:
    volatility: The semi-deviation of the series (volatility of values less than the mean).
    """
    excess =r-r.mean()
    excess_negative=excess[excess<0]
    num=(excess_negative**2).sum()
    Nb=excess_negative.shape[0]
    semi_deviat=np.sqrt(num/Nb)
    return semi_deviat

def semideviation3(r):
    """
    Returns the semideviation aka negative semideviation of r
    r must be a Series or a DataFrame, else raises a TypeError
    """
    excess= r-r.mean()                                        # We demean the returns
    excess_negative = excess[excess<0]                        # We take only the returns below the mean
    excess_negative_square = excess_negative**2               # We square the demeaned returns below the mean
    n_negative = (excess<0).sum()
    print( excess_negative.std(ddof=0))                       # number of returns under the mean
    return (excess_negative_square.sum()/n_negative)**0.5     # semideviation

def données_ind30 ():
    "la foction attend un fichier csv(header=0, index_col=0, parse_dates=True, na_values=-99.9) et retourne le fichier mis dans standart exploitatable pour l'annalyse "
    rets10=pd.read_csv('ind30_m_vw_rets.csv', header=0,index_col=0, parse_dates=True, na_values=-99.99)
    rets10=rets10/100
    #rets1.plot.line()
    rets10.index= pd.to_datetime(rets10.index,format='%Y%m')
    rets10.index=rets10.index.to_period("M")
    rets10.columns=rets10.columns.str.strip()
    return rets10

def historic_cvar(r,q=5):
   """This function is used to evaluate the historical
   Value at Risk (VaR) at the q% level for a return series r"""
   
   if isinstance (r, pd.DataFrame):
        return r.aggregate (historic_cvar, q = q)
   elif isinstance(r,pd.Series):
        return -np.percentile(r, q, axis= 0)
   else:
       raise TypeError("expected r to be serie or data frame")
       
def vaR_parametric(r,level=0.05,modify=True):
    """This function is used to evaluate with parametrical method 
    Value at Risk (VaR) at the q% level for a return series r"""
    #compute zscore 
    from scipy.stats import norm
    z=norm.ppf (level)
    if modify:
        s=skewness(r)
        k=Kurtosis(r)
        z= (z+(z**2 - 1)*(s/6)+(z**3 - 3*z)*(k-3)/24 - (2*z**3 -5*z)*((s**2)/36))
 

    return -(r.mean() + z*r.std(ddof=0))