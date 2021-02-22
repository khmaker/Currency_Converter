# Currency Converter

Study project from [JetBrains Academy](https://hyperskill.org/projects/157)

## About 
Want to convert one currency to another? You can go to your bank website and do the math by yourself. Or you can write a program to do it quickly and efficiently! The Currency Converter is a simple console program that calculates the amount of money you get by converting one currency to another.

## Description
You're in the bank. Think about how much and what kind of currency you have.

1. Take the currency code, the amount of money that you have, and the currency code that you want to receive as the user input.
2. Retrieve the data from [FloatRates](http://www.floatrates.com/json-feeds.html) as in the previous exercises.
3. Save the exchange rates for USD and EUR.
4. Read the currency to exchange for and the amount of money.
5. Take a look at the cache. Maybe you already have what you need?
6. If you have the currency in your cache, calculate the amount.
7. If not, get it from the site, and calculate the amount.
8. Save all the information to your cache.
9. Repeat steps 3-7 until there is no currency left to process.
10. Print the results.

## Examples

```
> ILS
> USD
> 45
Checking the cache…
Oh! It is in the cache!
You received 13.84 USD.
> RSD
> 57
Checking the cache…
Sorry, but it is not in the cache!
You received 1684.41 RSD.
> EUR
> 33
Checking the cache…
Oh! It is in the cache!
You received 8.38 EUR.
```
```
> USD
> EUR
> 20
Checking the cache…
Oh! It is in the cache!
You received 16.52 EUR.
> NOK
> 45
Checking the cache…
Sorry, but it is not in the cache!
You received 382.1 NOK.
> SEK
> 75
Checking the cache…
Sorry, but it is not in the cache!
You received 624.66 SEK.
> NOK
> 55
Checking the cache…
Oh! It is in the cache!
You received 467.02 NOK.
> ISK
> 91
Checking the cache…
Sorry, but it is not in the cache!
You received 11708.38 ISK.
```
